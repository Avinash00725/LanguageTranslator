from transformers import MarianMTModel, MarianTokenizer

class EnglishToHindiTranslator:
    def __init__(self, model_name="Helsinki-NLP/opus-mt-en-hi"):
        self.tokenizer = MarianTokenizer.from_pretrained(model_name)
        self.model = MarianMTModel.from_pretrained(model_name)

    def translate(self, text):
        # Prepare the text for the model
        tokens = self.tokenizer.prepare_seq2seq_batch([text], return_tensors="pt", padding=True)
        # Generate translation
        translation = self.model.generate(**tokens)
        # Decode the output
        translated_text = self.tokenizer.decode(translation[0], skip_special_tokens=True)
        return translated_text
