import tensorflow as tf
from transformers import MarianTokenizer, TFAutoModelForSeq2SeqLM

# Load the pre-trained model and tokenizer for translation (e.g., English to Chinese)
model_name = "Helsinki-NLP/opus-mt-en-zh"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = TFAutoModelForSeq2SeqLM.from_pretrained(model_name)

def translate_text(input_text, source_lang="en", target_lang="zh"):
    input_text = input_text.lower()  # Preprocess text if needed
    inputs = tokenizer.encode(input_text, return_tensors="tf", padding=True, max_length=512, truncation=True)
    translated = model.generate(inputs, max_length=100, num_return_sequences=1)
    translation = tokenizer.batch_decode(translated, skip_special_tokens=True)
    return translation[0]

if __name__ == "__main__":
    while True:
        input_text = input("Enter text in English (or 'exit' to quit): ")
        if input_text.lower() == "exit":
            break
        translation = translate_text(input_text, source_lang="en", target_lang="fr")
        print(f"Translation: {translation}")
