# Makefile for Gradio Modal GCP Speech UI

.PHONY: help setup install check-env test lint format clean run dev deploy-modal deploy-hf

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

# Deploy to Modal
deploy-modal:
	@echo "🚀 Deploying to Modal..."
	@echo "🔍 Checking Modal authentication..."
	@modal token list || (echo "❌ Modal not authenticated. Run 'modal token new' first." && exit 1)
	@echo "📦 Deploying application..."
	@modal deploy src/modal_app.py
	@echo "✅ Deployment to Modal complete"

# Deploy to HuggingFace Spaces
deploy-hf:
	@echo "🤗 Deploying to HuggingFace Spaces..."
	@echo "🔍 Checking git configuration..."
	@git status > /dev/null 2>&1 || (echo "❌ Not a git repository. Initialize with 'git init' first." && exit 1)
	@echo "📦 Pushing to HuggingFace Spaces..."
	@echo "ℹ️  Make sure you've set up HF Spaces remote: git remote add hf https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME"
	@git add -A
	@git commit -m "Deploy to HuggingFace Spaces - $(shell date '+%Y-%m-%d %H:%M:%S')" || echo "No changes to commit"
	@git push hf main || (echo "❌ Push failed. Check HF remote configuration." && exit 1)
	@echo "✅ Deployment to HuggingFace Spaces complete"
