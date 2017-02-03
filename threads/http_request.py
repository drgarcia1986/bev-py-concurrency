from concurrent.futures import ThreadPoolExecutor, as_completed

import requests


def make_get(delay):
    response = requests.get('https://httpbin.org/delay/{}'.format(delay))
    return delay, response.status_code == 200


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=3) as executor:
        print('start threads')
        futures = [
            executor.submit(make_get, 5),
            executor.submit(make_get, 2),
            executor.submit(make_get, 3),
        ]
        print('waiting...')
        for f in as_completed(futures):
            print(f.result())

    print('Done')
