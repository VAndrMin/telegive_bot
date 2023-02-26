import logging
import os

from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler

from handlers.start_handler import start_handler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def main() -> None:
    load_dotenv()

    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    application = ApplicationBuilder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()

    # Set up the start command handler
    application.add_handler(CommandHandler("start", start_handler))

    # Start the bot
    application.run_polling()


if __name__ == '__main__':
    main()
