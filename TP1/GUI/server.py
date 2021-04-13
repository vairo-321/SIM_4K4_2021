"""
    server.py

    Servidor websocket para servir la api al cliente en el navegador
"""

import asyncio
import websockets

async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")
    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")

async def server(websocket, path):
    event = await websocket.recv()

    if event == "ws-test":
        print("[TEST] ws server tested -> OK")
        await websocket.send("OK")

# Iniciar el servidor en localhost:8080
start_server = websockets.serve(server, "localhost", 8080)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
