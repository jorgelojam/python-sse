from aiohttp_sse_client import client as sse_client
import asyncio

async def notification():
    async with sse_client.EventSource('http://127.0.0.1:8000/stream') as event_source:
        try:
            async for event in event_source:
                print(event)
        except ConnectionError:
            pass

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(notification())
    loop.close()

if __name__ == '__main__':
    main()