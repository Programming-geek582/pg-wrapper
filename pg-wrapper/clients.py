import aiohttp, requests
from .errors import NoUrlError

class AsyncApiClient:
    """An api client that is for asynchorous enviorenments"""
    def __init__(self):
        super().__init__()

    @staticmethod
    async def get_programming_joke() -> str:
        async with aiohttp.ClientSession() as session:
            url = await session.get('https://restapi.htmlgeek.repl.co/api/v2/joke/programming')
            json = await url.json()
            return json['joke']

    @staticmethod
    async def shorten(url : str = None):
        if not url:
            raise NoUrlError('You did not provide a url to shorten')
        async with aiohttp.ClientSession() as session:
            url = await session.get(f'https://restapi.htmlgeek.repl.co/api/v2/shorten?url={url}')
            json = await url.json()
            return json['short_url']

class SyncApiClient:
    """An api client for synchorous enviorenments"""
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def get_programming_joke() -> str:
        r = requests.get('https://restapi.htmlgeek.repl.co/v2/joke/programming')
        res = r.json()
        return res['joke']

    @staticmethod
    def shorten(url : str = None):
        if not url:
            raise NoUrlError('You did not provide a url to shorten')
        r = requests.get(f'https://restapi.htmlgeek.repl.co/api/v2/shorten?url={url}')
        res = r.json()
        return res['joke']
