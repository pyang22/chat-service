from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    """WebSocket consumer stub — implemented in Phase 3."""

    async def connect(self) -> None:
        await self.close(code=4403)
