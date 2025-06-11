"""
Google Cloud Speech-to-Text client implementation.

This module provides the main interface for interacting with the
Google Cloud Speech-to-Text API.
"""

import os
import json
import logging
from typing import Dict, Any, Optional
from pathlib import Path

from .audio_processor import AudioProcessor
from .exceptions import GCPSpeechError, AuthenticationError

logger = logging.getLogger(__name__)


class SpeechToTextClient:
    """Main client for Google Cloud Speech-to-Text operations."""
    
    def __init__(self, credentials_path: Optional[str] = None, project_id: Optional[str] = None):
        """
        Initialize the Speech-to-Text client.
        
        Args:
            credentials_path: Path to GCP service account JSON file
            project_id: Google Cloud project ID
        """
        self.credentials_path = credentials_path
        self.project_id = project_id
        self.audio_processor = AudioProcessor()
        
        # Client will be initialized when first used
        self._client = None
        self._is_authenticated = False
        self._credentials_validated = False
        
        logger.info("SpeechToTextClient initialized with authentication support")
    
    def _validate_credentials_file(self, credentials_path: str) -> Dict[str, Any]:
        """
        Validate the GCP service account credentials file.
        
        Args:
            credentials_path: Path to the credentials JSON file
            
        Returns:
            Dictionary containing parsed credentials
            
        Raises:
            AuthenticationError: If credentials file is invalid
        """
        try:
            if not os.path.exists(credentials_path):
                raise AuthenticationError(f"Credentials file not found: {credentials_path}")
            
            # Validate file is readable and valid JSON
            with open(credentials_path, 'r') as f:
                credentials = json.load(f)
            
            # Check for required fields in service account JSON
            required_fields = ['type', 'project_id', 'private_key_id', 'private_key', 'client_email']
            missing_fields = [field for field in required_fields if field not in credentials]
            
            if missing_fields:
                raise AuthenticationError(f"Invalid credentials file. Missing fields: {', '.join(missing_fields)}")
            
            if credentials.get('type') != 'service_account':
                raise AuthenticationError("Credentials file must be a service account key")
            
            logger.info(f"Credentials file validated: {credentials.get('client_email')}")
            return credentials
            
        except json.JSONDecodeError as e:
            raise AuthenticationError(f"Credentials file is not valid JSON: {e}")
        except Exception as e:
            raise AuthenticationError(f"Failed to validate credentials file: {e}")
    
    def _authenticate(self) -> bool:
        """
        Authenticate with Google Cloud using service account credentials.
        
        Returns:
            True if authentication successful
            
        Raises:
            AuthenticationError: If authentication fails
        """
        try:
            # Get credentials path from instance variable or environment
            credentials_path = self.credentials_path or os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
            
            if not credentials_path:
                raise AuthenticationError(
                    "No credentials found. Set GOOGLE_APPLICATION_CREDENTIALS environment variable "
                    "or provide credentials_path when initializing the client"
                )
            
            # Validate credentials file
            credentials = self._validate_credentials_file(credentials_path)
            
            # Set environment variable for GCP SDK
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path
            
            # Extract project ID if not provided
            if not self.project_id:
                self.project_id = credentials.get('project_id')
                logger.info(f"Using project ID from credentials: {self.project_id}")
            
            self._is_authenticated = True
            self._credentials_validated = True
            
            logger.info(f"Authentication successful for project: {self.project_id}")
            return True
            
        except AuthenticationError:
            raise
        except Exception as e:
            logger.error(f"Authentication failed: {e}")
            raise AuthenticationError(f"Authentication failed: {e}")
    
    def _get_client(self):
        """
        Get or create the GCP Speech client.
        
        Returns:
            Google Cloud Speech client (placeholder for now)
        """
        if not self._is_authenticated:
            self._authenticate()
        
        if self._client is None:
            # For now, return a placeholder
            # In the next logical commit, we'll initialize: speech.SpeechClient()
            self._client = "AUTHENTICATED_GCP_CLIENT_PLACEHOLDER"
            logger.info("GCP Speech client created with authentication")
        
        return self._client
    
    def is_available(self) -> bool:
        """
        Check if the GCP Speech-to-Text service is available.
        
        Returns:
            True if service is available and authenticated
        """
        try:
            # Try to authenticate and get client
            self._get_client()
            logger.info("GCP Speech-to-Text service is available")
            return True
        except AuthenticationError as e:
            logger.warning(f"GCP Speech service not available - authentication failed: {e}")
            return False
        except Exception as e:
            logger.warning(f"GCP Speech service not available: {e}")
            return False
    
    def get_authentication_status(self) -> Dict[str, Any]:
        """
        Get detailed authentication status information.
        
        Returns:
            Dictionary containing authentication details
        """
        return {
            'is_authenticated': self._is_authenticated,
            'credentials_validated': self._credentials_validated,
            'credentials_path': self.credentials_path or os.getenv('GOOGLE_APPLICATION_CREDENTIALS'),
            'project_id': self.project_id,
            'client_initialized': self._client is not None
        }
    
    def transcribe_audio(self, file_path: str, language_code: str = "en-US") -> Dict[str, Any]:
        """
        Transcribe an audio file using Google Cloud Speech-to-Text.
        
        Args:
            file_path: Path to the audio file
            language_code: Language code for recognition (e.g., 'en-US')
            
        Returns:
            Dictionary containing transcription results and metadata
        """
        # Validate audio file
        is_valid, validation_message = self.audio_processor.validate_audio_file(file_path)
        if not is_valid:
            raise GCPSpeechError(f"Audio validation failed: {validation_message}")
        
        # Authenticate and get client
        client = self._get_client()
        
        # Get audio information
        audio_info = self.audio_processor.get_audio_info(file_path)
        
        # Return skeleton mock result
        return {
            "transcript": f"[SKELETON MOCK] Basic transcription for {audio_info['filename']}",
            "confidence": 0.85,
            "language_code": language_code,
            "audio_info": audio_info,
            "processing_method": "skeleton",
        }
