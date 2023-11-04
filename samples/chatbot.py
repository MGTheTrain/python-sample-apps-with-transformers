import tensorflow as tf
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained GPT-2 model and tokenizer
# model_name = "gpt2" # medium transformer model - less accuracy - requires less hardware resources
model_name = "gpt2-large" # large transformer model - more accuracy - requires more hardware resources
# model_name = "gpt2-x1" # very large transformer model - even more accuracy - requires even more hardware resources
model = TFGPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

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