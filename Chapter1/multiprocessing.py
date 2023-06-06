import multiprocessing
from do_something import process_jadwal

if __name__ == '__main__':
    stasiun_kereta = ['Gambir', 'Bandung', 'Yogyakarta', 'Surabaya', 'Malang']

    num_processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=num_processes)

    results = [pool.apply_async(process_jadwal, args=(stasiun,)) for stasiun in stasiun_kereta]
    pool.close()
    pool.join()

    print("Proses jadwal kereta api selesai.")
