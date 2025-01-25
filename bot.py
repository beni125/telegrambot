from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# توکن ربات تلگرام
TELEGRAM_TOKEN = "7231279761:AAFAFLWhjpnjAvcRiuPgD14i2YXhMw_BU1A"

# دستور /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! من یک ربات تلگرام هستم.")

# دستور /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("دستوراتی که می‌توانید استفاده کنید:\n/start - شروع ربات\n/help - راهنما")

# هندلر برای پیام‌های متنی
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.lower()  # پیام کاربر
    if "قهوه" in user_message:
        await update.message.reply_text("قهوه می‌تواند باعث افزایش انرژی و تمرکز شود. همچنین آنتی‌اکسیدان زیادی دارد!")
    else:
        await update.message.reply_text("متوجه نشدم. لطفاً سؤال دیگری بپرسید.")

# تابع اصلی برای راه‌اندازی ربات
def main():
    # ساخت اپلیکیشن
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # اضافه کردن هندلرها
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # اجرای ربات
    application.run_polling()

if __name__ == "__main__":
    main()
