import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from SWEET_TOXIC_MUSIC import LOGGER, app, userbot
from SWEET_TOXIC_MUSIC.core.call import WEREWOLF_DEMON
from SWEET_TOXIC_MUSIC.misc import sudo
from SWEET_TOXIC_MUSIC.plugins import ALL_MODULES
from SWEET_TOXIC_MUSIC.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("SWEET_TOXIC_MUSIC.plugins" + all_module)
    LOGGER("SWEET_TOXIC_MUSIC.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await WEREWOLF_DEMON.start()
    try:
        await WEREWOLF_DEMON.stream_call("https://graph.org/file/7e7c0564bfb98e9ec652f.jpg")
    except NoActiveGroupCall:
        LOGGER("SWEET_TOXIC_MUSIC").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await WEREWOLF_DEMON.decorators()
    LOGGER("SWEET_TOXIC_MUSIC").info(
        "WEREWOLF_DEMON Music started"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("SWEET_TOXIC_MUSIC").info("Stopping Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
