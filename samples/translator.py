import argparse
import tensorflow as tf
from transformers import MarianTokenizer, TFAutoModelForSeq2SeqLM

def main(args):
    # Load the pre-trained model and tokenizer for translation
    model_name = f"Helsinki-NLP/opus-mt-{args.source_lang}-{args.target_lang}"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = TFAutoModelForSeq2SeqLM.from_pretrained(model_name)

    while True:
        input_text = input(f"Enter text in {args.source_lang} (or 'exit' to quit): ")
        if input_text.lower() == "exit":
            break
        translation = translate_text(input_text, model, tokenizer)
        print(f"Translation: {translation}")

def translate_text(input_text, model, tokenizer):
    input_text = input_text.lower()  # Preprocess text if needed
    inputs = tokenizer.encode(input_text, return_tensors="tf", padding=True, max_length=512, truncation=True)
    translated = model.generate(inputs, max_length=100, num_return_sequences=1)
    translation = tokenizer.batch_decode(translated, skip_special_tokens=True)
    return translation[0]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Transformer Translator")
    parser.add_argument("--source_lang", type=str, default="en", help="Source language code (e.g., 'en' for English)")
    parser.add_argument("--target_lang", type=str, default="fr", help="Target language code (e.g., 'fr' for French)")
    args = parser.parse_args()
    main(args)
