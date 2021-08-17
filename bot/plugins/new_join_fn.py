#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | yesraaj11


from bot.localisation import Localisation
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

async def new_join_f(client, message):
    # delete all other messages, except for AUTH_USERS
    await message.delete(revoke=True)
    # reply the correct CHAT ID,
    # and LEAVE the chat
    chat_type = message.chat.type
    if chat_type != "private":
        await message.reply_text(
            Localisation.WRONG_MESSAGE.format(
                CHAT_ID=message.chat.id
            )
        )
        # leave chat
        await message.chat.leave()


async def help_message_f(client, message):
    # display the /help message
    await message.reply_text(
        Localisation.HELP_MESSAGE,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Support', url='https://telegram.me/share/url?url=**Syn%20-%20Video%20-%20Compressor**%20%0A%0AYou%20can%20Compress%20Telegram%20Videos%0A%0ACompress%20now%20-%20@Synvidcombot')
                ]
            ]
        ),
        quote=True
    )
