import time

from celery import Celery

app = Celery('addTask', broker='amqp://guest@localhost//')

@app.task
def jadwal_perjalanan(stasiun: str) -> str:
    print(f"Memproses jadwal perjalanan kereta api di stasiun {stasiun}")
    time.sleep(1)
    return f"Jadwal perjalanan kereta api di stasiun {stasiun} selesai."

@app.task
def penjadwalan_kereta(stasiun: str):
    result = jadwal_perjalanan(stasiun)
    print(result)
