import asyncio
import websockets 

async def echo(websocket , path):
    async for msg in websocket:
        print(msg , 'receive from client')
        greeting = f"Hi {msg}"
        await websocket.send(greeting)
    
asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, 'localhost', 8964))
asyncio.get_event_loop().run_forever()