#!/usr/bin/env python3
"""
Test script for audio analysis functionality.
Tests the AudioProcessor class with various scenarios.
"""

import sys
import os
from pathlib import Path
import json

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from gcp_client.audio_processor import AudioProcessor
from gcp_client.exceptions import AudioProcessingError, UnsupportedFormatError


def test_audio_processor():
    """Test the AudioProcessor functionality."""
    
    print("🎵 Testing AudioProcessor functionality\n")
    
    # Initialize processor
    processor = AudioProcessor()
    print("✅ AudioProcessor initialized successfully")
    
    # Test 1: Non-existent file
    print("\n📋 Test 1: Non-existent file")
    try:
        info = processor.get_audio_info("/path/to/nonexistent.wav")
        print("❌ Should have failed for non-existent file")
    except AudioProcessingError as e:
        print(f"✅ Correctly handled non-existent file: {e}")
    
    # Test 2: Unsupported format
    print("\n📋 Test 2: Unsupported format")
    try:
        # Create a dummy file with unsupported extension
        dummy_file = "/tmp/test_audio.xyz"
        with open(dummy_file, 'w') as f:
            f.write("dummy content")
        
        info = processor.get_audio_info(dummy_file)
        print(f"✅ Basic info for unsupported format: {info['is_supported']} = {info['is_supported']}")
        
        # Clean up
        os.remove(dummy_file)
        
    except Exception as e:
        print(f"⚠️  Unexpected error: {e}")
    
    # Test 3: Test constants and format support
    print("\n📋 Test 3: Format support and constants")
    print(f"✅ Supported formats: {list(processor.SUPPORTED_FORMATS.keys())}")
    print(f"✅ Max sync file size: {processor.MAX_FILE_SIZE_SYNC / (1024*1024):.1f} MB")
    print(f"✅ Max async file size: {processor.MAX_FILE_SIZE_ASYNC / (1024*1024):.1f} MB")
    print(f"✅ Sample rate range: {processor.MIN_SAMPLE_RATE} - {processor.MAX_SAMPLE_RATE} Hz")
    print(f"✅ Min duration: {processor.MIN_DURATION_SECONDS}s")
    print(f"✅ Silence threshold: {processor.SILENCE_THRESHOLD}")
    
    # Test 4: Generate a simple audio file for testing (if possible)
    print("\n📋 Test 4: Testing with generated audio")
    try:
        import numpy as np
        import librosa
        import soundfile as sf
        
        # Generate a simple 1-second sine wave at 440 Hz
        sample_rate = 44100
        duration = 1.0
        t = np.linspace(0, duration, int(sample_rate * duration))
        audio_data = 0.5 * np.sin(2 * np.pi * 440 * t)
        
        # Save as WAV file
        test_audio_file = "/tmp/test_sine_wave.wav"
        sf.write(test_audio_file, audio_data, sample_rate)
        
        print(f"✅ Generated test audio file: {test_audio_file}")
        
        # Test basic info
        info = processor.get_audio_info(test_audio_file)
        print(f"✅ File info - Size: {info['size_mb']:.3f} MB, Format: {info['format']}")
        print(f"✅ Supported: {info['is_supported']}, Analysis available: {info.get('audio_analysis_available', 'N/A')}")
        
        if info.get('audio_analysis_available'):
            print(f"✅ Duration: {info['duration_seconds']}s")
            print(f"✅ Sample rate: {info['sample_rate']} Hz")
            print(f"✅ Channels: {info['channels']}")
            print(f"✅ Load method: {info.get('load_method', 'N/A')}")
        
        # Test detailed analysis
        print("\n📋 Testing detailed audio analysis:")
        analysis = processor._analyze_audio_content(test_audio_file)
        print(f"✅ Detailed analysis:")
        for key, value in analysis.items():
            if key != 'audio_shape':  # Skip complex shape info
                print(f"   {key}: {value}")
        
        # Test validation
        print("\n📋 Testing audio validation:")
        is_valid, message = processor.validate_audio_file(test_audio_file)
        print(f"✅ Validation result: {is_valid}")
        print(f"✅ Validation message: {message}")
        
        # Clean up
        os.remove(test_audio_file)
        print("✅ Cleaned up test file")
        
    except ImportError as e:
        print(f"⚠️  Could not test with generated audio (missing dependencies): {e}")
    except Exception as e:
        print(f"❌ Error during audio generation test: {e}")
    
    print("\n🎉 Audio analysis testing completed!")


if __name__ == "__main__":
    test_audio_processor()
