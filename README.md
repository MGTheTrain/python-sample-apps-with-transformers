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

- Build the docker image: `docker build -t python-sample-with-transformers:stable .`
- Run a container: `docker run --rm -it python-sample-with-transformers:stable sh`. Navigate in the container process to the `samples` folder (via `cd samples`) and execute one of those, e.g. `python en-to-france-translator.py`
- In order to remove dangling images: `docker image prune -a`