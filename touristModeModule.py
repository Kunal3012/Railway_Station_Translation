from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
import requests

class TouristModeApp(App):
    def __init__(self, **kwargs):
        super(TouristModeApp, self).__init__(**kwargs)
        self.azure_translation_key = "YOUR_AZURE_TRANSLATION_API_KEY"
        self.google_translate_enabled = True  # Set to True if using Google Translate

    def build(self):
        self.languages = ["English", "Hindi", "Spanish", "French", "German"]  # Add more languages
        self.selected_language = "English"  # Default language

        layout = BoxLayout(orientation="vertical")

        # Language selection spinner
        self.spinner = Spinner(text=self.selected_language, values=self.languages)
        self.spinner.bind(text=self.on_spinner_select)
        layout.add_widget(self.spinner)

        # Text translation label
        self.translation_label = Label(text="Translation will appear here")
        layout.add_widget(self.translation_label)

        # Translate button
        translate_button = Button(text="Translate", on_press=self.translate_text)
        layout.add_widget(translate_button)

        return layout

    def on_spinner_select(self, instance, text):
        self.selected_language = text

    def translate_text(self, instance):
        text_to_translate = "Hello, world!"  # Replace with user input
        if self.selected_language != "English":
            # Translate to the selected language using Azure Translator Service
            translation_url = f"https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to={self.selected_language.lower()}"
            headers = {
                "Ocp-Apim-Subscription-Key": self.azure_translation_key,
                "Content-Type": "application/json",
            }
            data = [{"text": text_to_translate}]
            response = requests.post(translation_url, headers=headers, json=data)
            translated_text = response.json()[0]["translations"][0]["text"]
        else:
            translated_text = text_to_translate

        self.translation_label.text = translated_text

    def switch_to_google_translate(self):
        # Code to switch to Google Translate (offline mode) if desired
        pass

if __name__ == '__main__':
    TouristModeApp().run()
