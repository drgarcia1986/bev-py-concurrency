import falcon
import requests


class DelayResource:
    def on_get(self, req, resp, delay):
        response = requests.get('https://httpbin.org/delay/{}'.format(delay))
        resp.body = '{}-{}'.format(delay, response.status_code)


api = falcon.API()
api.add_route('/{delay}/', DelayResource())
