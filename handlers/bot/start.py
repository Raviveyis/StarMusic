# 𝐃𝐎𝐍𝐓 𝐌𝐄𝐒𝐒 𝐖𝐈𝐓𝐇 𝐂𝐎𝐃𝐄𝐒 𝐂𝐎𝐏𝐘𝐑𝐈𝐆𝐇𝐓 @SHAILENDRA34 | 
# 𝐃𝐞𝐚𝐫 𝐏𝐞𝐫𝐨 𝐩𝐩𝐥𝐬 𝐏𝐥𝐢𝐬𝐡 𝐃𝐨𝐧'𝐭 𝐫𝐞𝐦𝐨𝐯𝐞 𝐭𝐡𝐢𝐬 𝐥𝐢𝐧𝐞 𝐟𝐫𝐨𝐦 𝐡𝐞𝐫𝐞 🌚


from helpers.filters import command
from pyrogram import Client as bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import (BOT_NAME, SUPPORT_GROUP, OWNER_USERNAME, BOT_USERNAME)


@bot.on_message(filters.command("start"))
def start_(bot, message):
    
    START_TEXT = """**⭐ Salam✋ {}\n\n▫️Men {} \n\n▫️Sade Bir Musiqi Botuyam .\n\n▫️Meni Qrupunuza elave edib  yönetici edin ve musiqin keyfini çıxarın !**"""

    START_BUTTON = [
                [
                    InlineKeyboardButton(text="🎉 Meni Qrupa Elave edin 🎉", url=f"http://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
                [
                    InlineKeyboardButton(text="📝 Sahibim ", url=f"https://t.me/BenimKiller"),
                    InlineKeyboardButton(text="🇹🇷 Söhbet ", url="https://t.me/lovelesslifee"),
                ],                
                [                    
                    InlineKeyboardButton(text="📚 Bütün Emirler ", url="https://t.me/lovelesslifee/5"),
                ],
                
            ]
    message.reply_text(
        START_TEXT.format(message.from_user.mention, BOT_NAME, SUPPORT_GROUP),
        reply_markup=InlineKeyboardMarkup(START_BUTTON)
    )
    message.delete()

@bot.on_message(filters.command("hsusueue"))
def help_(bot, message):
    HELP_TXT = """Salam✋ {}\nişte yardım menüsü \nQrupuna elave edib musiqi keyfine başlayabilirsiniz @{} probleminiz nedir? 💫"""
    
    HELP_BUTTON = [
        [
            InlineKeyboardButton(text="🕹️ Esas emrler", callback_data="basic_"),
            InlineKeyboardButton(text="🕹️ Admin emrler", callback_data="admin_cmd"),
        ],
        [
            InlineKeyboardButton(text="🗑 Bağla", callback_data="close_"),
            InlineKeyboardButton(text="⬅️ Geri", callback_data="HOME"),
        ],
    ]
    message.reply_text(
        HELP_TXT.format(message.from_user.first_name, SUPPORT_GROUP),
        reply_markup=InlineKeyboardMarkup(HELP_BUTTON)
    )
    message.delete()

@bot.on_callback_query()
def callback_query(Client, callback: CallbackQuery):
    if callback.data == "help_":
    
        HELP_TXT = f"""Salam✋ işte yardım menyusu istediğiniz seçimi seçin ve keşf edin \nHer cür yardım veya problem  üçünn qatılın @{SUPPORT_GROUP} Probleminiz nedir 💫?"""
    
        HELP_BUTTON = [
            [
                InlineKeyboardButton(text="🕹️ Esas emrler", callback_data="bcd"),
                InlineKeyboardButton(text="🕹️ Admin emrler", callback_data="admin"),
            ],
            [
                InlineKeyboardButton(text="🗑 Bağla", callback_data="close_"),
                InlineKeyboardButton(text="⬅️ Geri", callback_data="HOME"),
            ],
        ]
        callback.edit_message_text(
            HELP_TXT,
            reply_markup=InlineKeyboardMarkup(HELP_BUTTON)
        )
    elif callback.data == "HOME":
 
        START_TEXT = f"""Salam✋, Men {BOT_NAME} \nSade ve gecikmesiz bir bottur\nHer hansi bir probleminiz olduğunda qatılın 👉 @{SUPPORT_GROUP}\nya da kömek butonuna basın  /kömek """
        START_BUTTON = [
                [
                    InlineKeyboardButton(text="Sohbet 💫", url=f"https://t.me/lovelesslifee"),
                    InlineKeyboardButton(text="Meni Qrupa elave edin ➕", url=f"http://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
                [
                    InlineKeyboardButton(text="Sahibim ⭐", url=f"https://t.me/{OWNER_USERNAME}"),
                    InlineKeyboardButton(text="Sahibim ✨", url="https://t.me/BenimKiller"),
                ],                
                [                    
                    InlineKeyboardButton(text="Emrler 🕹️", callback_data="help_"),
                ],
                
            ]
        
        callback.edit_message_text(
            START_TEXT,
            reply_markup=InlineKeyboardMarkup(START_BUTTON)
        )
    elif callback.data == "bcd":
        B_HELP = """
`ʙᴀsɪᴄ ᴄᴏᴍᴍᴀɴᴅs :- `

/çalışdır (Sorğu, yt linki, ses dosyası ) - bu komutu kullanın ve müziğin keyfine bakın 
/ytp (sorğu) - Daha gelişmiş muzik aramak için kullanın 
/tap (Sorğu) - Bu emirler sevdiginiz musiqileri yülkeye bilirsiniz 
/axtar (sorğu) - YouTube de axtarış eder
"""
        BUTTON = [
            [
                InlineKeyboardButton(text="🗑 bağla", callback_data="close_"),
                InlineKeyboardButton(text="⬅️ Geri", callback_data="help_"),
            ],
        ]
        callback.edit_message_text(
            B_HELP,
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )
    elif callback.data == "admin":
        A_HELP = """
`Admin emrleri :-`

/dayandır - Oxunan musiqini dayandırar
/davam - dayanan musiqini devam etdirir
/kec - sıradaki musiqiye geçer 
/bitir - musiqini sonlandırır
/qatıl - asistanı qrupa elave eder


`Sudo komutlar :-`

/rmf - Dosyayı veri tabanından temizler 
/rmw - Veri tabanınından ham dosyaları temizler
/temizle - Dosyaları  temizler
/gcast - global mesaj yayınlamaq üçün 
"""
        BUTTON = [
            [
                InlineKeyboardButton(text="🗑 bağla", callback_data="close_"),
                InlineKeyboardButton(text="⬅️ Geri", callback_data="help_"),
            ],
        ]
        callback.edit_message_text(
            A_HELP,
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )
    elif callback.data == "close_":
        callback.message.delete()
