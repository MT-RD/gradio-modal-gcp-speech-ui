"""
Audio processing utilities for Google Cloud Speech-to-Text.

This module provides functions for preprocessing audio files before
sending them to the Google Cloud Speech-to-Text API.
"""

import os
import logging
from typing import Tuple, Optional, Dict, Any
from pathlib import Path

import librosa
import numpy as np

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
    
    # Audio validation constants
    MIN_DURATION_SECONDS = 0.5      # Minimum audio length
    MAX_DURATION_SYNC = 60          # Max duration for sync processing (seconds)
    MAX_DURATION_ASYNC = 3600       # Max duration for async processing (seconds)
    
    # Quality thresholds
    MIN_SAMPLE_RATE = 8000          # Minimum sample rate for GCP
    MAX_SAMPLE_RATE = 48000         # Maximum sample rate for GCP
    SILENCE_THRESHOLD = 0.01        # RMS threshold for silence detection
    MIN_SPEECH_RATIO = 0.1          # Minimum ratio of non-silent audio
    
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

    # --- Enhanced Audio Analysis Methods (Skeleton) ---
    
    def _analyze_audio_content(self, file_path: str) -> Dict[str, Any]:
        """
        Extract detailed audio characteristics using librosa.
        
        Args:
            file_path: Path to the audio file
            
        Returns:
            Dictionary containing detailed audio analysis
        """
        try:
            # Check if file exists and get basic info
            if not os.path.exists(file_path):
                raise AudioProcessingError(f"Audio file not found: {file_path}")
            
            file_extension = Path(file_path).suffix.lower()
            file_size = os.path.getsize(file_path)
            
            # Validate file format support
            if file_extension not in self.SUPPORTED_FORMATS:
                supported_formats = ', '.join(self.SUPPORTED_FORMATS.keys())
                raise UnsupportedFormatError(
                    f"Unsupported format {file_extension}. Supported: {supported_formats}"
                )
            
            # Load audio file with graceful fallback handling
            load_method = 'unknown'
            try:
                # Primary method: preserve original format
                audio_data, sample_rate = librosa.load(file_path, sr=None, mono=False)
                load_method = 'librosa_original'
            except Exception as primary_error:
                logger.warning(f"Primary loading failed for {file_path}: {primary_error}")
                try:
                    # Fallback: force mono conversion
                    audio_data, sample_rate = librosa.load(file_path, sr=None, mono=True)
                    load_method = 'librosa_mono_fallback'
                    logger.info(f"Successfully loaded {file_path} with mono conversion")
                except Exception as mono_error:
                    logger.warning(f"Mono fallback failed for {file_path}: {mono_error}")
                    try:
                        # Last resort: default sample rate
                        audio_data, sample_rate = librosa.load(file_path, sr=22050, mono=True)
                        load_method = 'librosa_default_sr'
                        logger.info(f"Successfully loaded {file_path} with default settings")
                    except Exception as final_error:
                        raise AudioProcessingError(
                            f"All loading methods failed for {file_path}. "
                            f"Final error: {final_error}"
                        )
            audio_data, sample_rate = librosa.load(file_path, sr=None, mono=False)
            
            # Extract basic audio metrics
            if audio_data.ndim == 1:
                # Mono audio
                channels = 1
                total_samples = len(audio_data)
                duration_seconds = total_samples / sample_rate
            else:
                # Multi-channel audio
                channels = audio_data.shape[0]
                total_samples = audio_data.shape[1]
                duration_seconds = total_samples / sample_rate
            
            # Calculate basic audio statistics
            if audio_data.ndim == 1:
                rms_energy = float(librosa.feature.rms(y=audio_data)[0].mean())
                max_amplitude = float(audio_data.max())
                min_amplitude = float(audio_data.min())
            else:
                # For multi-channel, average across channels
                rms_energy = float(librosa.feature.rms(y=audio_data.mean(axis=0))[0].mean())
                max_amplitude = float(audio_data.max())
                min_amplitude = float(audio_data.min())
            
            # Return comprehensive audio information
            return {
                'audio_loaded': True,
                'sample_rate': int(sample_rate),
                'channels': channels,
                'duration_seconds': round(duration_seconds, 3),
                'total_samples': total_samples,
                'rms_energy': round(rms_energy, 6),
                'max_amplitude': round(max_amplitude, 6),
                'min_amplitude': round(min_amplitude, 6),
                'audio_shape': audio_data.shape,
                'file_path': file_path,
                'file_extension': file_extension,
                'file_size_bytes': file_size,
                'gcp_encoding': self.SUPPORTED_FORMATS.get(file_extension),
                'load_method': load_method
            }
            
        except Exception as e:
            logger.error(f"Failed to load audio file {file_path}: {e}")
            raise AudioProcessingError(f"Could not analyze audio content: {e}")
        
    
    def _validate_audio_quality(self, audio_data, sample_rate: int) -> Tuple[bool, str]:
        """
        Validate audio quality metrics against GCP requirements.
        
        Args:
            audio_data: Audio time series data
            sample_rate: Sample rate in Hz
            
        Returns:
            Tuple of (is_valid, validation_message)
        """
        # TODO: Implement quality validation
        # - Check sample rate range
        # - Validate audio duration
        # - Assess signal quality (RMS, SNR)
        # - Check for clipping/distortion
        raise NotImplementedError("Audio quality validation not yet implemented")
    
    def _check_for_silence(self, audio_data, sample_rate: int) -> Dict[str, Any]:
        """
        Detect silence and analyze speech content.
        
        Args:
            audio_data: Audio time series data
            sample_rate: Sample rate in Hz
            
        Returns:
            Dictionary containing silence analysis results
        """
        # TODO: Implement silence detection
        # - Calculate RMS energy levels
        # - Detect silent segments
        # - Calculate speech activity ratio
        # - Identify potential recording issues
        raise NotImplementedError("Silence detection not yet implemented")
    
    def _suggest_audio_fixes(self, issues: list) -> str:
        """
        Provide actionable suggestions for audio problems.
        
        Args:
            issues: List of identified audio issues
            
        Returns:
            Human-readable suggestions for fixing issues
        """
        # TODO: Implement fix suggestions
        # - Analyze issue types
        # - Provide specific recommendations
        # - Suggest optimal recording settings
        raise NotImplementedError("Audio fix suggestions not yet implemented")
    
    def preprocess_for_gcp(self, file_path: str) -> Dict[str, Any]:
        """
        Prepare audio file for optimal GCP Speech-to-Text processing.
        
        Args:
            file_path: Path to the audio file
            
        Returns:
            Dictionary containing preprocessing recommendations
        """
        # TODO: Implement GCP preprocessing
        # - Analyze current audio format
        # - Recommend optimal encoding
        # - Suggest quality improvements
        # - Provide conversion parameters
        raise NotImplementedError("GCP preprocessing not yet implemented")
