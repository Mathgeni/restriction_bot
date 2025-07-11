from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from src.config import config

router = Router()


NOT_SUBSCRIBED_TEXT = """
{name}{start}рошу, подпишитесь на канал, чтобы я пропускал Ваши сообщения в чат\!
"""


@router.message(F.content_type == "text")
async def can_send_messaged(message: Message):
    print(message.from_user.username)
    if message.from_user.username in (
        "GroupAnonymousBot",
        "trubitsinamarina",
    ):
        return
    if message.chat.id != "chat_trubitsina":
        return
    chat_member = await message.bot.get_chat_member(
        chat_id=f"@{config.CHANNEL_TAG}",
        user_id=message.from_user.id
    )
    if not chat_member.status in ("member", "creator", "administrator"):
        tg_user_name = message.from_user.first_name or message.from_user.full_name or ""
        tg_username = message.from_user.username
        if not tg_username:
            name = tg_user_name
        else:
            name = f"""[{tg_user_name}](tg://resolve?domain={tg_username})"""
        text = NOT_SUBSCRIBED_TEXT.format(
            name=name,
            start="П" if not name else ", п",
            channel=config.CHANNEL_TAG,
        )
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="Подпишитесь",
                        url=f"https://t.me/{config.CHANNEL_TAG}"
                    )
                ]
            ],
        )
        await message.delete()
        await message.bot.send_message(
            chat_id=message.chat.id,
            text=text,
            parse_mode="MarkdownV2",
            reply_markup=keyboard,
        )

