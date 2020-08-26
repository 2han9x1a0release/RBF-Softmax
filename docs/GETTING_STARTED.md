# Getting Started

This document provides basic instructions for training and evaluation using **RBF-Softmax**.

- For general information about **RBF-Softmax**, please refer [`README.md`](../README.md)
- For installation, please refer [`INSTALL.md`](INSTALL.md)

## Training Models

Training on ImageNet by using EfficientNet-B1 backbone:

```
python tools/train_net.py --cfg configs/EffNet-B1-RBF_8gpu.yaml OUT_DIR /tmp
```

## Finetuning Models

Finetuning on ImageNet by using pretrained ResNet-50 model:

```
python tools/train_net.py --cfg configs/ResNet-50-RBF_8gpu.yaml TRAIN.WEIGHTS /path/to/weights/file OUT_DIR /tmp
```

## Evaluating Models

Evaluating pretrained EfficientNet-B4 model on ImageNet:

```
python tools/test_net.py --cfg configs/EffNet-B4-RBF_8gpu.yaml TEST.WEIGHTS /path/to/weights/file OUT_DIR /tmp
```
