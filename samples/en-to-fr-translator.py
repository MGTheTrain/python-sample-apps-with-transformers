import tensorflow as tf
import tensorflow_text
import transformers
import sentencepiece
import numpy as np

# Load the MarianMT model and SentencePiece tokenizer for translation (e.g., English to French)
model_name = "Helsinki-NLP/opus-mt-en-fr"
model = transformers.TFAutoModelForTranslation.from_pretrained(model_name)
tokenizer = transformers.AutoTokenizer.from_pretrained(model_name)

def translate_text(input_text, source_lang="en", target_lang="fr"):
    input_text = input_text.lower()  # Preprocess text if needed
    input_ids = tokenizer.encode(input_text, return_tensors="tf", padding=True)
    translation = model.generate(input_ids, max_length=100, decoder_start_token_id=tokenizer.pad_token_id)
    translation_text = tokenizer.decode(translation[0], skip_special_tokens=True)
    return translation_text

if __name__ == "__main__":
    while True:
        input_text = input("Enter text in English (or 'exit' to quit): ")
        if input_text.lower() == "exit":
            break
        translation = translate_text(input_text, source_lang="en", target_lang="fr")
        print(f"Translation: {translation}")
