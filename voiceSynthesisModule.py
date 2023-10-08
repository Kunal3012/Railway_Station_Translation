import os
import time
from azure.cognitiveservices.speech import AudioDataStream, AudioOutputConfig, SpeechConfig, SpeechSynthesizer
from gtts import gTTS

def synthesize_speech_azure(text, language):
    # Set up Azure Text-to-Speech Service
    speech_config = SpeechConfig(subscription="<YourAzureSubscriptionKey>", region="<YourAzureRegion>")
    synthesizer = SpeechSynthesizer(speech_config=speech_config)

    # Set the voice and language for Azure TTS
    speech_config.speech_synthesis_voice_name = f"ta-IN-{language.capitalize()}"  # Replace with the desired Indian language

    # Synthesize speech with Azure Text-to-Speech
    result = synthesizer.speak_text_async(text).get()
    
    # Save the audio to a file
    audio_filename = "azure_audio.wav"
    audio_stream = AudioDataStream(result)
    audio_stream.save_to_wav_file(audio_filename)

    return audio_filename

def synthesize_speech_google_translate(text, language):
    # Use gTTS library for Google Translate TTS
    tts = gTTS(text=text, lang=language)

    # Save the audio to a file
    audio_filename = "google_audio.mp3"
    tts.save(audio_filename)

    return audio_filename

def multilingual_voice_synthesis(input_text, target_language, use_google_translate=False):
    if use_google_translate:
        audio_filename = synthesize_speech_google_translate(input_text, target_language)
    else:
        audio_filename = synthesize_speech_azure(input_text, target_language)

    # Construct the output in JSON format with audio metadata
    output_json = {
        "original_text": input_text,
        "target_language": target_language,
        "audio_file_path": audio_filename
    }

    return output_json

# Example usage
if __name__ == "__main__":
    input_text = "Your translated text to be synthesized into speech"
    target_language = "ta-IN"  # Replace with the desired Indian language code
    use_google_translate = False  # Set to True if you want to use Google Translate for offline synthesis

    synthesized_audio = multilingual_voice_synthesis(input_text, target_language, use_google_translate)
    print("Synthesized Audio Metadata: ", synthesized_audio)
