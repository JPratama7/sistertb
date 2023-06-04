import logging
import threading
import time

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s")

class Train:
    def __init__(self, stasiun, jadwal):
        self.stasiun = stasiun
        self.jadwal = jadwal

    def depart(self):
        logging.info(f"Kereta menuju {self.stasiun} berangkat pada pukul {self.jadwal}")
        time.sleep(2)
        logging.info(f"Kereta menuju {self.stasiun} tiba di tujuan pada pukul {self.jadwal}")

def train_schedule(train):
    train.depart()

if __name__ == "__main__":
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
        train = Train(stasiun, jadwal)
        thread = threading.Thread(target=train_schedule, args=(train,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    logging.info("Semua kereta telah berangkat dan tiba di tujuan")
