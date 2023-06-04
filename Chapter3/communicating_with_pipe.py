import multiprocessing


def create_jadwal(pipe):
    output_pipe, _ = pipe
    stasiun_kereta = ['Gambir', 'Bandung', 'Yogyakarta', 'Surabaya', 'Malang']
    for stasiun in stasiun_kereta:
        output_pipe.send(stasiun)
    output_pipe.close()


def proses_jadwal(pipe_1, pipe_2):
    close, input_pipe = pipe_1
    close.close()
    output_pipe, _ = pipe_2
    try:
        while True:
            stasiun = input_pipe.recv()
            print(f"Memproses jadwal perjalanan kereta api di stasiun {stasiun}")
        

            output_pipe.send(f"Proses jadwal kereta api di stasiun {stasiun} selesai.")
    except EOFError:
        output_pipe.close()


if __name__ == '__main__':
    pipe_1 = multiprocessing.Pipe(True)
    process_pipe_1 = multiprocessing.Process(target=create_jadwal, args=(pipe_1,))
    process_pipe_1.start()

    pipe_2 = multiprocessing.Pipe(True)
    process_pipe_2 = multiprocessing.Process(target=proses_jadwal, args=(pipe_1, pipe_2,))
    process_pipe_2.start()

    pipe_1[0].close()
    pipe_2[0].close()

    try:
        while True:
            print(pipe_2[1].recv())
    except EOFError:
        print("End")
