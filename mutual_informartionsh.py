import torch
from self_info import nansum

def mutual_information(p_xy,p_x,p_y):
    mut_info = p_xy * torch.log2(p_xy/(p_x * p_y))
    out = nansum(mut_info)
    return out

print(mutual_information(torch.tensor([[0.1, 0.5], [0.1, 0.3]]),
torch.tensor([0.2, 0.8]), torch.tensor([[0.75, 0.25]])))