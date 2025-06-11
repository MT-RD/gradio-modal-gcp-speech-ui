"""
Custom exceptions for Google Cloud Speech-to-Text client.

This module defines custom exception classes for better error handling
in the GCP Speech-to-Text integration.
"""


class GCPSpeechError(Exception):
    """Base exception for all GCP Speech-to-Text related errors."""
    
    def __init__(self, message: str, error_code: str = None):
        super().__init__(message)
        self.message = message
        self.error_code = error_code

    def __str__(self) -> str:
        if self.error_code:
            return f"[{self.error_code}] {self.message}"
        return self.message


class AuthenticationError(GCPSpeechError):
    """Raised when authentication with Google Cloud fails."""
    
    def __init__(self, message: str = "Failed to authenticate with Google Cloud"):
        super().__init__(message, "AUTH_ERROR")


class AudioProcessingError(GCPSpeechError):
    """Raised when audio processing fails."""
    
    def __init__(self, message: str, original_error: Exception = None):
        super().__init__(message, "AUDIO_ERROR")
        self.original_error = original_error


class UnsupportedFormatError(GCPSpeechError):
    """Raised when an unsupported audio format is encountered."""
    
    def __init__(self, format_name: str):
        message = f"Unsupported audio format: {format_name}"
        super().__init__(message, "FORMAT_ERROR")
        self.format_name = format_name


class QuotaExceededError(GCPSpeechError):
    """Raised when GCP API quota is exceeded."""
    
    def __init__(self, message: str = "Google Cloud API quota exceeded"):
        super().__init__(message, "QUOTA_ERROR")

class TranscriptionError(GCPSpeechError):
    """Raised when transcription fails."""
    
    pass
