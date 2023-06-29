import sys
from pathlib import Path
pathvar = str(Path(__file__).resolve().parent.parent) + '\\'
sys.path.append(pathvar)

import logging

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    CallbackQueryHandler
)

from mafia_bot import config, handlers
from mafia_bot.db import close_db

COMMAND_HANDLERS = {
    "start": handlers.start,
    "help": handlers.help_,
    "info": handlers.info,
    "events": handlers.eventlist,
    "top": handlers.top
}

CALLBACK_QUERY_HANDLERS = {
    rf"^{config.EVENTLIST_CALLBACK_PATTERN}(\d+)$": handlers.eventlist_button,
    rf"^{config.EVENT_CALLBACK_PATTERN}(\d+)$": handlers.event_button,
    rf"^{config.EVENT_PROFILE_CALLBACK_PATTERN}(\d+)$": handlers.event_profile_button
}

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

if not config.TELEGRAM_BOT_TOKEN:
    raise ValueError(
        "BOT_TOKEN is not implemented in .env"
    )

def main():
    application = ApplicationBuilder().token(config.TELEGRAM_BOT_TOKEN).build()

    for command_name, command_haldler in COMMAND_HANDLERS.items():
        application.add_handler(CommandHandler(command_name, command_haldler))

    for pattern, handler in CALLBACK_QUERY_HANDLERS.items():
        application.add_handler(CallbackQueryHandler(handler, pattern=pattern))

    application.run_polling()


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import traceback
        logger.warning(traceback.format_exc())
    finally:
        close_db()
