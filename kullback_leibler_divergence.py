import torch
from self_info import nansum

def kl_divergence(p_x,q_x):
    kl_div = p_x * torch.log2(p_x/q_x)
    out = nansum(kl_div)
    return out.abs().item()

torch.manual_seed(1)
tensor_len = 10000
p = torch.normal(0, 1, (tensor_len, ))
q1 = torch.normal(-1, 1, (tensor_len, ))
q2 = torch.normal(1, 1, (tensor_len, ))
p = torch.sort(p)[0] #1 for original indices
q1 = torch.sort(q1)[0]
q2 = torch.sort(q2)[0]

print(p,q1,q2)

kl_pq1 = kl_divergence(p, q1)
kl_pq2 = kl_divergence(p, q2)
similar_percentage = abs(kl_pq1 - kl_pq2) / ((kl_pq1 + kl_pq2) / 2) * 100
print(kl_pq1, kl_pq2, similar_percentage)

kl_q2p = kl_divergence(q2, p)
differ_percentage = abs(kl_q2p - kl_pq2) / ((kl_q2p + kl_pq2) / 2) * 100

print(kl_q2p, differ_percentage)
