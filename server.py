import asyncio
import websockets 

async def echo(websocket , path):
    async for msg in websocket:
        greeting = f"Hi {msg}"
        await websocket.send(greeting)
    
asyncio.run(websockets.serve(echo , 'localhost' , 8964))