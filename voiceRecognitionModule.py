import os
import azure.cognitiveservices.speech as speechsdk

def recognize_speech(audio_file_path):
    # Set up Azure Cognitive Services Speech Configuration
    speech_config = speechsdk.SpeechConfig(subscription="<YourAzureSubscriptionKey>", region="<AzureRegion>")

    # Create a speech recognizer with a custom language configuration
    language_config = speechsdk.languageconfig.LanguageConfig("<YourIndianLanguageCode>")
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, language=language_config)

    # Open and read the audio file
    audio_input = speechsdk.AudioConfig(filename=audio_file_path)

    # Recognize speech from the audio input
    result = speech_recognizer.recognize_once(audio=audio_input)

    # Check for recognition result
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        return result.text
    elif result.reason == speechsdk.ResultReason.NoMatch:
        return "No speech could be recognized"
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details.reason
        if cancellation_details == speechsdk.CancellationReason.Error:
            return "Speech Recognition Error: {}".format(result.cancellation_details.reason_details)
        else:
            return "Speech Recognition Canceled: {}".format(cancellation_details)
    else:
        return "Unknown Error"

# Example usage
if __name__ == "__main__":
    audio_file_path = "<PathToYourAudioFile>"
    recognized_text = recognize_speech(audio_file_path)
    print("Recognized Text: ", recognized_text)
