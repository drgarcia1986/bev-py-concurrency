import asyncio

import aiohttp


async def make_get(delay):
    response = await aiohttp.get('https://httpbin.org/delay/{}'.format(delay))
    response.close()
    return delay, response.status == 200


async def make_requests(*delays):
    requests = [make_get(d) for d in delays]
    return await asyncio.gather(*requests)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    responses = loop.run_until_complete(make_requests(5, 2, 3))
    for response in responses:
        print(response)

    print('Done')
