import torch
from torch.nn import NLLLoss

def cross_entropy(y_hat,y):
    ce= -torch.log(y_hat[range(len(y_hat)),y])
    print(y_hat[range(len(y_hat)),y])
    print("------------------")
    print(ce)
    print("------------------")
    return ce.mean()

labels = torch.tensor([0,2,3])
preds = torch.tensor([[0.2, 0.3, 0.5,0.1], [0.2, 0.3, 0.5,0.1],[0.2, 0.3, 0.5,0.1]])
print("ce",cross_entropy(preds, labels))


# Implementation of cross-entropy loss in PyTorch combines `nn.LogSoftmax()`
# and `nn.NLLLoss()`
nll_loss = NLLLoss()
loss = nll_loss(torch.log(preds), labels)
print("negative loglikelihood",loss)