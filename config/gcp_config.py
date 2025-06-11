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
    
    # TODO: Add Audio format configurations  
    # TODO: Add Supported language codes
    # TODO: Add class methods for configuration handling
    # TODO: Add file size and duration limits
