import websockets
import asyncio 


async def hello(uri):
    async with websockets.connect(uri) as websocket:
        ans = input("What is you name:")
        await websocket.send(ans)
        name = await websocket.recv()
        print(f"recv : {name}")

asyncio.get_event_loop().run_until_complete(
    hello('ws://localhost:8964'))