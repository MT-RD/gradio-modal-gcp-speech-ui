# Makefile for Gradio Modal GCP Speech UI

.PHONY: help setup install check-env test lint format

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

# TODO: Add utility commands (clean)
# TODO: Add development and deployment commands (run, dev, deploy-modal, deploy-hf)
