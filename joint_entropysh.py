import torch
from self_info import nansum

def joint_entropy(p_xy):
    joint_ent = -p_xy * torch.log2(p_xy)
    out = nansum(joint_ent)
    return out

print(joint_entropy(torch.tensor([[0.1, 0.5], [0.1, 0.3]])))