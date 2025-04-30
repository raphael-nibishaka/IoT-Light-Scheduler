import asyncio
import websockets
import os

PORT = 8765

async def handler(websocket):
    async for message in websocket:
        print(f"Received schedule: {message}")
        # Simulate forwarding with print
        await websocket.send(f"Schedule forwarded to MQTT: {message}")
        os.system(f"mosquitto_pub -t light/schedule -m '{message}'")

async def main():
    async with websockets.serve(handler, 'localhost', PORT):
        print(f"WebSocket server running on ws://localhost:{PORT}")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
