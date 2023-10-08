from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

# Replace with your Azure Cognitive Services API keys
translation_key = "YOUR_TRANSLATION_API_KEY"
voice_synthesis_key = "YOUR_VOICE_SYNTHESIS_API_KEY"

# HTML form for user interaction
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["user_input"]
        selected_language = request.form["selected_language"]

        # Translate user input to the selected language
        translation_url = f"https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to={selected_language}"
        headers = {
            "Ocp-Apim-Subscription-Key": translation_key,
            "Content-Type": "application/json",
        }
        data = [{"text": user_input}]
        response = requests.post(translation_url, headers=headers, json=data)
        translated_text = response.json()[0]["translations"][0]["text"]

        # Convert translated text to speech
        synthesis_url = "https://eastus.tts.speech.microsoft.com/cognitiveservices/v1"
        headers = {
            "Authorization": "Bearer " + voice_synthesis_key,
            "Content-Type": "application/ssml+xml",
        }
        xml_body = f"<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='{selected_language}'><voice name='en-US-GuyNeural'>{translated_text}</voice></speak>"
        response = requests.post(synthesis_url, headers=headers, data=xml_body)
        audio_url = response.headers["location"]

        return render_template("index.html", user_input=user_input, translated_text=translated_text, audio_url=audio_url)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
