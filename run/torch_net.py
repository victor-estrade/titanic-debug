# coding: utf-8
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

# command line :
# python -m run.torch_net

import torch
import torch.nn as nn
import torch.optim as optim


import numpy as np


class L2(nn.Module):
    def __init__(self, n_in=1, n_out=1, n_unit=80):
        super().__init__()
        self.name = "{}x{:d}".format(self.__class__.__name__, n_unit)
        self.fc_in  = nn.Linear(n_in, n_unit)
        self.fc_out = nn.Linear(n_unit, n_out)

    def forward(self, x):
        x = self.fc_in(x)
        x = torch.relu(x)
        x = self.fc_out(x)
        return x

    def reset_parameters(self):
        self.fc_in.reset_parameters()
        self.fc_out.reset_parameters()


def to_torch(arr, cuda=True):
    """
    Transform given numpy array to a torch.Tensor
    """
    tensor = arr if torch.is_tensor(arr) else torch.from_numpy(arr)
    if cuda:
        tensor = tensor.cuda()
    return tensor


def generate_data(n_samples=2000, n_features=1, n_classes=2):
    X = np.random.random(size=(n_samples, n_features)).astype(np.float32)
    y = np.random.randint(0, n_classes, size=n_samples)
    return X, y


def run_one_training_step(X, y, net, criterion, optimizer, cuda_flag):
    X_batch = to_torch(X, cuda=cuda_flag)
    y_batch = to_torch(y, cuda=cuda_flag)
    optimizer.zero_grad()  # zero-out the gradients because they accumulate by default
    y_pred = net.forward(X_batch)
    loss = criterion(y_pred, y_batch)
    loss.backward()  # compute gradients
    optimizer.step()  # update params


def run(cuda_flag=False):
    n_samples = 2000
    n_features = 1
    n_classes = 2

    net = L2(n_in=n_features, n_out=n_classes, n_unit=20)
    criterion = torch.nn.CrossEntropyLoss(reduction='mean')
    optimizer = optim.Adam(net.parameters())

    if cuda_flag:
        net = net.cuda()
        criterion = criterion.cuda()

    X, y = generate_data(n_samples=n_samples, n_features=n_features, n_classes=n_classes)
    run_one_training_step(X, y, net, criterion, optimizer, cuda_flag)



HELLO_MSG = \
"""
Hello !
Running run.torch_net
"""

END_MSG = "OK"


def main():
    print(HELLO_MSG)
    run()
    print(END_MSG)


if __name__ == '__main__':
    main()
