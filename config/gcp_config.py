"""
Google Cloud Platform Configuration

This module contains specific configuration for Google Cloud Speech-to-Text API.
"""

from typing import Dict, Any, List
from config.settings import settings


class GCPConfig:
    """Google Cloud Platform configuration for Speech-to-Text API."""
    
    # Speech-to-Text API Configuration
    SPEECH_CONFIG = {
        "encoding": "LINEAR16",  # Default for WAV files
        "sample_rate_hertz": 16000,  # Will be auto-detected from audio
        "language_code": settings.default_language_code,
        "enable_automatic_punctuation": True,
        "enable_word_time_offsets": True,
        "enable_word_confidence": True,
        "model": "latest_long",  # Best for longer audio files
    }
    
    # Audio format configurations
    FORMAT_CONFIGS = {
        "wav": {
            "encoding": "LINEAR16",
            "sample_rate_hertz": None,  # Auto-detect
        },
        "mp3": {
            "encoding": "MP3",
            "sample_rate_hertz": None,  # Auto-detect
        },
        "m4a": {
            "encoding": "MP3",  # M4A often uses AAC, but MP3 encoding works for most cases
            "sample_rate_hertz": None,
        },
        "flac": {
            "encoding": "FLAC",
            "sample_rate_hertz": None,
        },
        "ogg": {
            "encoding": "OGG_OPUS",
            "sample_rate_hertz": 48000,  # Common for OGG Opus
        },
        "webm": {
            "encoding": "WEBM_OPUS",
            "sample_rate_hertz": 48000,  # Common for WebM Opus
        },
    }
    
    # TODO: Add Supported language codes
    # TODO: Add class methods for configuration handling
    # TODO: Add file size and duration limits
