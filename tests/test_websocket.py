import asyncio
import inspect

import pytest
from channels.testing import WebsocketCommunicator
from django.db.models import Model

from config.asgi import application

WS_HEADERS = [(b"origin", b"http://localhost")]


def test_no_chat_models():
    import apps.chat.models as chat_models

    for name, obj in inspect.getmembers(chat_models, inspect.isclass):
        if issubclass(obj, Model) and obj is not Model and getattr(obj._meta, "app_label", None) == "chat":
            pytest.fail(f"Unexpected chat model: {name}")


def test_ws_connect_closes_immediately():
    async def _run():
        communicator = WebsocketCommunicator(
            application, "/ws/chat/test-room/", headers=WS_HEADERS
        )
        connected, _ = await communicator.connect()
        assert connected is False
        await communicator.disconnect()

    asyncio.run(_run())


def test_ws_close_code_4403():
    async def _run():
        communicator = WebsocketCommunicator(
            application, "/ws/chat/test-room/", headers=WS_HEADERS
        )
        connected, close_code = await communicator.connect()
        assert connected is False
        assert close_code == 4403
        await communicator.disconnect()

    asyncio.run(_run())
