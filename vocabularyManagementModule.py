class VocabularyManager:
    def __init__(self):
        self.vocabulary = {}  # Initialize an empty vocabulary dictionary

    def add_translation(self, source_phrase, target_phrase, source_language, target_language):
        # Add a translation to the vocabulary
        key = (source_phrase, source_language)
        if key not in self.vocabulary:
            self.vocabulary[key] = {}
        self.vocabulary[key][target_language] = target_phrase

    def get_translation(self, source_phrase, source_language, target_language):
        # Retrieve a translation from the vocabulary
        key = (source_phrase, source_language)
        if key in self.vocabulary and target_language in self.vocabulary[key]:
            return self.vocabulary[key][target_language]
        else:
            return None  # Translation not found

    def update_translation(self, source_phrase, new_target_phrase, source_language, target_language):
        # Update an existing translation in the vocabulary
        key = (source_phrase, source_language)
        if key in self.vocabulary:
            self.vocabulary[key][target_language] = new_target_phrase

    def delete_translation(self, source_phrase, source_language, target_language):
        # Delete a translation from the vocabulary
        key = (source_phrase, source_language)
        if key in self.vocabulary and target_language in self.vocabulary[key]:
            del self.vocabulary[key][target_language]

# Example usage
if __name__ == "__main__":
    vocabulary_manager = VocabularyManager()

    # Adding translations
    vocabulary_manager.add_translation("Hello", "नमस्ते", "en", "hi")
    vocabulary_manager.add_translation("Train", "ट्रेन", "en", "hi")

    # Retrieving translations
    translation = vocabulary_manager.get_translation("Hello", "en", "hi")
    print("Translation:", translation)

    # Updating translations
    vocabulary_manager.update_translation("Hello", "हैलो", "en", "hi")

    # Deleting translations
    vocabulary_manager.delete_translation("Train", "en", "hi")
