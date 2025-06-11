#!/usr/bin/env python3
"""
Simple audio testing utility for development.
Tests the current AudioProcessor implementation.
"""

import sys
import os
from pathlib import Path
import tempfile
import json

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

def test_audio_processor():
    """Quick test of AudioProcessor functionality."""
    try:
        from gcp_client.audio_processor import AudioProcessor
        from gcp_client.exceptions import AudioProcessingError, UnsupportedFormatError
        
        print("🎵 Testing AudioProcessor...")
        processor = AudioProcessor()
        
        # Test constants
        print(f"✅ Supported formats: {list(processor.SUPPORTED_FORMATS.keys())}")
        print(f"✅ Sample rate range: {processor.MIN_SAMPLE_RATE}-{processor.MAX_SAMPLE_RATE} Hz")
        print(f"✅ Min duration: {processor.MIN_DURATION_SECONDS}s")
        
        # Test with a simple generated audio file
        try:
            import numpy as np
            import soundfile as sf
            
            # Generate test audio
            sample_rate = 44100
            duration = 1.0
            t = np.linspace(0, duration, int(sample_rate * duration))
            audio_data = 0.3 * np.sin(2 * np.pi * 440 * t)
            
            with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as tmp_file:
                sf.write(tmp_file.name, audio_data, sample_rate)
                
                # Test analysis
                info = processor.get_audio_info(tmp_file.name)
                print(f"✅ Analysis: {info['duration_seconds']}s, {info['sample_rate']}Hz, {info['channels']} channels")
                
                # Test validation
                is_valid, message = processor.validate_audio_file(tmp_file.name)
                print(f"✅ Validation: {is_valid} - {message}")
                
                os.unlink(tmp_file.name)
                
        except ImportError:
            print("⚠️  numpy/soundfile not available for audio generation test")
        
        print("🎉 AudioProcessor test completed successfully!")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Test error: {e}")
        return False

if __name__ == "__main__":
    success = test_audio_processor()
    sys.exit(0 if success else 1)
