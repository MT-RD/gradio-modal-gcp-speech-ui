# Sample Audio Files

This directory contains sample audio files for testing the speech-to-text functionality.

## Files

*Note: Audio files are not included in the repository due to size constraints. You can add your own sample files here for testing.*

### Recommended Sample Files:
- `sample_short.wav` - Short audio clip (< 1 minute) for quick testing
- `sample_medium.wav` - Medium audio clip (1-5 minutes) for standard testing
- `sample_long.wav` - Longer audio clip (> 5 minutes) for async processing testing

### File Naming Convention:
- Use descriptive names that indicate the content or duration
- Include the speaker type (e.g., `male_voice_`, `female_voice_`, `multiple_speakers_`)
- Include the expected language (e.g., `_en_us`, `_es_es`)

### Example Filenames:
- `male_voice_tech_talk_en_us.wav`
- `female_voice_interview_2min_en_gb.wav`
- `multiple_speakers_meeting_10min_en_us.wav`

## Adding Your Own Samples

1. Convert your audio files to supported formats (WAV, MP3, M4A, FLAC, etc.)
2. Place them in this directory
3. Update this README with descriptions of your sample files
4. Use them to test the application

## Audio Requirements

- **Formats**: WAV (recommended), MP3, M4A, FLAC, OGG, WebM
- **Quality**: 16 kHz sample rate or higher for best results
- **Size**: Keep under 25 MB for web upload testing
- **Duration**: Mix of short (< 1 min) and longer (1-10 min) files for comprehensive testing

## Testing Different Scenarios

Create samples that test:
- Clear speech vs. noisy environments
- Single speaker vs. multiple speakers
- Different accents and languages
- Technical terminology vs. casual conversation
- Phone call quality vs. studio recording quality
