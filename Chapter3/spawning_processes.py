import multiprocessing
import time

class KeretaApi:
    def __init__(self, stasiun):
        self.stasiun = stasiun

    def jadwal_perjalanan(self):
        print(f"Jadwal perjalanan kereta api dari stasiun {self.stasiun} pada {time.ctime()}")

def penjadwalan_kereta_api(stasiun):
    kereta = KeretaApi(stasiun)
    kereta.jadwal_perjalanan()

if __name__ == '__main__':
    stasiun_kereta = ['Gambir', 'Bandung', 'Yogyakarta', 'Surabaya', 'Malang']

    processes = []
    for stasiun in stasiun_kereta:
        process = multiprocessing.Process(target=penjadwalan_kereta_api, args=(stasiun,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print("Proses penjadwalan kereta api selesai.")
