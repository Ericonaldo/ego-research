#!/bin/bash
# Setup script for Project Aria tools
# Usage: bash aria/scripts/setup.sh

set -e

VENV_DIR="${1:-./aria_env}"

echo "=== Setting up Project Aria environment ==="

# Create virtual environment
python3 -m venv "$VENV_DIR"
source "$VENV_DIR/bin/activate"

# Upgrade pip
pip install --upgrade pip

# Install projectaria_tools with all extras
pip install 'projectaria-tools[all]'

# Install additional useful packages
pip install matplotlib numpy opencv-python-headless pillow tqdm

echo ""
echo "=== Setup complete ==="
echo "Activate with: source $VENV_DIR/bin/activate"
echo ""
echo "Next steps:"
echo "1. Go to https://www.projectaria.com/datasets/ and get a CDN file"
echo "2. Run: aria_dataset_downloader -c <cdn_file.json> -o ./aria/data/ -d 0"
echo "3. Use aria/scripts/process_vrs.py to extract data from VRS files"
