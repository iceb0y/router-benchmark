from asyncio import get_event_loop
from aiohttp import web
from fixture import register

router = web.UrlDispatcher()
register(lambda method, path, name: router.add_route(method, path, lambda: name, name=name))

class URL:
    raw_path = '/d/twd2/records-conn/iframe.html'

class Request:
    _method = 'GET'
    rel_url = URL()

async def main():
    request = Request()
    for i in range(100000):
        await router.resolve(request)

loop = get_event_loop()
loop.run_until_complete(main())
