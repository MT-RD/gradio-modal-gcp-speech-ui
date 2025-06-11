"""
Custom exceptions for Google Cloud Speech-to-Text client.

This module defines custom exception classes for better error handling
in the GCP Speech-to-Text integration.
"""


class GCPSpeechError(Exception):
    """Base exception for all GCP Speech-to-Text related errors."""
    
    pass


class AuthenticationError(GCPSpeechError):
    """Raised when authentication with Google Cloud fails."""
    
    pass


class AudioProcessingError(GCPSpeechError):
    """Raised when audio processing fails."""
    pass


class UnsupportedFormatError(GCPSpeechError):
    """Raised when an unsupported audio format is encountered."""
    pass


class QuotaExceededError(GCPSpeechError):
    """Raised when GCP API quota is exceeded."""
    
    pass

class TranscriptionError(GCPSpeechError):
    """Raised when transcription fails."""
    
    pass
