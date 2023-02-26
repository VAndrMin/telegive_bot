import logging
import os

from dotenv import load_dotenv
from telegram import Bot, Update, ChatMember
from telegram.ext import CallbackContext

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

load_dotenv()

channels = os.getenv("CHANNEL_IDS").split(',')


async def check_is_chat_member(user_id: int, chat_id: str, bot: Bot):
    chat_member = await bot.get_chat_member(user_id=user_id, chat_id=chat_id)

    return chat_member.status == ChatMember.MEMBER or chat_member.status == ChatMember.OWNER


async def check_is_member_in_all_chats(user_id: int, bot: Bot):
    for chat_id in channels:
        is_member = await check_is_chat_member(user_id, chat_id, bot)

        if not is_member:
            return False

    return True


async def start_handler(update: Update, context: CallbackContext):
    """Handle the /start command."""
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id

    logging.info(f"{chat_id}, {user_id}")

    is_member_in_all_chats = await check_is_member_in_all_chats(user_id, context.bot)

    if is_member_in_all_chats:
        message = f"Greeting, you're in"
    else:
        message = f"You joined not all channels"

    await context.bot.send_message(chat_id=chat_id, text=message)
