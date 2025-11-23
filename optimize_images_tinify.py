#!/usr/bin/env python3
"""
Optimize images using TinyPNG API for AVIF format
Processes attorney photos and hero image from originals folder
Creates responsive sizes: 220w, 400w, 450w, 800w
"""

import tinify
import os

# Set your TinyPNG API key
tinify.key = "79c7zSWGqVr12RTCkbZPbLkgrls4HH2N"

# Define image processing tasks
# Format: (source_file, output_sizes, crop_params)
images_to_process = [
    {
        "name": "Sorin Panainte",
        "source": "samples/originals/IMG_3013.jpg",
        "crop": {"method": "cover", "width": 3297, "height": 3297},  # Square crop from top
        "outputs": [
            {"width": 220, "filename": "images/sorin-panainte-criminal-defense-attorney-holland-mi-220w.avif"},
            {"width": 400, "filename": "images/sorin-panainte-criminal-defense-attorney-holland-mi.avif"}
        ]
    },
    {
        "name": "Jonathan Pyle",
        "source": "samples/originals/IMG_3031.jpg",
        "crop": {"method": "cover", "width": 3387, "height": 3387},  # Square crop from top
        "outputs": [
            {"width": 220, "filename": "images/jonathan-pyle-criminal-defense-attorney-holland-mi-220w.avif"},
            {"width": 400, "filename": "images/jonathan-pyle-criminal-defense-attorney-holland-mi.avif"}
        ]
    },
    {
        "name": "Hero Image (attorneys seated)",
        "source": "samples/originals/attorneys_seated.png",
        "crop": None,  # No crop, use original aspect ratio
        "outputs": [
            {"width": 450, "filename": "images/holland-michigan-criminal-defense-lawyers-450w.avif"},
            {"width": 800, "filename": "images/holland-michigan-criminal-defense-lawyers.avif"}
        ]
    }
]

def optimize_image(source_path, output_path, width, crop_params=None):
    """
    Optimize and resize image using Tinify API

    Args:
        source_path: Path to source image
        output_path: Path to save optimized image
        width: Target width in pixels
        crop_params: Optional dict with crop parameters
    """
    print(f"  Processing: {os.path.basename(output_path)} ({width}px wide)...")

    try:
        # Load source image
        source = tinify.from_file(source_path)

        # Apply crop if specified
        if crop_params:
            source = source.resize(
                method=crop_params["method"],
                width=crop_params["width"],
                height=crop_params["height"]
            )

        # Resize to target width (maintains aspect ratio)
        resized = source.resize(method="scale", width=width)

        # Convert to AVIF and save
        converted = resized.convert(type=["image/avif"])
        converted.to_file(output_path)

        # Get file size
        file_size = os.path.getsize(output_path) / 1024  # KB
        print(f"    [OK] Saved: {file_size:.1f} KB")

    except tinify.Error as e:
        print(f"    [ERROR] Error: {e}")
        return False

    return True

def main():
    print("=" * 60)
    print("TinyPNG AVIF Image Optimization")
    print("=" * 60)
    print()

    # Check API key is valid
    try:
        tinify.validate()
        print(f"[OK] API Key validated")
        print(f"[OK] Compressions this month: {tinify.compression_count}")
        print()
    except tinify.Error as e:
        print(f"[ERROR] API Key validation failed: {e}")
        return

    # Process each image
    total_processed = 0
    total_failed = 0

    for image in images_to_process:
        print(f"Processing: {image['name']}")
        print(f"  Source: {image['source']}")

        # Check if source exists
        if not os.path.exists(image['source']):
            print(f"  [ERROR] Source file not found!")
            total_failed += len(image['outputs'])
            continue

        # Process each output size
        for output in image['outputs']:
            success = optimize_image(
                source_path=image['source'],
                output_path=output['filename'],
                width=output['width'],
                crop_params=image['crop']
            )

            if success:
                total_processed += 1
            else:
                total_failed += 1

        print()

    # Summary
    print("=" * 60)
    print("Optimization Complete!")
    print("=" * 60)
    print(f"[OK] Successfully processed: {total_processed} images")
    if total_failed > 0:
        print(f"[ERROR] Failed: {total_failed} images")
    print(f"API compressions used: {tinify.compression_count}")
    print()

    # File size comparison
    print("Before/After Comparison:")
    print("-" * 60)
    for image in images_to_process:
        for output in image['outputs']:
            if os.path.exists(output['filename']):
                size = os.path.getsize(output['filename']) / 1024
                print(f"{os.path.basename(output['filename'])}: {size:.1f} KB")
    print()

if __name__ == "__main__":
    # Check if tinify is installed
    try:
        import tinify
    except ImportError:
        print("Error: tinify package not installed")
        print("Install with: pip install tinify")
        exit(1)

    main()
