import torch
import time

# Matrix dimensions
N = 10000
M = 10000
K = 10000

# Random matrices
A = torch.rand(N, M)
B = torch.rand(M, K)

cstart = time.time()
# Matrix multiplication on CPU
result_cpu = torch.mm(A, B)
print("Time taken do matrix multiplication two matrix sizes 1000000*1000000 on cpu is ",time.time()-cstart)

# Move matrices to GPU
A_gpu = A.cuda()
B_gpu = B.cuda()

gstart = time.time()
# Matrix multiplication on GPU
result_gpu = torch.mm(A_gpu, B_gpu)

# Move result back to CPU for comparison
result_gpu_cpu = result_gpu.cpu()
print("Time taken do matrix multiplication two matrix sizes 1000000*1000000 on cpu is ",time.time()-gstart)


# Check if the results are the same
print("Are the results the same?", torch.allclose(result_cpu, result_gpu_cpu))

