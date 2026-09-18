import os
import threading
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")
VIP_LINK = os.environ.get("VIP_LINK", "https://t.me/")
WAVE_NUMBER = os.environ.get("WAVE_NUMBER", "0777877044")
PRIX = 500

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton(f"J'ai payé {PRIX}F", callback_data='paid')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    text = f"Bienvenue sur Labo225 VIP 👑\n\nPour avoir accès, envoie {PRIX}F sur Wave: {WAVE_NUMBER}\nPuis clique sur le bouton ci-dessous."
    await update.message.reply_text(text, reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(f"Parfait ! Envoie la capture de paiement ici et tu auras le lien VIP.")

async def vip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Voici ton lien VIP: {VIP_LINK}")

# --- PARTIE WEB POUR RENDER GRATUIT ---
web_app = Flask(__name__)
@web_app.route('/')
def home():
    return "Bot Labo225 en ligne 24h/24 !"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    web_app.run(host='0.0.0.0', port=port)

# --- LANCEMENT DU BOT ---
app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("vip", vip))
app.add_handler(CallbackQueryHandler(button))

if __name__ == "__main__":
    threading.Thread(target=run_web).start()
    app.run_polling()
