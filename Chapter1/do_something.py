import random

def process_jadwal(stasiun):
    print(f"Memproses jadwal kereta api di stasiun {stasiun}")
 
if __name__ == '__main__':
    stasiun_kereta = ['Gambir', 'Bandung', 'Yogyakarta', 'Surabaya', 'Malang']
    for stasiun in stasiun_kereta:
        process_jadwal(stasiun)
    print("Proses jadwal kereta api selesai.")