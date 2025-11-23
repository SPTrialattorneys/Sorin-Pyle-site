#!/usr/bin/env python3
"""
Comprehensive Image Optimization using TinyPNG API
Optimizes ALL site images including attorney profiles, gallery photos, and blog images
"""

import tinify
import os

# Set your TinyPNG API key
tinify.key = "79c7zSWGqVr12RTCkbZPbLkgrls4HH2N"

# Define all images to process
images_to_process = [
    # ========================================
    # ATTORNEY PROFILE GALLERY PHOTOS (400x500 portrait)
    # ========================================
    {
        "name": "Jonathan Pyle - Trial Attorney West Michigan",
        "source": "samples/originals/IMG_3086.jpg",
        "crop": {"method": "cover", "width": 3200, "height": 4000},  # 4:5 ratio, from top
        "outputs": [
            {"width": 400, "filename": "images/jonathan-pyle-trial-attorney-west-michigan.avif"}
        ]
    },
    {
        "name": "Jonathan Pyle - DUI Lawyer Ottawa County",
        "source": "samples/originals/IMG_1176.HEIC",
        "crop": {"method": "cover", "width": 2000, "height": 2500},  # 4:5 ratio, from top
        "outputs": [
            {"width": 400, "filename": "images/jonathan-pyle-dui-lawyer-ottawa-county.avif"}
        ]
    },
    {
        "name": "Jonathan Pyle - Criminal Defense Grand Rapids",
        "source": "samples/originals/IMG_2670.jpg",
        "crop": {"method": "cover", "width": 2800, "height": 3500},  # 4:5 ratio, from top
        "outputs": [
            {"width": 400, "filename": "images/jonathan-pyle-criminal-defense-grand-rapids.avif"}
        ]
    },
    {
        "name": "Sorin Panainte - Trial Attorney West Michigan",
        "source": "samples/originals/IMG_2854.jpg",
        "crop": {"method": "cover", "width": 2800, "height": 3500},  # 4:5 ratio, from top
        "outputs": [
            {"width": 400, "filename": "images/sorin-panainte-trial-attorney-west-michigan.avif"}
        ]
    },
    {
        "name": "Sorin Panainte - Criminal Defense Grand Rapids",
        "source": "samples/originals/IMG_3047.jpg",
        "crop": {"method": "cover", "width": 3200, "height": 4000},  # 4:5 ratio, from top
        "outputs": [
            {"width": 400, "filename": "images/sorin-panainte-criminal-defense-grand-rapids.avif"}
        ]
    },
    {
        "name": "Sorin Panainte - Felony Defense Lawyer Holland",
        "source": "samples/originals/IMG_2747.jpg",
        "crop": {"method": "cover", "width": 3000, "height": 3750},  # 4:5 ratio, from top
        "outputs": [
            {"width": 400, "filename": "images/sorin-panainte-felony-defense-lawyer-holland.avif"}
        ]
    },

    # ========================================
    # ATTORNEY PROFILE MAIN PHOTOS (400x500 portrait)
    # ========================================
    {
        "name": "Jonathan Pyle - Criminal Lawyer Holland Michigan (Profile)",
        "source": "samples/originals/IMG_3031.jpg",
        "crop": {"method": "cover", "width": 3387, "height": 3387},  # Square
        "outputs": [
            {"width": 400, "filename": "images/jonathan-pyle-criminal-lawyer-holland-michigan.avif"}
        ]
    },
    {
        "name": "Sorin Panainte - Criminal Lawyer Holland Michigan (Profile)",
        "source": "samples/originals/IMG_3013.jpg",
        "crop": {"method": "cover", "width": 3297, "height": 3297},  # Square
        "outputs": [
            {"width": 400, "filename": "images/sorin-panainte-criminal-lawyer-holland-michigan.avif"}
        ]
    },

    # ========================================
    # ATTORNEYS PAGE PHOTOS (400x400 square)
    # ========================================
    {
        "name": "Jonathan Pyle - Holland Michigan Criminal Lawyer (Attorneys Page)",
        "source": "samples/originals/IMG_2875.jpg",
        "crop": {"method": "cover", "width": 3200, "height": 3200},  # Square
        "outputs": [
            {"width": 400, "filename": "images/jonathan-pyle-holland-michigan-criminal-lawyer.avif"}
        ]
    },
    {
        "name": "Sorin Panainte - Holland Michigan Criminal Lawyer (Attorneys Page)",
        "source": "samples/originals/IMG_2811.jpg",
        "crop": {"method": "cover", "width": 3200, "height": 3200},  # Square
        "outputs": [
            {"width": 400, "filename": "images/sorin-panainte-holland-michigan-criminal-lawyer.avif"}
        ]
    },

    # ========================================
    # BLOG & LARGE IMAGES (responsive sizes)
    # ========================================
    {
        "name": "Sorin at Gun Lake Tribe Expungement Fair",
        "source": "samples/Sorin_gun_lake.jpg",
        "crop": None,  # Use original aspect ratio
        "outputs": [
            {"width": 800, "filename": "images/sorin-panainte-gun-lake-tribe-expungement-fair.avif"}
        ]
    },

    # ========================================
    # EXISTING LARGE IMAGES TO RE-OPTIMIZE
    # (Already on site but poorly optimized)
    # ========================================
    {
        "name": "Parking Guide (from existing)",
        "source": "images/parking_guide.avif",  # Re-optimize existing
        "crop": None,
        "outputs": [
            {"width": 700, "filename": "images/parking_guide_web.avif"}
        ]
    },
    {
        "name": "Ottawa County Courthouse (from existing)",
        "source": "images/ottawa-county-courthouse.avif",  # Re-optimize existing
        "crop": None,
        "outputs": [
            {"width": 1200, "filename": "images/ottawa-county-courthouse.avif"}  # Overwrites itself
        ]
    },
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
    except Exception as e:
        print(f"    [ERROR] Unexpected error: {e}")
        return False

    return True

def main():
    print("=" * 60)
    print("TinyPNG AVIF Image Optimization - ALL SITE IMAGES")
    print("=" * 60)
    print()

    # Check API key is valid
    try:
        tinify.validate()
        print(f"[OK] API Key validated")
        print(f"[OK] Compressions this month: {tinify.compression_count}")
        print(f"[OK] Free tier remaining: {500 - tinify.compression_count}/500")
        print()
    except tinify.Error as e:
        print(f"[ERROR] API Key validation failed: {e}")
        return

    # Process each image
    total_processed = 0
    total_failed = 0
    total_skipped = 0

    for image in images_to_process:
        print(f"Processing: {image['name']}")
        print(f"  Source: {image['source']}")

        # Check if source exists
        if not os.path.exists(image['source']):
            print(f"  [WARNING] Source file not found! Skipping...")
            total_skipped += len(image['outputs'])
            print()
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
    if total_skipped > 0:
        print(f"[WARNING] Skipped (source not found): {total_skipped} images")
    if total_failed > 0:
        print(f"[ERROR] Failed: {total_failed} images")
    print(f"API compressions used this session: {tinify.compression_count - 170}")
    print(f"Total compressions this month: {tinify.compression_count}/500")
    print()

    # File size comparison
    print("Final Image Sizes:")
    print("-" * 60)
    total_size = 0
    for image in images_to_process:
        for output in image['outputs']:
            if os.path.exists(output['filename']):
                size = os.path.getsize(output['filename']) / 1024
                total_size += size
                print(f"{os.path.basename(output['filename'])}: {size:.1f} KB")
    print("-" * 60)
    print(f"Total optimized size: {total_size:.1f} KB ({total_size/1024:.2f} MB)")
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
