# import mpi4py
from mpi4py import MPI

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.Get_rank()

# dapatkan total proses berjalan
size = comm.Get_size()

# print(rank)
# jika saya rank 0 maka saya akan melakukan broadscast
data = "halo aku nabil"
if rank == 0:
    data = comm.bcast("mengirim: "+data, root=0)
# jika saya bukan rank 0 maka saya menerima pesan
else:
    data = "menerima: "+data

print ('rank: ', rank, data)
data = comm.bcast(data, root=0)