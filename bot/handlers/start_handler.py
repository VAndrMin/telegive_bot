from telegram import Update
from telegram.ext import CallbackContext


async def start_handler(update: Update, context: CallbackContext):
    """Handle the /start command."""
    chat_id = update.effective_chat.id  # обєкт.об'єкт(або інше).елемент.
    name = update.effective_user.first_name
    user_id = update.effective_user.id
    channels = [
        ["Test channel 1", "httpst.metask_test_channel1", -1001805771484],
        ["Test channel 2", "httpst.metask_test_channel2", -1001763595562],
        ["Test channel 3", "httpst.metask_test_channel3", -1001626957248],
        ["Test channel 4", "httpst.metask_test_channel4", -1001800227165],
    ]
    print(update.message.chat.type)

    print("in start handler")

    is_all_channels_member = await check_is_all_channels_member(channels, user_id,
                                                                context.bot)  # Виклик асинхронної функції через `Await`, та данні які ми передаємо у функцію
    print(is_all_channels_member)
    if is_all_channels_member:
        message = f"Вітання {name}! Welcome to the Telegive bot. Ти підписаний а значить переміг."
        await my_send_message(chat_id, message, context.bot)
    else:
        await my_send_message(chat_id, "не підписаний на всі канали ", context.bot)


async def my_send_message(chat_id, text, bot):
    print("in send message")

    await bot.send_message(chat_id=chat_id, text=text)


async def check_is_all_channels_member(channels, user_id, bot):
    print("in check_is_chat_member")
    for channel in channels:
        chat_member = await bot.get_chat_member(chat_id=channel[2], user_id=user_id)
        is_not_chat_member = chat_member.status != "member"
        print(chat_member.status)
        if is_not_chat_member:
            print("is not chat member")
            return False
    return True
