"""
Test Configuration and Fixtures

This module contains shared test configuration and fixtures for the test suite.
"""

import pytest
import tempfile
import os
from pathlib import Path
from unittest.mock import Mock


@pytest.fixture
def temp_audio_file():
    """Create a temporary audio file for testing."""
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        # Create a minimal WAV file header (44 bytes)
        f.write(b"RIFF")  # ChunkID
        f.write((36).to_bytes(4, "little"))  # ChunkSize
        f.write(b"WAVE")  # Format
        f.write(b"fmt ")  # Subchunk1ID
        f.write((16).to_bytes(4, "little"))  # Subchunk1Size
        f.write((1).to_bytes(2, "little"))  # AudioFormat (PCM)
        f.write((1).to_bytes(2, "little"))  # NumChannels (mono)
        f.write((16000).to_bytes(4, "little"))  # SampleRate
        f.write((32000).to_bytes(4, "little"))  # ByteRate
        f.write((2).to_bytes(2, "little"))  # BlockAlign
        f.write((16).to_bytes(2, "little"))  # BitsPerSample
        f.write(b"data")  # Subchunk2ID
        f.write((0).to_bytes(4, "little"))  # Subchunk2Size
        
        temp_path = f.name
    
    yield temp_path
    
    # Cleanup
    if os.path.exists(temp_path):
        os.unlink(temp_path)


@pytest.fixture
def mock_gcp_client():
    """Mock Google Cloud Speech client."""
    mock_client = Mock()
    mock_response = Mock()
    mock_response.results = [
        Mock(alternatives=[Mock(transcript="This is a test transcription.", confidence=0.95)])
    ]
    mock_client.recognize.return_value = mock_response
    return mock_client


@pytest.fixture
def sample_transcription_response():
    """Sample transcription response for testing."""
    return {
        "transcript": "This is a test transcription.",
        "confidence": 0.95,
        "words": [
            {"word": "This", "start_time": 0.0, "end_time": 0.2, "confidence": 0.98},
            {"word": "is", "start_time": 0.2, "end_time": 0.3, "confidence": 0.99},
            {"word": "a", "start_time": 0.3, "end_time": 0.4, "confidence": 0.97},
            {"word": "test", "start_time": 0.4, "end_time": 0.6, "confidence": 0.95},
            {"word": "transcription", "start_time": 0.6, "end_time": 1.2, "confidence": 0.92},
        ],
        "duration": 1.2,
        "language": "en-US"
    }
