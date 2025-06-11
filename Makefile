# Makefile for Gradio Modal GCP Speech UI

.PHONY: help setup install check-env test lint format clean run dev

# Default target
help:
	@echo "🚀 Gradio Modal GCP Speech UI Development Commands"
	@echo ""
	@echo "Setup & Installation:"
	@echo "  setup          - Run complete development environment setup"
	@echo "  install        - Install Python dependencies"
	@echo "  check-env      - Check environment configuration"
	@echo ""
	@echo "Development:"
	@echo "  test           - Run tests"
	@echo "  format         - Format code with black and isort"
	@echo "  lint           - Lint code with flake8 and mypy"
	@echo "  clean          - Clean temporary files and caches"
	@echo ""
	@echo "Running:"
	@echo "  run            - Run the Gradio app locally"
	@echo "  dev            - Run in development mode with auto-reload"
	@echo ""
	@echo "Deployment:"
	@echo "  deploy-modal   - Deploy to Modal"
	@echo "  deploy-hf      - Deploy to HuggingFace Spaces"

# Setup development environment
setup:
	@echo "🔧 Setting up development environment..."
	@chmod +x setup.sh
	@./setup.sh

# Install dependencies
install:
	@echo "📦 Installing dependencies..."
	@pip3 install -r requirements.txt

# Check environment configuration
check-env:
	@echo "🔍 Checking environment configuration..."
	@if [ ! -f .env ]; then \
		echo "❌ .env file not found. Copy .env.example to .env and configure it."; \
		exit 1; \
	fi
	@echo "✅ .env file found"
	@python -c "from config.settings import settings; print('✅ Configuration loaded successfully')" || echo "❌ Configuration error"

# Run tests
test:
	@echo "🧪 Running tests..."
	@pytest tests/ -v --cov=src --cov-report=term-missing --cov-report=html

# Format code
format:
	@echo "🎨 Formatting code..."
	@black src/ tests/ config/
	@isort src/ tests/ config/
	@echo "✅ Code formatted"

# Lint code
lint:
	@echo "🔍 Linting code..."
	@flake8 src/ tests/ config/
	@mypy src/ config/
	@echo "✅ Linting complete"

# Clean temporary files and caches
clean:
	@echo "🧹 Cleaning temporary files and caches..."
	@find . -type f -name "*.pyc" -delete
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	@rm -rf .pytest_cache/
	@rm -rf .coverage
	@rm -rf htmlcov/
	@rm -rf .mypy_cache/
	@rm -rf dist/
	@rm -rf build/
	@echo "✅ Cleanup complete"

# Run the Gradio app locally
run:
	@echo "🚀 Starting Gradio app..."
	@python3 src/app.py

# Run in development mode with auto-reload
dev:
	@echo "🔧 Starting development server with auto-reload..."
	@python3 -m gradio src/app.py --reload

# TODO: Add deployment commands (deploy-modal, deploy-hf)
