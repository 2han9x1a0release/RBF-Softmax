# Installation Instructions

This document covers how to install **RBF-Softmax** and its dependencies.


**Requirements:**

- NVIDIA GPU, Linux, Python3
- PyTorch
- Some Python packages listed below



## PyTorch

To install PyTorch with CUDA support, follow the [installation instructions](https://pytorch.org/get-started/locally/) from the [PyTorch website](https://pytorch.org).

## RBF-Softmax

Clone the **RBF-Softmax** repository:

```
cd path/to/clone/rbf_softmax
git clone https://github.com/2han9x1a0release/RBF-Softmax
```

Install Python dependencies:

```
pip install -r RBF-Softmax/requirements.txt
```

Set up Python modules:

```
cd RBF-Softmax && python setup.py develop --user
```

## Datasets
RBF-Softmax applies pycls as codebase. So here we follows the setting in Pycls. This project finds datasets via symlinks from `pycls/datasets/data` to the actual locations where the dataset images and annotations are stored. For instructions on how to create symlinks for ImageNet, please see [`DATA.md`](DATA.md).

## Getting Started

Please see [`GETTING_STARTED.md`](GETTING_STARTED.md) for basic instructions on training and evaluation.
