import asyncio
import json
from django.contrib.auth.models import User
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async


class AlpacaConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected", event)
        await self.send({
            "type": "websocket.accept"
        })
        while True:
            await asyncio.sleep(5)
            await self.send({
                "type": "websocket.send",
                "text": json.dumps({"message": "hello"})
            })

    async def websocket_receive(self, event):
        print("received", event)

    async def websocket_disconnect(self, event):
        print("disconnected", event)
