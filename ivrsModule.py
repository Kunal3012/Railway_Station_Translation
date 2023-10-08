import os
import azure.cognitiveservices.speech as speechsdk

def speech_recognition(audio_file):
    speech_config = speechsdk.SpeechConfig(subscription="YOUR_AZURE_SUBSCRIPTION_KEY", region="YOUR_REGION")
    audio_config = speechsdk.AudioConfig(filename=audio_file)

    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    result = speech_recognizer.recognize_once()
    return result.reason, result.text if result.reason == speechsdk.ResultReason.RecognizedSpeech else None

def text_to_speech(text):
    speech_config = speechsdk.SpeechConfig(subscription="YOUR_AZURE_SUBSCRIPTION_KEY", region="YOUR_REGION")

    audio_config = speechsdk.AudioOutputConfig(filename="output.wav")

    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    synthesizer.speak_text(text)

if __name__ == "__main__":
    while True:
        print("IVR System")
        print("1. Record and Recognize")
        print("2. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            input("Press Enter to start recording...")
            os.system("arecord -d 5 -r 16000 -f S16_LE input.wav")  # Adjust recording settings as needed
            print("Recording complete.")
            reason, recognized_text = speech_recognition("input.wav")
            if recognized_text:
                print(f"Recognized: {recognized_text}")
                # Translate recognized_text if needed
                # Perform any logic based on recognized_text
                # Provide responses or actions accordingly
                text_to_speech("You said: " + recognized_text)
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")
