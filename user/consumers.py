import asyncio
import json
from django.contrib.auth.models import User
from channels.consumer import AsyncConsumer
from django.conf import settings
from channels.db import database_sync_to_async


class AlpacaConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected", event)
        await self.send({
            "type": "websocket.accept"
        })
        market_data = settings.API.get_barset("SPY", 'minute', limit=5)
        while True:
            await self.send({
                "type": "websocket.send",
                "text": json.dumps({"data": market_data})
            })
            await asyncio.sleep(60)

    async def websocket_receive(self, event):
        print("received", event)

    async def websocket_disconnect(self, event):
        print("disconnected", event)
