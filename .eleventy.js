const htmlmin = require('html-minifier-terser');

module.exports = function(eleventyConfig) {

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

  // Date filter for footer copyright
  eleventyConfig.addFilter("date", function(date, format) {
    const d = date === "now" ? new Date() : new Date(date);
    if (format === "Y") {
      return d.getFullYear();
    }
    return d.toISOString();
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
