import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")
VIP_LINK = os.environ.get("VIP_LINK", "https://t.me/+TonLienVIP")
WAVE_NUMBER = os.environ.get("WAVE_NUMBER", "07 00 00 00 00")
PRIX = 500

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton(f"J'ai payé {PRIX}F sur Wave ✅", callback_data="paid")]]
    text = f"Bienvenue sur Labo225 VIP 👑\n\nPour accéder au groupe VIP :\n\n1️⃣ Envoie {PRIX}F sur Wave : {WAVE_NUMBER}\n2️⃣ Clique sur le bouton ci-dessous\n3️⃣ Envoie la capture du paiement"
    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(f"Parfait ! Envoie la capture de ton paiement Wave {PRIX}F.\nAprès vérif, tape /vip pour avoir ton lien : {VIP_LINK}")

async def vip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Voici ton accès VIP 👇\n{VIP_LINK}")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("vip", vip))
app.add_handler(CallbackQueryHandler(button))
print("Bot Labo225 VIP démarré...")
app.run_polling()
