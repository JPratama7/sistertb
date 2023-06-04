import multiprocessing
import time

def myFunc(stasiun):
    name = multiprocessing.current_process().name
    print(f"Processing train schedule for {stasiun} in process name: {name}")
   

if __name__ == '__main__':
    stasiun_kereta = ['Gambir', 'Bandung', 'Yogyakarta', 'Surabaya', 'Malang']
    processes = []

    for stasiun in stasiun_kereta:
        process = multiprocessing.Process(name=f"Process-{stasiun}", target=myFunc, args=(stasiun,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
