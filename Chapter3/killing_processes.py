import multiprocessing
import time

def jadwal_kereta():
    print('Memproses jadwal kereta api')
    for i in range(0, 10):
        print('--> Proses penjadwalan kereta api', i)
        time.sleep(1)
    print('Selesai memproses jadwal kereta api')

if __name__ == '__main__':
    p = multiprocessing.Process(target=jadwal_kereta)
    print('Proses sebelum eksekusi:', p, p.is_alive())
    p.start()
    print('Proses berjalan:', p, p.is_alive())
    p.join()
    print('Proses telah bergabung:', p, p.is_alive())
