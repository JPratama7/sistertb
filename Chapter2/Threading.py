
import time
import os
from random import randint
from threading import Thread

class TrainSchedule(Thread):
    def __init__(self, stasiun, jadwal):
        Thread.__init__(self)
        self.stasiun = stasiun
        self.jadwal = jadwal

    def run(self):
        print(f"Kereta menuju {self.stasiun} berangkat pada pukul {self.jadwal}")
        duration = randint(1, 10)
        time.sleep(duration)
        print(f"Kereta menuju {self.stasiun} tiba di tujuan pada pukul {self.jadwal}. Durasi perjalanan: {duration} detik.")

def main():
    start_time = time.time()

    schedules = [
        {"stasiun": "Gambir", "jadwal": "08:00"},
        {"stasiun": "Bandung", "jadwal": "09:30"},
        {"stasiun": "Yogyakarta", "jadwal": "11:15"},
        {"stasiun": "Surabaya", "jadwal": "13:45"},
        {"stasiun": "Malang", "jadwal": "15:20"}
    ]

    threads = []

    for schedule in schedules:
        stasiun = schedule["stasiun"]
        jadwal = schedule["jadwal"]
        thread = TrainSchedule(stasiun, jadwal)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Semua kereta telah berangkat dan tiba di tujuan")
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
