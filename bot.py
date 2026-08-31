#!/usr/bin/env python3
# bot.py - Simple Telegram bot using python-telegram-bot (v20+)
# Features: /start, /help, echo for text messages
# Requirements: pip install -r requirements.txt

import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Load environment variables from a local .env file (optional)
# Create a .env file in the project root with BOT_TOKEN=your_token and DO NOT commit it.
load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "مرحبا! أنا بوت بسيط. أرسل رسالة وسأعيدها لك (echo). استخدم /help للمزيد."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "/start - ابدأ\n/help - مساعدة\nأرسل أي نص لأرجعه لك."
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message and update.message.text:
        await update.message.reply_text(update.message.text)


def main() -> None:
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise SystemExit("Please set BOT_TOKEN environment variable or create a .env with BOT_TOKEN")

    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    logger.info("Starting bot (long polling)...")
    app.run_polling()


if __name__ == "__main__":
    main()
