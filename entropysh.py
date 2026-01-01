import torch
from self_info import nansum

def entropy(p):
    entropy= -p * torch.log2(p)
    out = nansum(entropy)
    return out

print(entropy(torch.tensor([0.1,0.5,0.1,0.3])))