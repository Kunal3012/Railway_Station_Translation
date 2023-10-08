from azure.cognitiveservices.translator.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials

def translate_and_transliterate(text, target_language):
    # Set up Azure Translator Service client
    subscription_key = "<YourAzureSubscriptionKey>"
    endpoint = "<YourAzureEndpoint>"
    credentials = CognitiveServicesCredentials(subscription_key)
    translator_client = TextAnalyticsClient(endpoint, credentials)

    # Translate text to the target language
    translation_result = translator_client.transliterate(
        text, target_language=target_language, is_transliteration_enabled=True
    )

    # Construct the output in JSON format
    output_json = {
        "original_text": text,
        "target_language": target_language,
        "translated_and_transliterated_text": translation_result.result
    }

    return output_json

# Example usage
if __name__ == "__main__":
    input_text = "Your input text to be translated and transliterated"
    target_language = "ta"  # Replace with the target Indian language code

    translated_transliterated_text = translate_and_transliterate(input_text, target_language)
    print("Translated and Transliterated Text: ", translated_transliterated_text)
