"""
Gradio interface components for the Speech-to-Text application.
"""

import gradio as gr
import os
from typing import Optional

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

def process_speech_with_validation(audio_input) -> str:
    """
    Enhanced speech processing function with file validation.
    This will be replaced with actual GCP Speech-to-Text integration.
    """
    if audio_input is None:
        return "🎤 Please upload an audio file or record some audio to transcribe."
    
    # Validate the uploaded file
    is_valid, validation_message = validate_audio_file(audio_input)
    
    if not is_valid:
        return validation_message
    
    # Mock transcription response with file info
    filename = os.path.basename(audio_input)
    file_size = os.path.getsize(audio_input) / (1024 * 1024)
    
    return f"""✅ **File Validation Successful!**

📁 **File:** {filename}
📊 **Size:** {file_size:.1f}MB
{validation_message}

🎙️ **Mock Transcription:**
"This is a placeholder transcription result. The audio file has been successfully validated and is ready for processing with Google Cloud Speech-to-Text API. This demonstrates that the file upload, validation, and processing pipeline is working correctly."

🔧 **Status:** Ready for GCP Speech-to-Text integration (Step 3)"""

def create_speech_interface() -> gr.Interface:
    """
    Create and configure the main Gradio interface for speech-to-text processing.
    
    Returns:
        gr.Interface: Configured Gradio interface
    """
    
    # Create the interface using simple string specification for compatibility
    interface = gr.Interface(
        fn=process_speech_with_validation,
        inputs="audio",  # Simple string specification
        outputs="text",  # Simple string specification
        title="🎙️ Speech-to-Text UI with File Validation",
        description=f"""
        Upload an audio file or record directly to get started with speech transcription.
        
        **Supported formats:** {', '.join(sorted(SUPPORTED_AUDIO_FORMATS))}
        **Maximum file size:** 100MB
        """
    )
    
    return interface
