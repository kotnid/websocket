import websockets
import asyncio 


async def hello(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send("tkt")
        name = await websocket.recv()
        print(f"recv : {name}")

asyncio.run(hello("ws:/localhost:8964"))        