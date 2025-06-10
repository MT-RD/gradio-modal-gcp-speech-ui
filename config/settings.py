"""
Application Configuration Module

This module contains the main configuration settings for the application.
"""

import os
from typing import List
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # Google Cloud Configuration
    gcp_project_id: str = Field(..., env="GCP_PROJECT_ID")
    google_application_credentials: str = Field(..., env="GOOGLE_APPLICATION_CREDENTIALS")
    gcs_bucket_name: str = Field(default="", env="GCS_BUCKET_NAME")
    
    # Modal Configuration
    modal_token_id: str = Field(..., env="MODAL_TOKEN_ID")
    modal_token_secret: str = Field(..., env="MODAL_TOKEN_SECRET")
    modal_app_name: str = Field(default="speech-to-text-app", env="MODAL_APP_NAME")
    
    # Application Configuration
    max_file_size_mb: int = Field(default=25, env="MAX_FILE_SIZE_MB")
    supported_formats: str = Field(default="wav,mp3,m4a,flac,ogg,webm", env="SUPPORTED_FORMATS")
    default_language_code: str = Field(default="en-US", env="DEFAULT_LANGUAGE_CODE")
    debug_mode: bool = Field(default=False, env="DEBUG_MODE")
    
    # Gradio Configuration
    gradio_share: bool = Field(default=False, env="GRADIO_SHARE")
    gradio_server_name: str = Field(default="127.0.0.1", env="GRADIO_SERVER_NAME")
    gradio_server_port: int = Field(default=7860, env="GRADIO_SERVER_PORT")
    gradio_theme: str = Field(default="default", env="GRADIO_THEME")
    
    # Development Configuration
    log_level: str = Field(default="INFO", env="LOG_LEVEL")
    enable_monitoring: bool = Field(default=False, env="ENABLE_MONITORING")
    test_mode: bool = Field(default=False, env="TEST_MODE")
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
    
    @property
    def supported_formats_list(self) -> List[str]:
        """Get supported formats as a list."""
        return [fmt.strip().lower() for fmt in self.supported_formats.split(",")]
    
    @property
    def max_file_size_bytes(self) -> int:
        """Get maximum file size in bytes."""
        return self.max_file_size_mb * 1024 * 1024


# Global settings instance
try:
    settings = Settings()
except Exception as e:
    # For development, create a dummy settings instance
    print(f"Warning: Could not load settings from environment: {e}")
    print("Using default settings for development. Make sure to create .env file for production.")
    
    class DummySettings:
        gcp_project_id = "dummy-project"
        google_application_credentials = "dummy-credentials.json"
        gcs_bucket_name = ""
        modal_token_id = "dummy-token-id"
        modal_token_secret = "dummy-token-secret"
        modal_app_name = "speech-to-text-app"
        max_file_size_mb = 25
        supported_formats = "wav,mp3,m4a,flac,ogg,webm"
        default_language_code = "en-US"
        debug_mode = True
        gradio_share = False
        gradio_server_name = "127.0.0.1"
        gradio_server_port = 7860
        gradio_theme = "default"
        log_level = "INFO"
        enable_monitoring = False
        test_mode = True
        
        @property
        def supported_formats_list(self):
            return [fmt.strip().lower() for fmt in self.supported_formats.split(",")]
        
        @property
        def max_file_size_bytes(self):
            return self.max_file_size_mb * 1024 * 1024
    
    settings = DummySettings()
