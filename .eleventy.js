const htmlmin = require('html-minifier-terser');
const pluginRss = require("@11ty/eleventy-plugin-rss");

module.exports = function(eleventyConfig) {

  // Add RSS plugin for feed generation
  eleventyConfig.addPlugin(pluginRss);

  // HTML Minification Transform (production only)
  if (process.env.NODE_ENV === 'production') {
    eleventyConfig.addTransform("htmlmin", function(content, outputPath) {
      if (outputPath && outputPath.endsWith(".html")) {
        return htmlmin.minify(content, {
          useShortDoctype: true,
          removeComments: true,
          collapseWhitespace: true,
          minifyCSS: true,
          minifyJS: true,
          keepClosingSlash: true,
          conservativeCollapse: true
        });
      }
      return content;
    });
  }

  // Pass-through copy for static files
  eleventyConfig.addPassthroughCopy("src/static");

  // CSS is processed by PostCSS (see package.json build:css script)
  // JS is processed by esbuild (see package.json build:js script)

  // Copy images to dist (will be processed by Sharp later)
  eleventyConfig.addPassthroughCopy({"images": "images"});

  // Copy fonts if they exist
  eleventyConfig.addPassthroughCopy({"fonts": "fonts"});

  // Copy vcard files for digital business cards
  eleventyConfig.addPassthroughCopy({"vcards": "vcards"});

  // Copy Cloudflare Pages configuration files
  eleventyConfig.addPassthroughCopy({"_headers": "_headers"});

  // Blog posts collection
  eleventyConfig.addCollection("posts", function(collectionApi) {
    return collectionApi.getFilteredByGlob("src/blog/posts/*.md")
      .filter(post => !post.data.draft)
      .sort((a, b) => b.date - a.date);
  });

  // Posts by category collection
  eleventyConfig.addCollection("postsByCategory", function(collectionApi) {
    const posts = collectionApi.getFilteredByGlob("src/blog/posts/*.md")
      .filter(post => !post.data.draft);
    const categories = {};

    posts.forEach(post => {
      const category = post.data.category || "uncategorized";
      if (!categories[category]) {
        categories[category] = [];
      }
      categories[category].push(post);
    });

    // Sort posts within each category
    Object.keys(categories).forEach(category => {
      categories[category].sort((a, b) => b.date - a.date);
    });

    return categories;
  });

  // Date filter for footer copyright
  eleventyConfig.addFilter("date", function(date, format) {
    const d = date === "now" ? new Date() : new Date(date);
    if (format === "Y") {
      return d.getFullYear();
    }
    return d.toISOString();
  });

  // Blog date filters
  eleventyConfig.addFilter("readableDate", function(date) {
    return new Date(date).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    });
  });

  eleventyConfig.addFilter("isoDate", function(date) {
    return new Date(date).toISOString().split('T')[0];
  });

  eleventyConfig.addFilter("htmlDateString", function(date) {
    return new Date(date).toISOString();
  });

  // Replace filter for image srcset
  eleventyConfig.addFilter("replace", function(str, find, replace) {
    return str.replace(new RegExp(find, 'g'), replace);
  });

  // Critical CSS filter - reads and returns CSS file contents for inlining
  eleventyConfig.addFilter("criticalCSS", function(filename) {
    if (!filename) return '';

    const fs = require('fs');
    const path = require('path');
    const cssPath = path.join(__dirname, 'src', '_data', filename);

    try {
      if (fs.existsSync(cssPath)) {
        return fs.readFileSync(cssPath, 'utf8');
      }
    } catch (error) {
      console.error(`Error reading critical CSS file: ${filename}`, error);
    }

    return '';
  });

  // Responsive image shortcode
  eleventyConfig.addShortcode("responsiveImage", function(src, alt, sizes = "100vw", loading = "lazy") {
    // Extract basename (filename without extension)
    const basename = src.replace(/\.[^/.]+$/, '').replace(/^\/images\//, '');

    // Load image manifest
    let manifest = {};
    try {
      const manifestPath = require('path').join(__dirname, 'src', '_data', 'images.json');
      if (require('fs').existsSync(manifestPath)) {
        manifest = JSON.parse(require('fs').readFileSync(manifestPath, 'utf8'));
      }
    } catch (error) {
      // Manifest doesn't exist yet, return simple img tag
      return `<img src="${src}" alt="${alt}" loading="${loading}">`;
    }

    const imageData = manifest[basename];
    if (!imageData) {
      // Image not in manifest, return simple img tag
      return `<img src="${src}" alt="${alt}" loading="${loading}">`;
    }

    // Group variants by format
    const variantsByFormat = imageData.variants.reduce((acc, variant) => {
      if (!acc[variant.format]) acc[variant.format] = [];
      acc[variant.format].push(variant);
      return acc;
    }, {});

    // Generate srcset for each format
    const sources = [];

    // AVIF (most efficient)
    if (variantsByFormat.avif) {
      const srcset = variantsByFormat.avif
        .map(v => `${v.url} ${v.width}w`)
        .join(', ');
      sources.push(`<source type="image/avif" srcset="${srcset}" sizes="${sizes}">`);
    }

    // WebP (widely supported)
    if (variantsByFormat.webp) {
      const srcset = variantsByFormat.webp
        .map(v => `${v.url} ${v.width}w`)
        .join(', ');
      sources.push(`<source type="image/webp" srcset="${srcset}" sizes="${sizes}">`);
    }

    // Fallback to original format (JPEG/PNG)
    const fallbackFormat = variantsByFormat.jpeg || variantsByFormat.jpg || variantsByFormat.png;
    let imgTag = `<img src="${src}" alt="${alt}" loading="${loading}">`;

    if (fallbackFormat && fallbackFormat.length > 0) {
      const srcset = fallbackFormat
        .map(v => `${v.url} ${v.width}w`)
        .join(', ');
      imgTag = `<img src="${fallbackFormat[0].url}" alt="${alt}" srcset="${srcset}" sizes="${sizes}" loading="${loading}">`;
    }

    // Return picture element with sources
    return `<picture>${sources.join('')}${imgTag}</picture>`;
  });

  // Watch for source file changes during development
  eleventyConfig.addWatchTarget("./src/assets/styles/");
  eleventyConfig.addWatchTarget("./src/assets/scripts/");

  // Build performance optimizations
  eleventyConfig.setQuietMode(true); // Reduce console output

  // Faster builds by using cached data
  eleventyConfig.setDataDeepMerge(true);

  return {
    dir: {
      input: "src",
      output: "dist",
      includes: "_includes",
      data: "_data"
    },
    templateFormats: ["njk", "html", "md"],
    htmlTemplateEngine: "njk",
    markdownTemplateEngine: "njk",

    // Performance: Use more efficient template compiler
    pathPrefix: "/",

    // Performance: Enable incremental builds
    markdownTemplateEngine: "njk"
  };
};
