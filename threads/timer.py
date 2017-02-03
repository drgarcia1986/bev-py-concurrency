from concurrent.futures import ThreadPoolExecutor, wait
from datetime import datetime
from time import sleep


def print_msg(msg, count, delay):
    for _ in range(count):
        sleep(delay)
        print('{}: {}'.format(datetime.now(), msg))


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=3) as executor:
        print('É hora do show!')
        futures = [
            executor.submit(print_msg, 'birl', 10, 1),
            executor.submit(print_msg, '37-anos', 5, 2),
            executor.submit(print_msg, 'ajuda o maluco doente', 2, 5),
        ]

        sleep(2)
        print('Acho que não vai dar hein')

        wait(futures)

    print('Fim!')
