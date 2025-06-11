#!/usr/bin/env python3
"""
Additional edge case tests for audio analysis.
"""

import sys
import os
from pathlib import Path
import json

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from gcp_client.audio_processor import AudioProcessor
from gcp_client.exceptions import AudioProcessingError, UnsupportedFormatError


def test_edge_cases():
    """Test edge cases and error scenarios."""
    
    print("🔍 Testing edge cases and error scenarios\n")
    
    processor = AudioProcessor()
    
    # Test 1: Empty file
    print("📋 Test 1: Empty audio file")
    try:
        empty_file = "/tmp/empty_audio.wav"
        with open(empty_file, 'wb') as f:
            f.write(b'')  # Empty file
        
        info = processor.get_audio_info(empty_file)
        print(f"✅ Empty file basic info - Size: {info['size_bytes']} bytes")
        print(f"✅ Analysis available: {info.get('audio_analysis_available', 'N/A')}")
        
        if not info.get('audio_analysis_available'):
            print(f"✅ Analysis error: {info.get('analysis_error', 'N/A')}")
        
        os.remove(empty_file)
        
    except Exception as e:
        print(f"✅ Handled empty file error: {e}")
    
    # Test 2: Very small audio file
    print("\n📋 Test 2: Very short audio (0.1 seconds)")
    try:
        import numpy as np
        import soundfile as sf
        
        # Generate very short audio (0.1 seconds)
        sample_rate = 44100
        duration = 0.1
        t = np.linspace(0, duration, int(sample_rate * duration))
        audio_data = 0.5 * np.sin(2 * np.pi * 440 * t)
        
        short_file = "/tmp/very_short.wav"
        sf.write(short_file, audio_data, sample_rate)
        
        info = processor.get_audio_info(short_file)
        print(f"✅ Short file duration: {info.get('duration_seconds', 'N/A')}s")
        print(f"✅ Below minimum duration ({processor.MIN_DURATION_SECONDS}s): {info.get('duration_seconds', 0) < processor.MIN_DURATION_SECONDS}")
        
        os.remove(short_file)
        
    except Exception as e:
        print(f"⚠️  Error testing short audio: {e}")
    
    # Test 3: Different sample rates
    print("\n📋 Test 3: Various sample rates")
    try:
        import numpy as np
        import soundfile as sf
        
        test_rates = [8000, 16000, 22050, 44100, 48000]
        
        for rate in test_rates:
            # Generate 0.5 second audio
            duration = 0.5
            t = np.linspace(0, duration, int(rate * duration))
            audio_data = 0.3 * np.sin(2 * np.pi * 440 * t)
            
            test_file = f"/tmp/test_{rate}hz.wav"
            sf.write(test_file, audio_data, rate)
            
            try:
                analysis = processor._analyze_audio_content(test_file)
                within_range = processor.MIN_SAMPLE_RATE <= analysis['sample_rate'] <= processor.MAX_SAMPLE_RATE
                print(f"✅ {rate} Hz: Duration {analysis['duration_seconds']}s, Within GCP range: {within_range}")
                
                os.remove(test_file)
                
            except Exception as e:
                print(f"❌ Failed at {rate} Hz: {e}")
                if os.path.exists(test_file):
                    os.remove(test_file)
                
    except ImportError:
        print("⚠️  Skipping sample rate tests (missing audio libraries)")
    except Exception as e:
        print(f"⚠️  Error in sample rate tests: {e}")
    
    # Test 4: Test all supported formats (mock)
    print("\n📋 Test 4: Format support validation")
    for ext, encoding in processor.SUPPORTED_FORMATS.items():
        print(f"✅ {ext} → {encoding} (Conversion needed: {ext in ['.m4a', '.aac', '.wma']})")
    
    print("\n🎉 Edge case testing completed!")


if __name__ == "__main__":
    test_edge_cases()
