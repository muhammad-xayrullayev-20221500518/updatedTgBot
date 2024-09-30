from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext
from telegram.ext import MessageHandler, filters
from telegram.ext import CommandHandler
from telegram.ext import Updater
from telegram.ext import MessageHandler, filters, CallbackContext

class AnonymousForwardBot:

    def __init__(self):
        self.your_user_id =  
        self.friend_responses = {'Вика': 'Привет, милашка Вика! Ну что, счет 4/5?)) Ну готовься)))',
                                 'Алиса': 'Привет! Ты что вчера обиделась? Ну не обижайся, тебе улыбка больше к лицу)',
                                 'Елена': 'Здравствуй, моя подруга Елена!'}
        # Add more friends and responses as needed

    def start(self, update: Update, context: CallbackContext) -> None:
        update.message.reply_text('This is the property of "feigned madness of Hamlet". The bot is activated, send the anonymous message. Тапни на /help комманду')

    def help_command(self, update: Update, context: CallbackContext) -> None:
        update.message.reply_text('Send me a message, and I will forward it anonymously/Отправь коммент!')

    def forward_message_to_user(self, update: Update, context: CallbackContext) -> None:
        message = update.message
        chat_id = message.chat_id
        incoming_text = message.text

        # Check for friend's name in the message
        for friend_name, response in self.friend_responses.items():
            if friend_name.lower() in incoming_text.lower():
                # If friend's name is mentioned, customize the response
                message.reply_text(response)
                return  # Exit the loop and function

        # If friend's name is not found, forward the message and reply as usual
        self.forward_message(message)
        message.reply_text('Your message has been received anonymously and forwarded./ Все сделано!')

    def forward_message(self, message):
        # Forward the message to the specified user
        forward_message = message.forward(chat_id=self.your_user_id)

    def main(self) -> None:
        updater = Updater("6465671510:AAGD3eIkFWDit4zzhGztsuOTHEgAV8noWDw")  # Replace with your bot token
        dispatcher = updater.dispatcher

        # Define command handlers
        dispatcher.add_handler(CommandHandler("start", self.start))
        dispatcher.add_handler(CommandHandler("help", self.help_command))

        # Define message handler
        dispatcher.add_handler(MessageHandler(filters.text & ~filters.command, self.forward_message_to_user))

        # Start the Bot
        updater.start_polling()

        updater.idle()


if __name__ == '__main__':
    bot = AnonymousForwardBot()
    bot.main()
