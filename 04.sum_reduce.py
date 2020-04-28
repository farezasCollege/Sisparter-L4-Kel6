# import mpi4py
from mpi4py import MPI

# import library random untuk generate angka integer secara random
import random

## buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.Get_rank()

# dapatkan total proses berjalan
size = comm.Get_size()

# generate angka integer secara random untuk setiap proses
ran = random.randint(1,100)
print("random -> ",ran)
# lakukam penjumlahan dengan teknik reduce, root reduce adalah proses dengan rank 0
jum = comm.allreduce(ran, op=MPI.SUM)

# jika saya proses dengan rank 0 maka saya akan menampilkan hasilnya
if rank==0:
    print("Hasil : ", jum)

