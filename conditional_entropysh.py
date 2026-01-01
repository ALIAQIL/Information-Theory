import torch
from self_info import nansum

def conditional_entropy(p_xy, p_x):
    p_y_given_x = p_xy/p_x
    cond_ent = -p_xy * torch.log2(p_y_given_x)
    out = nansum(cond_ent)
    return out
print(conditional_entropy(torch.tensor([[0.1, 0.5], [0.2, 0.3]]),
torch.tensor([0.2, 0.8])))