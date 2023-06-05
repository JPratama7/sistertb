from mpi4py import MPI
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

num_trains = 10

stations = ['Gambir', 'Bandung', 'Yogyakarta', 'Surabaya', 'Malang']

num_platforms = len(stations)

def schedule_trains(train_id):
    platform = random.randint(0, num_platforms - 1)  
    platform_name = stations[platform]
    print("Kereta api", train_id, "tiba di stasiun", "(", platform_name, ")")

# Master process
if rank == 0:
    for i in range(1, num_trains + 1):
        comm.send(i, dest=i % size, tag=i)

    for i in range(1, num_trains + 1):
        message = comm.recv(source=i % size, tag=i)
        print("Konfirmasi kereta api", message, "diterima")

else:
    train_id = comm.recv(source=0, tag=rank)
    schedule_trains(train_id)

    comm.send(train_id, dest=0, tag=rank)
