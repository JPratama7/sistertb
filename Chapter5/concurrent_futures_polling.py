import concurrent.futures
import time

stasiun_kereta = ['Gambir', 'Bandung', 'Yogyakarta', 'Surabaya', 'Malang']


def jadwal_perjalanan(stasiun: str) -> str:
    print(f"Memproses jadwal perjalanan kereta api di stasiun {stasiun}")
    time.sleep(1)
    return f"Jadwal perjalanan kereta api di stasiun {stasiun} selesai."


def penjadwalan_kereta(stasiun: str):
    result = jadwal_perjalanan(stasiun)
    print(result)


if __name__ == '__main__':
    start_time = time.perf_counter()
    for stasiun in stasiun_kereta:
        penjadwalan_kereta(stasiun)
    print(f"Sequential Execution in {time.perf_counter() - start_time} seconds")

    start_time = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(penjadwalan_kereta, stasiun_kereta)
    print(f"Thread Pool Execution in {time.perf_counter() - start_time} seconds")

    start_time = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        executor.map(penjadwalan_kereta, stasiun_kereta)
    print(f"Process Pool Execution in {time.perf_counter() - start_time} seconds")
