# import random
# from mpi4py import MPI

# comm = MPI.COMM_WORLD
# size = comm.size
# rank = comm.rank

# inside = 0
# nsamples = 120000

# for i in range(nsamples):
#     x = random.random();
#     y = random.random();
#     if (x*x)+(y*y)<1:
#         inside += 1


# mypi = (4.0 * inside)/nsamples

# print ("mypi =",mypi,"for rank", rank)


# y = comm.reduce(mypi, op=MPI.SUM)

# if rank==0:
#     pi = (1.0 / size) * y

#     print("Computed value of pi on " + str(size) + " processors is " + str(pi))
#     print("Using " + str(size) + " samples.")




# from mpi4py import MPI

# comm = MPI.COMM_WORLD
# size = comm.size
# rank = comm.rank

# def f(x):
#     return 4.0/(1.0+x*x)

# n = 512

# if rank == 0:
#     comm.bcast(n)


# h = 1.0/n
# local_sum = 0.0

# for i in range(rank+1,n+1, size):
#     x = h*(i-0.5)
#     y = f(x)
#     local_sum += y

# global_sum = comm.reduce(local_sum, MPI.SUM)
# if rank == 0:
#     print("PI is ",h*global_sum)


import random
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank

inside = 0
nsamples = 1200000

for i in range(nsamples):
    x = random.random();
    y = random.random();
    if (x*x)+(y*y)<1:
        inside += 1


#mypi = (4.0 * inside)/nsamples

print ("mypi =",inside,"for rank", rank)


y = comm.reduce(inside, op=MPI.SUM)
print("Y "+str(y))

if rank==0:
#    pi = (1.0 / size) * y
    pi = (4.0*y)/(nsamples*size)

    print("Computed value of pi on " + str(size) + " processors is " + str(pi))
    print("Using " + str(size) + " samples.")
