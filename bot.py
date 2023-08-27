import logging
from telegram.ext import Updater, CommandHandler
from pydub import AudioSegment
from pydub.playback import play

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define the /start command handler
def start(update, context):
    audio_url = "https://stream01048.westreamradio.com/wsm-am-mp3"
    audio = AudioSegment.from_mp3(audio_url)
    play(audio)

# Define the /stop command handler
def stop(update, context):
    # Add code to stop audio playback
    pass

def main():
    # Initialize the Updater with your bot's token
    updater = Updater("6542382919:AAF0QqmLGR1GaA7aUfzgHNqgjPGLQNR-BJ4", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("stop", stop))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop
    updater.idle()

if __name__ == '__main__':
    main()
  
