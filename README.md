# python-sample-apps-with-trasnformers


## Table of Contents

- [Summary](#summary)
- [References](#references)
- [How to use](#how-to-use)

## Summary

Sample apps utilizing the transformers pip package.

## References

/

## How to use

Execute the following to run a sample app trough a docker container:

```sh
# Build the docker image
docker build -t python-sample-with-transformers:stable .
# Run a container
docker run --rm -it python-sample-with-transformers:stable bash -c "python3 samples/en-to-fr-translator.py"
```

In order to clear docker resources:

````sh
docker rm -f $(docker ps -qa)
docker system prune --volumes --force
# In order to remove dangling images (e.g. `ERROR: Could not install packages due to an EnvironmentError: [Errno 28] No space` could appear on Windows OS for example)
docker image prune
```