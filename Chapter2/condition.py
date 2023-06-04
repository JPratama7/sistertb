import logging
import multiprocessing
import time

LOG_FORMAT = '%(asctime)s %(processName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

def process_jadwal(stasiun):
    logging.info(f"Memproses jadwal perjalanan kereta api di stasiun {stasiun}")
   

if __name__ == '__main__':
    stasiun_kereta = ['Gambir', 'Bandung', 'Yogyakarta', 'Surabaya', 'Malang']

    num_processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=num_processes)

    start_time = time.time()

    results = [pool.apply_async(process_jadwal, args=(stasiun,)) for stasiun in stasiun_kereta]
    pool.close()
    pool.join()

    end_time = time.time()
    total_time = end_time - start_time

    logging.info("Proses jadwal kereta api selesai.")
    logging.info(f"Waktu total yang dibutuhkan: {total_time} detik")
