import requests


def make_get(delay):
    response = requests.get('https://httpbin.org/delay/{}'.format(delay))
    return delay, response.status_code == 200


if __name__ == "__main__":
    print('start requests')
    print(make_get(5))
    print(make_get(2))
    print(make_get(3))
    print('Done')
