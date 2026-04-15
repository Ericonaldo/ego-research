#!/bin/bash
# Download Project Aria datasets using aria_dataset_downloader
#
# Prerequisites:
#   1. pip install 'projectaria-tools[all]'
#   2. Get CDN file from https://www.projectaria.com/datasets/
#
# Usage:
#   bash aria/scripts/download_dataset.sh <cdn_file.json> [output_dir] [data_types]
#
# Examples:
#   # Download VRS only
#   bash aria/scripts/download_dataset.sh adt_download_urls.json ./aria/data/adt 0
#
#   # Download VRS + MPS trajectory + eye gaze
#   bash aria/scripts/download_dataset.sh aea_download_urls.json ./aria/data/aea "0 1 3"
#
#   # Download everything
#   bash aria/scripts/download_dataset.sh adt_download_urls.json ./aria/data/adt "0 1 2 3 4 5 6 7 8 9"

set -e

CDN_FILE="${1:?Usage: $0 <cdn_file.json> [output_dir] [data_types]}"
OUTPUT_DIR="${2:-./aria_data}"
DATA_TYPES="${3:-0}"  # Default: VRS only

if [ ! -f "$CDN_FILE" ]; then
    echo "Error: CDN file not found: $CDN_FILE"
    echo ""
    echo "To get a CDN file:"
    echo "  1. Go to https://www.projectaria.com/datasets/"
    echo "  2. Choose a dataset (e.g., ADT, AEA)"
    echo "  3. Enter your email and agree to the license"
    echo "  4. Download the CDN JSON file"
    exit 1
fi

# Check if aria_dataset_downloader is available
if ! command -v aria_dataset_downloader &> /dev/null; then
    echo "Error: aria_dataset_downloader not found"
    echo "Install with: pip install 'projectaria-tools[all]'"
    exit 1
fi

echo "=== Project Aria Dataset Download ==="
echo "CDN file:    $CDN_FILE"
echo "Output dir:  $OUTPUT_DIR"
echo "Data types:  $DATA_TYPES"
echo ""

mkdir -p "$OUTPUT_DIR"

# Run downloader
aria_dataset_downloader \
    --cdn_file "$CDN_FILE" \
    --output_folder "$OUTPUT_DIR" \
    --data_types $DATA_TYPES

echo ""
echo "=== Download complete ==="
echo "Data saved to: $OUTPUT_DIR"
