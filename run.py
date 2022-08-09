# -*- coding: utf-8 -*-
import asyncio
import os

import botpy
from botpy import logging
from botpy.ext.cog_yaml import read
from botpy.message import Message
from typing import Union

import handler

test_config = read(os.path.join(os.path.dirname(__file__), "config.yaml"))

activeChannel=["9534920"]
startup="Azalea已经启动！"

class MyClient(botpy.Client):
    async def on_ready(self):
        for id in activeChannel:
            await self.api.post_message(channel_id=id, content=startup)

    async def on_at_message_create(self, message: Message):
        if "sleep" in message.content:
            await asyncio.sleep(10)
        await message.reply(content=f"机器人{self.robot.name}收到你的@消息了: {message.content}")

    async def on_message_create(self, message: Message):
        content=message.content
        if content.startswith("表情包"):
            words=content.split(" ")
            if len(words)==1:
                await message.reply(content="未检测到表情包关键词")
            else:
                stickers=handler.getStickers(words[1])
                for sticker in stickers:
                    await message.reply(file_image=sticker)
        elif content.startswith("帮助") or content.startswith("help"):
            await message.reply(content="Azalea bot 使用帮助\n\t1. 表情包 关键词；将会在本地搜索并发送关键词相关的表情包\n")
        else:
            await message.reply(content=message.content)

if __name__ == "__main__":
    # 通过预设置的类型，设置需要监听的事件通道
    # intents = botpy.Intents.none()
    # intents.public_guild_messages=True

    # 通过kwargs，设置需要监听的事件通道
    intents = botpy.Intents(public_guild_messages=True, guild_messages=True)
    client = MyClient(intents=intents)
    client.run(appid=test_config["appid"], token=test_config["token"])