from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import asyncio

# Bot token from BotFather
BOT_TOKEN = "7851660861:AAGx_p5einpLcEuXJPzXWWtFPRToMBEaqSU"

# Import mood detection and reply generation from your combined file
from enhanced_mood_detector import MoodDetector, ReplyGenerator

# Initialize AI components
mood_detector = MoodDetector()
reply_generator = ReplyGenerator()

# Conversation history per user (chat_id)
user_histories = {}

# Maximum memory length (messages per user)
MAX_HISTORY = 5

# Handle /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Hello! I'm Smart Sales Agent Pro.\nAsk me anything about your sales issue, lead, or product!")

# Handle all incoming text messages
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_text = update.message.text.strip()

    # Initialize history for this user if not present
    if chat_id not in user_histories:
        user_histories[chat_id] = []

    # Add current message to user history
    user_histories[chat_id].append(user_text)

    # Keep only recent N messages
    user_histories[chat_id] = user_histories[chat_id][-MAX_HISTORY:]

    # Build conversation context
    conversation_context = "\n".join(user_histories[chat_id])

    # Detect mood
    mood_result = mood_detector.detect_mood(user_text)
    mood = mood_result["mood"]
    label = mood_result["label"]
    intensity = mood_detector.analyze_sentiment_intensity(user_text)
    category = mood_detector.get_mood_category(label)

    # Generate smart AI reply with memory
    # Generate smart AI reply with mood + intensity
    smart_reply = reply_generator.generate_reply(user_text, category, intensity)


    # Final message
    final_message = (
        f"🤖 Mood: {mood} (Intensity: {intensity})\n"
        f"💬 {smart_reply}"
    )

    await update.message.reply_text(final_message)

# Run the bot
def start_bot():
    asyncio.set_event_loop(asyncio.new_event_loop())  # ✅ Required for threads in Python 3.10+

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

    print("✅ Telegram bot is running...")
    app.run_polling()
