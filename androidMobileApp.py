import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
import speech_recognition as sr

kivy.require('1.11.1')

class MyLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # Create a label for instructions
        self.add_widget(Label(text="Press the button to start recording audio:"))

        # Create a button for audio input
        self.audio_button = Button(text="Record Audio")
        self.audio_button.bind(on_press=self.record_audio)
        self.add_widget(self.audio_button)

        # Create a dropdown list for language selection
        self.language_spinner = Spinner(
            text='Select Language',
            values=['English', 'Hindi', 'Spanish'],  # Add more languages as needed
        )
        self.add_widget(self.language_spinner)

        # Create an area for announcements
        self.announcement_label = Label(text="", halign='center', valign='middle')
        self.add_widget(self.announcement_label)

    def record_audio(self, instance):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Please speak something...")
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language="en")  # Change the language as needed
            self.announcement_label.text = f"You said: {text}"
        except sr.UnknownValueError:
            self.announcement_label.text = "Sorry, I could not understand your speech."
        except sr.RequestError as e:
            self.announcement_label.text = "Sorry, an error occurred while making the request to Google."

class MyApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()
