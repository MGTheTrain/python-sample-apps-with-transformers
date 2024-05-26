# python-sample-apps-with-trasnformers


## Table of Contents

- [Summary](#summary)
- [References](#references)
- [Getting started](#how-to-use)

## Summary

Sample TensorFlow and PyTorch apps utilizing the `transformers` pip package and trained transformer models.

## References

- [IBM granite-code-models Github repository](https://github.com/ibm-granite/granite-code-models?tab=readme-ov-file#inference)

## Getting started

### Tensorflow apps

Build the docker image:

```sh
docker build -t python-sample-with-transformers-and-tf:stable -f TensorFlow.Dockerfile .
```
Execute the following to run a TensorFlow sample app trough a docker container:

```sh
# Run in a docker container an app utilizing a huggface transofmer model trained for english to french translation tasks
docker run --rm -it python-sample-with-transformers-and-tf:stable bash -c "python3 samples/translator.py --source_lang en --target_lang fr"
# Run in a docker container an app utilizing a huggface transofmer model trained for english to german translation tasks
docker run --rm -it python-sample-with-transformers-and-tf:stable bash -c "python3 samples/translator.py --source_lang en --target_lang de"
# Run in a docker container an app utilizing a huggface transofmer model trained for english to chinese translation tasks
docker run --rm -it python-sample-with-transformers-and-tf:stable bash -c "python3 samples/translator.py --source_lang en --target_lang zh"
# Run in a docker container a chatbot app which utilizes a GPT2 transformer model
docker run --rm -it python-sample-with-transformers-and-tf:stable bash -c "python3 samples/chatbot.py --model_name <gpt2, gpt-large, gp2-x1>"
```

### Pytorch apps

**Option A - Preferred:**

Install pip dependencies and run PyTorch sample app:

```sh
pip install -r requirements.pt.txt
python3 samples/granite-chatbot.py --model_name <ibm-granite/granite-3b-code-base, ibm-granite/granite-3b-code-instruct, ibm-granite/granite-8b-code-base, ibm-granite/granite-8b-code-instruct, ibm-granite/granite-20b-code-base, ibm-granite/granite-20b-code-instruct, ibm-granite/granite-34b-code-base, ibm-granite/granite-34b-code-instruct> --device <cuda, cpu>
```

**Option B - Optional and process might be terminated due to insufficient memory:** 

Build the docker image:

```sh
docker build -t python-sample-with-transformers-and-pt:stable -f PyTorch.Dockerfile .
```
Execute the following to run a PyTorch sample app trough a docker container:

```sh
# Run in a docker container a granite chat bot app which utilizes a ibm-granite/granite-3b-code-base transformer model
# NOTE: 
# - Downloading pre-trained model files (weights, etc.) takes quite a long time and only CPU hardware is considered (no GPU mounting in Docker container considered)
# - Process might be terminated due to insufficient memory
docker run --rm -it python-sample-with-transformers-and-pt:stable bash -c "python3 samples/granite-chatbot.py --model_name <ibm-granite/granite-3b-code-base, ibm-granite/granite-3b-code-instruct, ibm-granite/granite-8b-code-base, ibm-granite/granite-8b-code-instruct, ibm-granite/granite-20b-code-base, ibm-granite/granite-20b-code-instruct, ibm-granite/granite-34b-code-base, ibm-granite/granite-34b-code-instruct>"
```

In order to clear docker resources:

```sh
docker rm -f $(docker ps -qa)
docker system prune --volumes --force
```
