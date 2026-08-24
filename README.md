# Factorisation of Kohonen Self-organising Map (SOME)

## Pre-requisites

- `uv` v0.5+. Follow [these instructions](https://docs.astral.sh/uv/getting-started/installation/) to install.

## Quick Start

```bash
# Install dependencies
make install
```

## Remarks

- My approach to refactoring, observations, and my notes are in [refactoring_notes.ipynb](./refactoring_notes.ipynb).
- Repo itself is a striped down version of a cookiecutter template I maintain.
- I utilised `uv` to set up a simple development environment.
- I decided to keep all the code samples, tests, and benchmarking I have done in the repo in case there is interest. Below is a breakdown of those files.
  - [benchmark.ipynb](./benchmark.ipynb): Code for benchmarking. You can run the commands as they are to reproduce the plots.
  - [kohonen.py](./kohonen.py) and [kohonen_refactored.py](./kohonen_refactored.py): These are the main module files I used for testing, and refactoring.
  - [tests.py](./tests.py): Very simple (and, definitely not the best way for testing) test setup, so I did not break anything while refactoring.
- I have not used any AI tools to produce, or write any part you see in the repo.
- I spent in total 2-3 hours from start to finish including understanding how SOME works.