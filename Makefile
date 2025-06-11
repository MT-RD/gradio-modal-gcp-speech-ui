# Makefile for Gradio Modal GCP Speech UI

.PHONY: help install setup test lint format clean dev deploy-modal

# Default target
help:
	@echo "Available commands:"
	@echo "  setup          - Set up development environment"
	@echo "  install        - Install dependencies"
	@echo "  test           - Run tests"
	@echo "  lint           - Run linting (flake8, mypy)"
	@echo "  format         - Format code (black, isort)"
	@echo "  clean          - Clean up temporary files"
	@echo "  dev            - Run in development mode"
	@echo "  deploy-modal   - Deploy to Modal (future)"

# Set up the entire development environment
setup:
	@echo "Setting up development environment..."
	@chmod +x setup.sh
	@./setup.sh

# Install dependencies only
install:
	@echo "Installing dependencies..."
	@pip install -r requirements.txt

# Run tests
test:
	@echo "Running tests..."
	@python -m pytest tests/ -v

# Run linting
lint:
	@echo "Running linting..."
	@python -m flake8 src/ tests/ config/
	@python -m mypy src/ config/

# Format code
format:
	@echo "Formatting code..."
	@python -m black src/ tests/ config/
	@python -m isort src/ tests/ config/

# Clean up temporary files
clean:
	@echo "Cleaning up..."
	@find . -type f -name "*.pyc" -delete
	@find . -type d -name "__pycache__" -delete
	@find . -type d -name "*.egg-info" -exec rm -rf {} +
	@find . -type f -name ".coverage" -delete
	@rm -rf build/ dist/ .pytest_cache/ .mypy_cache/

# Run in development mode (placeholder)
dev:
	@echo "Starting development server..."
	@echo "This will be implemented in future commits"
	@echo "For now, activate venv and run: python src/gradio_app/app.py"

# Deploy to Modal (placeholder)
deploy-modal:
	@echo "Deploying to Modal..."
	@echo "This will be implemented in future commits"
	@echo "Command will be: modal deploy src/modal_functions/speech_processor.py"

# Check environment setup
check-env:
	@echo "Checking environment setup..."
	@python -c "import sys; print(f'Python: {sys.version}')"
	@python -c "import gradio; print(f'Gradio: {gradio.__version__}')" 2>/dev/null || echo "❌ Gradio not installed"
	@python -c "import modal; print('✅ Modal installed')" 2>/dev/null || echo "❌ Modal not installed"
	@python -c "import google.cloud.speech; print('✅ Google Cloud Speech installed')" 2>/dev/null || echo "❌ Google Cloud Speech not installed"
	@ffmpeg -version >/dev/null 2>&1 && echo "✅ FFmpeg available" || echo "❌ FFmpeg not available"
