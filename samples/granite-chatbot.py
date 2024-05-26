import argparse
from transformers import AutoModelForCausalLM, AutoTokenizer

# List of viable model options
MODEL_OPTIONS = [
    "ibm-granite/granite-3b-code-base", # trained with 3 billion parameters
    "ibm-granite/granite-3b-code-instruct",
    "ibm-granite/granite-8b-code-base",
    "ibm-granite/granite-8b-code-instruct",
    "ibm-granite/granite-20b-code-base",
    "ibm-granite/granite-20b-code-instruct",
    "ibm-granite/granite-34b-code-base",
    "ibm-granite/granite-34b-code-instruct"
]

def load_model_and_tokenizer(model_path, device):
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path, device_map=device)
    model.eval()
    return model, tokenizer

def generate_text(model, tokenizer, input_text, device):
    input_tokens = tokenizer(input_text, return_tensors="pt").to(device)
    output_tokens = model.generate(**input_tokens)
    output_text = tokenizer.decode(output_tokens[0], skip_special_tokens=True)
    return output_text

def main(args):
    model, tokenizer = load_model_and_tokenizer(args.model_name, args.device)
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        
        output_text = generate_text(model, tokenizer, user_input, args.device)
        print("Chatbot:", output_text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Interactive text generation using a pretrained model")
    parser.add_argument("--model_name", type=str, choices=MODEL_OPTIONS, default="ibm-granite/granite-3b-code-base", help="Pre-trained model name or path")
    parser.add_argument("--device", type=str, choices=["cuda", "cpu"], default="cpu", help="Device to run the model on (cuda or cpu)")
    args = parser.parse_args()
    main(args)
