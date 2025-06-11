"""
Google Cloud Speech-to-Text client module.

This module provides the interface for interacting with Google Cloud Speech-to-Text API.
"""

from .speech_client import SpeechToTextClient
from .audio_processor import AudioProcessor
from .exceptions import (
    GCPSpeechError,
    AudioProcessingError,
    AuthenticationError,
    UnsupportedFormatError
)

__all__ = [
    'SpeechToTextClient',
    'AudioProcessor', 
    'GCPSpeechError',
    'AudioProcessingError',
    'AuthenticationError',
    'UnsupportedFormatError'
]
