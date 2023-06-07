import asyncio
import time
import random

async def jadwal_perjalanan(stasiun: str):
    print(f"Memproses jadwal perjalanan kereta api di stasiun {stasiun}")
    await asyncio.sleep(random.randint(0, 5))
    print(f"Jadwal perjalanan kereta api di stasiun {stasiun} selesai")

async def penjadwalan_kereta(stasiun: str, end_time: float, loop: asyncio.AbstractEventLoop):
    await jadwal_perjalanan(stasiun)
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, penjadwalan_kereta, stasiun, end_time, loop)
    else:
        loop.stop()

async def main():
    loop = asyncio.get_event_loop()
    end_loop = loop.time() + 60

    stasiun_kereta = ['Gambir', 'Bandung', 'Yogyakarta', 'Surabaya', 'Malang']
    tasks = []
    for stasiun in stasiun_kereta:
        task = asyncio.create_task(penjadwalan_kereta(stasiun, end_loop, loop))
        tasks.append(task)
    
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
