# Gradio-Powered Speech-to-Text UI with Google Cloud STT and Modal Deployment

A modern, user-friendly web interface for transcribing speech from audio files using Google Cloud Speech-to-Text (STT), built with Gradio for the frontend and Modal for scalable serverless backend execution.

## 🚀 Features

- **Drag-and-drop audio file upload** via clean Gradio interface
- **Multiple audio format support** (WAV, MP3, M4A, FLAC, etc.)
- **Serverless processing** with Modal for scalable transcription
- **Google Cloud Speech-to-Text** integration for accurate transcription
- **Multiple deployment options**: Local, Modal Web, and HuggingFace Spaces
- **Real-time progress tracking** and error handling
- **Modern, responsive UI** with audio preview capabilities

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌────────────────────┐
│   Gradio UI     │────│   Modal Backend  │────│  Google Cloud STT  │
│   (Frontend)    │    │   (Serverless)   │    │      (API)         │
└─────────────────┘    └──────────────────┘    └────────────────────┘
```

## 📁 Project Structure

```
gradio-modal-gcp-speech-ui/
├── src/
│   ├── gradio_app/          # Gradio frontend application
│   ├── modal_functions/     # Modal serverless functions
│   ├── gcp_client/          # Google Cloud STT client
│   └── utils/               # Shared utilities
├── config/
│   ├── settings.py          # Application configuration
│   └── gcp_config.py        # Google Cloud configuration
├── docs/
│   ├── setup/               # Setup and deployment guides
│   └── api/                 # API documentation
├── tests/                   # Test files
├── samples/                 # Sample audio files for testing
├── requirements.txt         # Python dependencies
├── pyproject.toml          # Modern Python project configuration
└── README.md               # This file
```

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.8+
- Google Cloud Platform account
- Modal account and API key
- FFmpeg (for audio processing)

### 1. Clone and Setup Environment

```bash
# Clone the repository
git clone <your-repo-url>
cd gradio-modal-gcp-speech-ui

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Google Cloud Setup

Follow the detailed setup guide in [`docs/setup/gcp-setup.md`](docs/setup/gcp-setup.md) to:
- Create a GCP project
- Enable Speech-to-Text API
- Create service account credentials
- Set up authentication

### 3. Modal Setup

```bash
# Install Modal CLI and authenticate
pip install modal
modal token new
```

### 4. Environment Configuration

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your credentials
# - GCP service account key path
# - Modal API key
# - Other configuration options
```

## 🚀 Usage

### Local Development

```bash
# Run the Gradio app locally
python src/gradio_app/app.py
```

### Modal Deployment

```bash
# Deploy to Modal
modal deploy src/modal_functions/speech_processor.py
```

### HuggingFace Spaces

See [`docs/setup/huggingface-deployment.md`](docs/setup/huggingface-deployment.md) for deployment instructions.

## 📊 Supported Audio Formats

- WAV (recommended)
- MP3
- M4A
- FLAC
- OGG
- WEBM (audio)

## 🎯 Roadmap

- [x] Basic Gradio interface
- [x] Modal backend integration
- [x] Google Cloud STT integration
- [x] Multi-format audio support
- [ ] HuggingFace ASR model comparison
- [ ] LLM-powered transcription post-processing
- [ ] Batch processing capabilities
- [ ] Real-time streaming transcription
- [ ] Multi-language support
- [ ] Custom vocabulary support

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- 📖 Check the [documentation](docs/)
- 🐛 Report issues on [GitHub Issues](https://github.com/yourusername/gradio-modal-gcp-speech-ui/issues)
- 💬 Join discussions in [GitHub Discussions](https://github.com/yourusername/gradio-modal-gcp-speech-ui/discussions)

## 🏷️ Tags

`#gradio` `#modal` `#speech-to-text` `#google-cloud` `#asr` `#ai` `#serverless` `#python`
