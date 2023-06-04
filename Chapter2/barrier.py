from threading import Barrier, Thread
import time

class KeretaApi:
    def __init__(self, stasiun):
        self.stasiun = stasiun

    def jadwal_perjalanan(self):
        print(f"Jadwal perjalanan kereta api dari stasiun {self.stasiun} pada {time.ctime()}")

def penjadwalan_kereta_api(barrier, kereta):
    print(f"Memproses jadwal kereta api dari stasiun {kereta.stasiun}...")
    time.sleep(2)  
    kereta.jadwal_perjalanan()
    barrier.wait()
    print(f"Selesai memproses jadwal kereta api dari stasiun {kereta.stasiun}.")

def main():
    stasiun_kereta = ['Gambir', 'Bandung', 'Yogyakarta', 'Surabaya', 'Malang']
    barrier = Barrier(len(stasiun_kereta))
    threads = []

    for stasiun in stasiun_kereta:
        kereta = KeretaApi(stasiun)
        thread = Thread(target=penjadwalan_kereta_api, args=(barrier, kereta))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Proses penjadwalan kereta api selesai.")

if __name__ == "__main__":
    main()
