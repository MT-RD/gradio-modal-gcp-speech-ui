"""
Gradio interface components for the Speech-to-Text application.
"""

import gradio as gr
import os
from typing import Optional, Tuple
from datetime import datetime

# Supported audio file formats for validation
SUPPORTED_AUDIO_FORMATS = {
    '.wav', '.mp3', '.m4a', '.ogg', '.flac', '.aac', '.wma'
}

def validate_audio_file(file_path: str) -> tuple[bool, str]:
    """
    Validate uploaded audio file format and existence.
    
    Args:
        file_path: Path to the uploaded audio file
        
    Returns:
        Tuple of (is_valid, message)
    """
    if not file_path:
        return False, "❌ No file provided."
    
    if not os.path.exists(file_path):
        return False, "❌ File does not exist."
    
    # Get file extension
    _, ext = os.path.splitext(file_path.lower())
    
    if ext not in SUPPORTED_AUDIO_FORMATS:
        supported_list = ", ".join(sorted(SUPPORTED_AUDIO_FORMATS))
        return False, f"❌ Unsupported file format '{ext}'. Supported formats: {supported_list}"
    
    # Get file size
    file_size = os.path.getsize(file_path)
    file_size_mb = file_size / (1024 * 1024)
    
    # Check file size (limit to 100MB for reasonable processing)
    if file_size_mb > 100:
        return False, f"❌ File too large ({file_size_mb:.1f}MB). Maximum size: 100MB."
    
    return True, f"✅ Valid audio file ({ext.upper()}, {file_size_mb:.1f}MB)"

def get_audio_info(file_path: str) -> dict:
    """
    Get detailed information about the audio file.
    
    Args:
        file_path: Path to the audio file
        
    Returns:
        Dictionary with audio file information
    """
    info = {
        'filename': os.path.basename(file_path),
        'size_mb': os.path.getsize(file_path) / (1024 * 1024),
        'format': os.path.splitext(file_path)[1].upper(),
        'upload_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    # Try to get duration using basic file info (simplified for now)
    # In a real implementation, you'd use librosa or similar
    info['duration'] = "Duration detection available in Step 3"
    
    return info

def format_audio_info(info: dict) -> str:
    """Format audio file information for display."""
    return f"""📁 **File Information:**
• **Name:** {info['filename']}
• **Format:** {info['format']}
• **Size:** {info['size_mb']:.1f} MB
• **Uploaded:** {info['upload_time']}
• **Duration:** {info['duration']}"""

def process_speech_with_validation(audio_input) -> str:
    """
    Enhanced speech processing function with file validation.
    This will be replaced with actual GCP Speech-to-Text integration.
    """
    if audio_input is None:
        return """🎤 **Welcome to Speech-to-Text!**

Please upload an audio file or use the microphone to record audio.

**📋 Instructions:**
1. Click "Upload" to select an audio file from your device
2. Or click "Record" to capture audio directly  
3. Supported formats: WAV, MP3, M4A, OGG, FLAC, AAC, WMA
4. Maximum file size: 100MB

**🎯 What happens next:**
• File validation and format checking
• Audio information extraction  
• Mock transcription (Step 3 will add real GCP integration)"""
    
    # Validate the uploaded file
    is_valid, validation_message = validate_audio_file(audio_input)
    
    if not is_valid:
        return f"""❌ **Validation Failed**

{validation_message}

**🔧 Troubleshooting:**
• Check that your file is a supported audio format
• Ensure file size is under 100MB
• Try converting to WAV or MP3 if issues persist

**✅ Supported formats:** {', '.join(sorted(SUPPORTED_AUDIO_FORMATS))}"""
    
    # Get detailed audio file information
    audio_info = get_audio_info(audio_input)
    info_display = format_audio_info(audio_info)
    
    # Mock transcription response with enhanced file info
    return f"""✅ **File Validation Successful!**

{info_display}

{validation_message}

🎙️ **Mock Transcription:**
"This is a placeholder transcription result. The audio file '{audio_info['filename']}' has been successfully validated and analyzed. File size: {audio_info['size_mb']:.1f}MB. The system is ready for processing with Google Cloud Speech-to-Text API."

🔧 **Processing Status:** 
• ✅ File uploaded and validated
• ✅ Audio information extracted  
• ✅ Ready for speech recognition (Step 3)
• 🎵 Audio preview: Available in browser player above

� **Next Steps:** Integration with Google Cloud Speech-to-Text API will provide actual transcription results."""

def create_speech_interface() -> gr.Interface:
    """
    Create and configure the main Gradio interface for speech-to-text processing.
    
    Returns:
        gr.Interface: Configured Gradio interface
    """
    
    # Create the interface with enhanced audio component
    interface = gr.Interface(
        fn=process_speech_with_validation,
        inputs=gr.Audio(
            label="🎵 Audio Input",
            type="filepath"
        ),
        outputs=gr.Textbox(
            label="📝 Transcription Results",
            lines=12,
            placeholder="Upload an audio file to see transcription results and file information..."
        ),
        title="🎙️ Speech-to-Text UI with Enhanced Audio Preview",
        description=f"""
        Upload an audio file or record directly to get started with speech transcription.
        
        **✅ Supported formats:** {', '.join(sorted(SUPPORTED_AUDIO_FORMATS))}  
        **📊 Maximum file size:** 100MB  
        **🎵 Audio preview:** Built-in player for uploaded files  
        **📋 File info:** Detailed information display  
        
        The interface will validate your file and provide detailed feedback before processing.
        """,
        examples=None,  # We'll add example files later
        allow_flagging="never"
    )
    
    return interface
