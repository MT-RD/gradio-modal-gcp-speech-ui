# Gradio-Powered Speech-to-Text UI with Google Cloud STT and Modal Deployment

A modern, user-friendly web interface for transcribing speech from audio files using Google Cloud Speech-to-Text (STT), built with Gradio for the frontend and Modal for scalable serverless backend execution.

## 🚀 Features

### ✅ Currently Implemented
- **Drag-and-drop audio file upload** via clean Gradio interface
- **Multiple audio format support** (WAV, MP3, M4A, OGG, FLAC, AAC, WMA)
- **File validation system** with format and size checking (100MB limit)
- **Audio preview functionality** with built-in player
- **Detailed file information display** (name, size, format, upload time)
- **Enhanced error handling** with troubleshooting guidance
- **Professional UI/UX** with welcome messages and status indicators
- **Comprehensive audio analysis** with librosa integration
- **Audio quality metrics** (duration, sample rate, channels, RMS energy)
- **Robust file format handling** with graceful fallbacks
- **GCP client foundation** with authentication structure

### 🚧 In Development
- **Complete GCP Speech-to-Text** integration for transcription
- **Audio quality validation** against GCP requirements
- **Serverless processing** with Modal for scalable transcription
- **Real-time progress tracking** during transcription

### 🎯 Planned Features
- **Multiple deployment options**: Local, Modal Web, and HuggingFace Spaces
- **Language selection interface** with 50+ supported languages
- **Batch processing capabilities** for multiple files
- **Transcription export** (TXT, JSON, SRT formats)
- **Audio duration detection** and advanced file analysis

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

### Current Local Development (Step 2 - UI Ready)

```bash
# Quick start with automated setup
./setup.sh

# Or manual setup:
# 1. Create virtual environment
python -m venv venv
source venv/bin/activate

# 2. Install dependencies
make install

# 3. Run the application
make run
# Application will be available at http://127.0.0.1:7860

# For development mode with auto-reload
make dev
```

### Testing Current Features

1. **Upload Audio Files**: Test with WAV, MP3, M4A, OGG, FLAC, AAC, or WMA files
2. **File Validation**: Try invalid formats or large files (>100MB) to see error handling
3. **Audio Preview**: Use the built-in player to preview uploaded audio
4. **File Information**: View detailed file metadata and processing status

### Future Usage (After GCP Integration)

```bash
# Configure environment
cp .env.example .env
# Edit .env with your GCP credentials

# Deploy to Modal (Step 4)
modal deploy src/modal_functions/speech_processor.py

# Deploy to HuggingFace Spaces (Step 4)
# See docs/setup/huggingface-deployment.md
```

## 📊 Supported Audio Formats

- **WAV** (recommended for best quality)
- **MP3** (most common format)
- **M4A** (Apple audio format)
- **OGG** (open source format)
- **FLAC** (lossless compression)
- **AAC** (Advanced Audio Coding)
- **WMA** (Windows Media Audio)

**File Size Limit**: 100MB per file  
**Validation**: Automatic format and size checking with detailed error messages

## 🎯 Roadmap

### ✅ Completed (Phase 1-2)
- [x] Project structure and build system
- [x] Comprehensive configuration management  
- [x] Basic Gradio interface with audio upload
- [x] File validation and error handling
- [x] Audio preview and file information display
- [x] Enhanced UI/UX with professional feedback

### ✅ Completed (Phase 3A - GCP Foundation)
- [x] GCP client package structure (`src/gcp_client/`)
- [x] Comprehensive audio analysis with librosa integration
- [x] Audio format validation for all 7 GCP-supported formats
- [x] Detailed audio metrics extraction (duration, sample rate, channels)
- [x] Robust error handling with user-friendly messages
- [x] AudioProcessor with graceful loading fallbacks
- [x] SpeechToTextClient authentication foundation

### 🚧 In Progress (Phase 3B)
- [ ] Complete GCP Speech-to-Text client implementation
- [ ] Audio quality validation against GCP requirements
- [ ] Synchronous and asynchronous transcription methods

### 📋 Planned (Phase 4-5)
- [ ] Modal backend integration and deployment
- [ ] HuggingFace Spaces deployment
- [ ] Language selection interface (50+ languages)
- [ ] Audio duration detection with librosa
- [ ] Batch processing capabilities
- [ ] Transcription export (TXT, JSON, SRT)
- [ ] HuggingFace ASR model comparison
- [ ] LLM-powered transcription post-processing
- [ ] Real-time streaming transcription
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
