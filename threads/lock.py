from concurrent.futures import ThreadPoolExecutor, wait
from time import sleep
from threading import Lock

counter = 0
lock = Lock()


def update_counter(count, delay):
    global counter
    for _ in range(count):
        with lock:
            current_counter = counter
            sleep(delay)
            counter = current_counter + 1


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=3) as executor:
        print('start threads')
        futures = [
            executor.submit(update_counter, 5, 0.5),
            executor.submit(update_counter, 3, 1),
            executor.submit(update_counter, 10, 0.2),
        ]
        print('waiting...')
        wait(futures)

    print('Final value is ', counter)
