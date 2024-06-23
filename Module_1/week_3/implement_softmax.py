import torch
import torch.nn as nn
import math


class SoftMaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_max = torch.max(x, dim=0, keepdims=True)
        exps = torch.exp(x - x_max.values)
        partition = exps.sum(0, keepdims=True)
        return exps / partition


class MySoftMax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        exps = torch.exp(x)
        return exps / exps.sum()


def main():
    data = torch.Tensor([5, 2, 4])
    my_softmax = MySoftMax()
    output = my_softmax(data)
    print(output)

    data2 = torch.Tensor([1, 2, 300000000])
    output2 = my_softmax(data2)
    print(output2)

    data3 = torch.Tensor([1, 2, 3])
    softmax_stable = SoftMaxStable()
    output3 = softmax_stable(data3)
    print(output3)


if __name__ == '__main__':
    main()
