from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def matrix_multiply(A, B):
    return np.dot(A, B)

if __name__ == "__main__":
    # Assume matrix size is divisible by the number of processes
    N = 8  # Size of the matrix
    A = np.random.rand(N, N) if rank == 0 else None
    B = np.random.rand(N, N) if rank == 0 else None

    # Scatter rows of A and columns of B to all processes
    local_A = np.zeros((N // size, N))
    local_B = np.zeros((N, N // size))

    comm.Scatter(A, local_A, root=0)
    comm.Bcast(B, root=0)
    local_B = B[:, rank * (N // size):(rank + 1) * (N // size)]

    # Each process computes its local part of the result matrix
    local_C = np.dot(local_A, local_B)

    # Gather the local results to form the final matrix C
    C = None
    if rank == 0:
        C = np.zeros((N, N))

    comm.Gather(local_C, C, root=0)

    if rank == 0:
        print("Resultant matrix C:")
        print(C)
