import argparse
import tensorflow as tf
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer

def main(args):
    # Load the pre-trained GPT-2 model and tokenizer
    model = TFGPT2LMHeadModel.from_pretrained(args.model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(args.model_name)

    # Chatbot loop
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        # Tokenize the user input
        input_ids = tokenizer.encode("You: " + user_input, return_tensors="tf")

        # Generate a response from the model
        response = model.generate(input_ids, max_length=100, num_return_sequences=1, pad_token_id=50256)
        chatbot_output = tokenizer.decode(response[0], skip_special_tokens=True)

        print("Chatbot:", chatbot_output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple GPT-2 Chatbot")
    parser.add_argument("--model_name", type=str, default="gpt2", help="Pre-trained model name (e.g. gpt2, gpt2-medium, gpt2-large, etc.)")
    args = parser.parse_args()
    main(args)
