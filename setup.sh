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

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️ Upgrading pip..."
pip3 install --upgrade pip

# Install dependencies
echo "📚 Installing dependencies..."
pip3 install -r requirements.txt

# Create .env file from template if it doesn't exist
if [ ! -f ".env" ]; then
    echo "⚙️ Creating .env file from template..."
    cp .env.example .env
    echo "📝 Please edit .env file with your actual configuration values"
else
    echo "✅ .env file already exists"
fi

# Check if FFmpeg is installed (required for audio processing)
if ! command -v ffmpeg &> /dev/null; then
    echo "⚠️ FFmpeg is not installed. Please install FFmpeg for audio processing:"
    echo "   macOS: brew install ffmpeg"
    echo "   Ubuntu: sudo apt-get install ffmpeg"
    echo "   Windows: Download from https://ffmpeg.org/download.html"
else
    echo "✅ FFmpeg detected"
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env file with your configuration:"
echo "   - Add your Google Cloud credentials path"
echo "   - Add your Modal API token"
echo "   - Configure other settings as needed"
echo ""
echo "2. Follow the Google Cloud setup guide:"
echo "   docs/setup/gcp-setup.md (will be created in next commit)"
echo ""
echo "3. Activate the virtual environment:"
echo "   source venv/bin/activate"
echo ""
echo "4. Run the application (when implemented):"
echo "   python src/gradio_app/app.py"
echo ""
echo "🔍 For more information, see README.md"
