"""
Audio processing utilities for Google Cloud Speech-to-Text.

This module provides functions for preprocessing audio files before
sending them to the Google Cloud Speech-to-Text API.
"""

import os
import logging
from typing import Tuple, Optional, Dict, Any
from pathlib import Path

from .exceptions import AudioProcessingError, UnsupportedFormatError

logger = logging.getLogger(__name__)


class AudioProcessor:
    """Handles audio file processing and validation for GCP Speech-to-Text."""
    
    # Supported audio formats for GCP Speech-to-Text API
    SUPPORTED_FORMATS = {
        '.wav': 'LINEAR16',      # Uncompressed WAV (recommended)
        '.flac': 'FLAC',         # Free Lossless Audio Codec
        '.mp3': 'MP3',           # MPEG Audio Layer III
        '.m4a': 'MP3',           # Will be converted to MP3
        '.ogg': 'OGG_OPUS',      # Ogg container with Opus codec
        '.aac': 'MP3',           # Will be converted to MP3
        '.wma': 'MP3'            # Will be converted to MP3
    }
    
    # GCP Speech-to-Text file size limits
    MAX_FILE_SIZE_SYNC = 10 * 1024 * 1024      # 10MB for synchronous requests
    MAX_FILE_SIZE_ASYNC = 1000 * 1024 * 1024   # 1GB for asynchronous requests
    
    # Audio quality recommendations
    RECOMMENDED_SAMPLE_RATES = [8000, 16000, 22050, 44100, 48000]  # Hz
    RECOMMENDED_CHANNELS = [1, 2]  # Mono or Stereo
    
    def __init__(self):
        """Initialize the AudioProcessor."""
        logger.info("AudioProcessor initialized with GCP format support")
    
    def get_audio_info(self, file_path: str) -> Dict[str, Any]:
        """
        Get detailed information about an audio file.
        
        Args:
            file_path: Path to the audio file
            
        Returns:
            Dictionary containing audio file information
        """
        if not os.path.exists(file_path):
            raise AudioProcessingError(f"Audio file not found: {file_path}")
        
        file_size = os.path.getsize(file_path)
        file_extension = Path(file_path).suffix.lower()
        
        return {
            'filename': os.path.basename(file_path),
            'size_bytes': file_size,
            'size_mb': file_size / (1024 * 1024),
            'format': file_extension,
            'encoding': self.SUPPORTED_FORMATS.get(file_extension),
            'is_supported': file_extension in self.SUPPORTED_FORMATS,
            'requires_conversion': file_extension in ['.m4a', '.aac', '.wma'],
            'max_size_sync': file_size <= self.MAX_FILE_SIZE_SYNC,
            'max_size_async': file_size <= self.MAX_FILE_SIZE_ASYNC,
            # Audio details will be added when librosa is integrated
            'duration_seconds': None,
            'sample_rate': None,
            'channels': None,
        }
    
    def validate_audio_file(self, file_path: str) -> Tuple[bool, str]:
        """
        Validate an audio file for GCP Speech-to-Text processing.
        
        Args:
            file_path: Path to the audio file to validate
            
        Returns:
            Tuple of (is_valid, validation_message)
        """
        try:
            info = self.get_audio_info(file_path)
            
            # Check if format is supported
            if not info['is_supported']:
                supported_formats = ', '.join(self.SUPPORTED_FORMATS.keys())
                return False, f"Unsupported format {info['format']}. Supported: {supported_formats}"
            
            # Check file size against GCP limits
            if not info['max_size_async']:
                return False, f"File too large ({info['size_mb']:.1f}MB). Maximum: 1000MB for async processing"
            
            # Determine processing method
            processing_method = "synchronous" if info['max_size_sync'] else "asynchronous"
            message = f"Valid {info['format']} file ({info['size_mb']:.1f}MB) - {processing_method} processing"
            
            # Add conversion note if needed
            if info['requires_conversion']:
                message += " (will be converted to MP3)"
                
            return True, message
            
        except Exception as e:
            return False, f"Validation failed: {e}"
