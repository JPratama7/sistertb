
import threading
from do_something import process_jadwal

if __name__ == '__main__':
    stasiun_kereta = ['Gambir', 'Bandung', 'Yogyakarta', 'Surabaya', 'Malang']

    threads = []
    for stasiun in stasiun_kereta:
        thread = threading.Thread(target=process_jadwal, args=(stasiun,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Proses jadwal kereta api selesai.")
