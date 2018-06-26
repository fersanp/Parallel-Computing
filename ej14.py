from mpi4py import MPI
 
comm=MPI.COMM_WORLD
rank = comm.rank
print("my rank is : " , rank)

if rank==1:
    data_send= "a     
    destination_process = 5
    source_process = 5
    data_received=comm.sendrecv(data_send,dest=destination_process,source =source_process)


if rank==5:
    data_send= "b"
    destination_process = 1
    source_process = 1
    data_received=comm.sendrecv(data_send,dest=destination_process,source=source_process)
