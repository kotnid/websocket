import websockets
import asyncio 


async def hello(uri):
    async with websockets.connect(uri) as websocket:
        ans = input("What is you name:")
        await websocket.send(ans)
        name = await websocket.recv()
        print(f"recv : {name}")

async def get(uri):
    async with websockets.connect(uri) as websocket:
        while True:
            msg = await websocket.recv()
            print(f"recv:{msg}")
asyncio.get_event_loop().run_until_complete(
    get('ws://127.0.0.1:8964/'))