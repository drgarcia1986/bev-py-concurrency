import aiohttp
from aiohttp import web


async def handle(request):
    delay = request.match_info.get('delay', 2)
    response = await aiohttp.get('https://httpbin.org/delay/{}'.format(delay))
    response.close()
    return web.Response(text='{}-{}'.format(delay, response.status))

if __name__ == "__main__":
    app = web.Application()
    app.router.add_get('/{delay}/', handle)

    web.run_app(app)
