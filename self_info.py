import torch

def nansum(x):
    return x[~torch.isnan(x)].sum()

def self_information(p):
    return -torch.log2(torch.tensor(p)).item()



if __name__ == "__main__":
    print(self_information(1/64))