from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["qoşul"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Meni önce yönetici etmelisen</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =   "VanessaMusicAsistan"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"•> **Senin İsteyinle Geldim** !")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>Asistan Zaten Qrupda Var</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>Asistan {user.first_name} üçün ağır qatılma isteklerine göre  qrupunuza Qatılamadı! Asistanın qrupda qadağa olunmadığından emin olun."
            "Veya Asistan Hesabını Qrupa Özün Eleva Edin </b>",
        )
        return
    await message.reply_text(
            "<b>Asistan Zaten Qrupda Var</b>",
        )
    
@USER.on_message(filters.group & filters.command(["ayril"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            f"<b>İstifadeçi qrupunuzdan terk ede bilmedi!."
            "\n\nYada özünüz çıxara bilersiniz</b>",
        )
        return
