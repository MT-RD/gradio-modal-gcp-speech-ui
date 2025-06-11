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
    
    # Supported language codes
    SUPPORTED_LANGUAGES = {
        "en-US": "English (United States)",
        "en-GB": "English (United Kingdom)",
        "es-ES": "Spanish (Spain)",
        "es-US": "Spanish (United States)",
        "fr-FR": "French (France)",
        "de-DE": "German (Germany)",
        "it-IT": "Italian (Italy)",
        "pt-BR": "Portuguese (Brazil)",
        "ja-JP": "Japanese (Japan)",
        "ko-KR": "Korean (South Korea)",
        "zh-CN": "Chinese (Simplified)",
        "hi-IN": "Hindi (India)",
        "ar-SA": "Arabic (Saudi Arabia)",
        "ru-RU": "Russian (Russia)",
        "nl-NL": "Dutch (Netherlands)",
        "sv-SE": "Swedish (Sweden)",
        "da-DK": "Danish (Denmark)",
        "no-NO": "Norwegian (Norway)",
        "fi-FI": "Finnish (Finland)",
        "pl-PL": "Polish (Poland)",
    }
    
    @classmethod
    def get_config_for_format(cls, audio_format: str) -> Dict[str, Any]:
        """
        Get Speech-to-Text configuration for a specific audio format.
        
        Args:
            audio_format: The audio file format (e.g., 'wav', 'mp3')
            
        Returns:
            Dictionary containing the configuration for the format
        """
        base_config = cls.SPEECH_CONFIG.copy()
        format_config = cls.FORMAT_CONFIGS.get(audio_format.lower(), {})
        
        # Update base config with format-specific settings
        base_config.update(format_config)
        
        return base_config
    
    @classmethod
    def get_supported_languages(cls) -> List[Dict[str, str]]:
        """
        Get list of supported languages for the UI.
        
        Returns:
            List of dictionaries with 'code' and 'name' keys
        """
        return [
            {"code": code, "name": name}
            for code, name in cls.SUPPORTED_LANGUAGES.items()
        ]
    
    # File size and duration limits
    MAX_FILE_SIZE_BYTES = 10 * 1024 * 1024  # 10 MB for short audio
    MAX_AUDIO_DURATION_SECONDS = 480  # 8 minutes for synchronous recognition
    
    # For longer files, we'll need to use asynchronous recognition
    ASYNC_RECOGNITION_THRESHOLD_SECONDS = 60  # 1 minute
    ASYNC_MAX_DURATION_SECONDS = 28800  # 8 hours
