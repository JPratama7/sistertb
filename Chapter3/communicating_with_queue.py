import multiprocessing
import random
import time

class TrainProducer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        stasiun_kereta = ['Gambir', 'Bandung', 'Yogyakarta', 'Surabaya', 'Malang']
        for stasiun in stasiun_kereta:
            jadwal = self.generate_jadwal()
            kereta = {"stasiun": stasiun, "jadwal": jadwal}
            self.queue.put(kereta)
            print(f"TrainProducer: Jadwal kereta menuju {stasiun} ({jadwal}) ditambahkan ke antrian")
            time.sleep(1)

    def generate_jadwal(self):
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        return f"{hour:02d}:{minute:02d}"

class TrainConsumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            if self.queue.empty():
                print("TrainConsumer: Antrian kosong, proses selesai")
                break
            else:
                time.sleep(2)
                kereta = self.queue.get()
                stasiun = kereta["stasiun"]
                jadwal = kereta["jadwal"]
                print(f"TrainConsumer: Kereta menuju {stasiun} ({jadwal}) dikeluarkan dari antrian")
                time.sleep(1)

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    train_producer = TrainProducer(queue)
    train_consumer = TrainConsumer(queue)
    train_producer.start()
    train_consumer.start()
    train_producer.join()
    train_consumer.join()
