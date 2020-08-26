# This code is created by X.Zhang and licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import torch.nn as nn
import torch


class RBFLogits(nn.Module):
    def __init__(self, feature_dim, class_num, scale, gamma):
        super(RBFLogits, self).__init__()
        self.feature_dim = feature_dim
        self.class_num = class_num
        self.weight = nn.Parameter( torch.FloatTensor(class_num, feature_dim))
        self.bias = nn.Parameter(torch.FloatTensor(class_num))
        self.scale = scale
        self.gamma = gamma
        nn.init.xavier_uniform_(self.weight)
    def forward(self, feat, label):
        diff = torch.unsqueeze(self.weight, dim=0) - torch.unsqueeze(feat, dim=1)
        diff = torch.mul(diff, diff)
        metric = torch.sum(diff, dim=-1)
        kernal_metric = torch.exp(-1.0 * metric / self.gamma)
        if self.training:
            train_logits = self.scale * kernal_metric
            # ###
            # Add some codes to modify logits, e.g. margin, temperature and etc.
            # ###
            return train_logits
        else:
            test_logits = self.scale * kernal_metric
            return test_logits


class LinearLogits(nn.Module):
    def __init__(self, feature_dim, class_num):
        super(LinearLogits, self).__init__()
        self.feature_dim = feature_dim
        self.class_num = class_num
        self.weight = nn.Parameter( torch.FloatTensor(class_num, feature_dim))
        self.bias = nn.Parameter(torch.FloatTensor(class_num))
        nn.init.xavier_uniform_(self.weight)
    def forward(self, feat, label):
        logits = nn.functional.linear(feat, self.weight) + self.bias
        if self.training:
            train_logits = logits
            # ###
            # Add some codes to modify logits, e.g. margin, temperature and etc.
            # ###
            return train_logits
        else:
            test_logits = logits
            return test_logits