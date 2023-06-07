import asyncio
import time
from random import randint

async def penjadwalan_kereta():
    print('Memulai penjadwalan kereta api\n')
    input_value = randint(0, 1)
    await asyncio.sleep(1)

    if input_value == 0:
        result = await jadwal_perjalanan_1(input_value)
    else:
        result = await jadwal_perjalanan_2(input_value)

    print('Proses Transisi:\nMemulai penjadwalan kereta api memanggil ' + result)


async def jadwal_perjalanan_1(transition_value: int) -> str:
    output_value = 'Jadwal Perjalanan 1 dengan nilai transisi = %s\n' % transition_value
    input_value = randint(0, 1)
    await asyncio.sleep(1)

    print('...evaluasi...')
    if input_value == 0:
        result = await jadwal_perjalanan_3(input_value)
    else:
        result = await jadwal_perjalanan_2(input_value)

    return output_value + 'Jadwal Perjalanan 1 memanggil %s' % result


async def jadwal_perjalanan_2(transition_value: int) -> str:
    output_value = 'Jadwal Perjalanan 2 dengan nilai transisi = %s\n' % transition_value
    input_value = randint(0, 1)
    await asyncio.sleep(1)

    print('...evaluasi...')
    if input_value == 0:
        result = await jadwal_perjalanan_1(input_value)
    else:
        result = await jadwal_perjalanan_3(input_value)

    return output_value + 'Jadwal Perjalanan 2 memanggil %s' % result


async def jadwal_perjalanan_3(transition_value: int) -> str:
    output_value = 'Jadwal Perjalanan 3 dengan nilai transisi = %s\n' % transition_value
    input_value = randint(0, 1)
    await asyncio.sleep(1)

    print('...evaluasi...')
    if input_value == 0:
        result = await jadwal_perjalanan_1(input_value)
    else:
        result = await end_state(input_value)

    return output_value + 'Jadwal Perjalanan 3 memanggil %s' % result


async def end_state(transition_value: int) -> str:
    output_value = 'End State dengan nilai transisi = %s\n' % transition_value
    print('...menghentikan komputasi...')
    return output_value


if __name__ == '__main__':
    print('Simulasi Sistem Penjadwalan Kereta API menggunakan Asyncio Coroutine')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(penjadwalan_kereta())
