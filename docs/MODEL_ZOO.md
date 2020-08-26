# Model Zoo

## Introduction

This file documents a collection of baselines and pretrained models trained with **RBF-Softmax**.

### Experimental Settings

- Please see [Experimental settings](https://github.com/facebookresearch/pycls/blob/master/MODEL_ZOO.md#experimental-settings) in pycls.

### Training Settings

- Please see [Training settings](https://github.com/facebookresearch/pycls/blob/master/MODEL_ZOO.md#training-settings) in pycls.

## Baselines

**NOTE: All the released RBF-Softmax models are from the last training epoch, not the best evaluated models. The results of best-performed models are higher than these released models.**

### ResNet Models
-  *As a reference: The top-1 error ImageNet baseline of ResNet-50 is 23.3% in [pycls](https://github.com/facebookresearch/pycls/blob/master/MODEL_ZOO.md), 23.85% in [Pytorch Pretrain](https://pytorch.org/docs/stable/torchvision/models.html), and 24.4% in [TensorFlow Slim](https://github.com/tensorflow/models/tree/master/research/slim)*

<table><tbody>
<!-- START ResNet TABLE -->
<!-- TABLE HEADER -->
<th valign="bottom">model</th>
<th valign="bottom">flops<br/>(B)</th>
<th valign="bottom">params<br/>(M)</th>
<th valign="bottom">acts<br/>(M)</th>
<th valign="bottom">batch<br/>size</th>
<th valign="bottom">error<br/>(top-1)</th>
<th valign="bottom">download</th>
<!-- TABLE BODY -->
<!-- ROW ResNet-50-RBF -->
<tr>
<td align="left"><a href="configs/dds_baselines/resnet/R-50-1x64d_dds_8gpu.yaml">ResNet-50</a></td>
<td align="center">4.1</td>
<td align="center">22.6</td>
<td align="center">11.1</td>
<td align="center">256</td>
<td align="center">22.9</td>
<td align="center"><a href="https://www.dropbox.com/s/geo7xb4gz422n1r/RBF_ResNet50.pyth?dl=0">model</a></td>
</tr>
<!-- END ResNet TABLE -->
</tbody></table>


### EfficientNet Models
- *As a reference: The top-1 ImageNet baseline of EfficientNet-B0,B1,B4 is 24.9%, 24.1%, 21.2% in [pycls](https://github.com/facebookresearch/pycls/blob/master/MODEL_ZOO.md), respectively.*


<table><tbody>
<!-- START EfficientNet TABLE -->
<!-- TABLE HEADER -->
<th valign="bottom">model</th>
<th valign="bottom">flops<br/>(B)</th>
<th valign="bottom">params<br/>(M)</th>
<th valign="bottom">acts<br/>(M)</th>
<th valign="bottom">batch<br/>size</th>
<th valign="bottom">error<br/>(top-1)</th>
<th valign="bottom">download</th>
<!-- TABLE BODY -->
<!-- ROW EfficientNet-B0-RBF -->
<tr>
<td align="left"><a href="configs/EffNet-B0_RBF_8gpu.yaml">EfficientNet-B0</a></td>
<td align="center">0.4</td>
<td align="center">5.3</td>
<td align="center">6.7</td>
<td align="center">256</td>
<td align="center">24.8</td>
<td align="center"><a href="https://www.dropbox.com/s/d95nvzufu0iopsw/RBF_EffNet-B0.pyth?dl=0">model</a></td>
</tr>
<!-- ROW EfficientNet-B1-RBF -->
<tr>
<td align="left"><a href="configs/EffNet-B1_RBF_8gpu.yaml">EfficientNet-B1</a></td>
<td align="center">0.7</td>
<td align="center">7.8</td>
<td align="center">10.9</td>
<td align="center">256</td>
<td align="center">23.5</td>
<td align="center"><a href="https://www.dropbox.com/s/4n4yxyjxllxyavv/rbf_effnet-b1.pyth?dl=0">model</a></td>
</tr>
<!-- ROW EfficientNet-B4-RBF -->
<tr>
<td align="left"><a href="configs/EffNet-B4_RBF_8gpu.yaml">EfficientNet-B4</a></td>
<td align="center">4.2</td>
<td align="center">19.0</td>
<td align="center">48.5</td>
<td align="center">128</td>
<td align="center">21.1</td>
<td align="center"><a href="https://www.dropbox.com/s/rp6bevik3p1qke1/rbf_effnet-b4.pyth?dl=0">model</a></td>
</tr>
<!-- END EfficientNet TABLE -->
</tbody></table>
