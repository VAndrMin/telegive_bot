from telegram import Update
from telegram.ext import CallbackContext


async def start_handler(update: Update, context: CallbackContext):
    """Handle the /start command."""
    chat_id = update.effective_chat.id
    name = update.effective_user.first_name

    message = f"Hello {name}! Welcome to the Telegive bot."

    await context.bot.send_message(chat_id=chat_id, text=message)
