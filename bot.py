from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8769109300:AAHXPVJTPpLbZDBznpPgmkviI37W_go8tUE"

# أمر البداية
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌾 Hay Day Farming Assistant جاهز!"
    )

# أمر الأرباح
async def profit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        buy = int(context.args[0])
        sell = int(context.args[1])

        result = sell - buy

        await update.message.reply_text(
            f"💰 الربح = {result}"
        )

    except:
        await update.message.reply_text(
            "استعمل الأمر هكذا:\n/profit 50 120"
        )

# Auto Planting
async def autoplant(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌾 Automatic Planting Activated!"
    )

# Auto Harvesting
async def autoharvest(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚜 Automatic Harvesting Activated!"
    )

# تشغيل البوت
app = ApplicationBuilder().token(TOKEN).build()

# Handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("profit", profit))
app.add_handler(CommandHandler("autoplant", autoplant))
app.add_handler(CommandHandler("autoharvest", autoharvest))

print("🌾 Hay Day Bot Started...")

app.run_polling()