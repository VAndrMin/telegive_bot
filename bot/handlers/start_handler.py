from telegram import Update
from telegram.ext import CallbackContext


async def start_handler(update: Update, context: CallbackContext):
    """Handle the /start command."""
    chat_id = update.effective_chat.id                       #обєкт.об'єкт(або інше).елемент.
    name = update.effective_user.first_name
    user_id = update.effective_user.id
    channel_chat_id = -1001805771484
    print(update.message.chat.type)

    message = f"Вітання {name}! Welcome to the Telegive bot. Ти живий а значить переміг."
    print("in start handler")

    await check_is_chat_member(channel_chat_id, user_id, context.bot)                 #Виклик асинхронної функції через `Await`, та данні які ми передаємо у функцію

    await my_send_message(chat_id, message,context.bot)

async def my_send_message(chat_id, text, bot):                                        #Тіло асинхронної функції яку можна викликати
    print("in send message")

    await bot.send_message(chat_id=chat_id, text=text)


async def check_is_chat_member(chat_id, user_id, bot):
    print("in check_is_chat_member")
    chat_member = await bot.get_chat_member(chat_id, user_id)
    is_chat_member = chat_member.status == "member"
    print(is_chat_member)
