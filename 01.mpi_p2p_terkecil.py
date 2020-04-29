# import mpi4py
from mpi4py import MPI

# buat COMM
comm = MPI.COM_WORLD

# dapatkan rank proses
rank = comm.Get_rank()

# dapatkan total proses berjalan
size = comm.Get_size()

# jika saya rank ke 0 maka saya akan mengirimkan pesan ke proses yang mempunyai rank 1 s.d size
if rank == 0:
    for i range(1, size):
        sendMessage = ("send Rank %d" %i)
        com.send(sendMessage, dest=i)
	
# jika saya bukan rank 0 maka saya menerima pesan yang berasal dari proses dengan rank 0
else:
	recvMessage = comm.recv(source=0)
    print(recvMessage)
