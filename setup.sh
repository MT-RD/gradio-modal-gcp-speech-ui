#!/bin/bash

# Setup script for Gradio Modal GCP Speech UI
# This script sets up the development environment

set -e

echo "🚀 Setting up Gradio Modal GCP Speech UI development environment..."

# Check if Python 3.8+ is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed. Please install Python 3.8 or later."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
REQUIRED_VERSION="3.8"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
    echo "❌ Python $REQUIRED_VERSION or later is required. Found Python $PYTHON_VERSION."
    exit 1
fi

echo "✅ Python $PYTHON_VERSION detected"

# TODO: Add virtual environment setup
# TODO: Add dependencies installation
# TODO: Add environment file setup
# TODO: Add FFmpeg check and completion message

echo "🔧 Setup script skeleton ready for incremental implementation..."
