# WS client example

import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8080"
    async with websockets.connect(uri) as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f"> {name}")

        greeting = await websocket.recv()
        print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(hello())

# import socket
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(('localhost',8090))
#
# s.send("gdgdgf")

