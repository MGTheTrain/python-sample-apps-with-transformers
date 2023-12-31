# python-sample-apps-with-trasnformers


## Table of Contents

- [Summary](#summary)
- [References](#references)
- [How to use](#how-to-use)

## Summary

Sample apps utilizing the transformers pip package and trained transformer models.

## References

/

## How to use

Build the docker image:

```sh
docker build -t python-sample-with-transformers:stable .
```
Execute the following to run a sample app trough a docker container:

```sh
# Run in a docker container an app utilizing a huggface transofmer model trained for english to french translation tasks
docker run --rm -it python-sample-with-transformers:stable bash -c "python3 samples/translator.py --source_lang en --target_lang fr"
# Run in a docker container an app utilizing a huggface transofmer model trained for english to german translation tasks
docker run --rm -it python-sample-with-transformers:stable bash -c "python3 samples/translator.py --source_lang en --target_lang de"
# Run in a docker container an app utilizing a huggface transofmer model trained for english to chinese translation tasks
docker run --rm -it python-sample-with-transformers:stable bash -c "python3 samples/translator.py --source_lang en --target_lang zh"
# Run in a docker container a chatbot app which utilizes a GPT2 transformer model
docker run --rm -it python-sample-with-transformers:stable bash -c "python3 samples/chatbot.py --model_name <gpt2, gpt-large, gp2-x1>"
```

In order to clear docker resources:

```sh
docker rm -f $(docker ps -qa)
docker system prune --volumes --force
# In order to remove dangling images (e.g. `ERROR: Could not install packages due to an EnvironmentError: [Errno 28] No space` could appear on Windows OS for example)
docker image prune
```
