################################################################################
# Imports
################################################################################
import telebot

import config

################################################################################
# Main variables
################################################################################
TOKEN = config.token

BOT = telebot.TeleBot(TOKEN)

class UserPeer:
    def __init__(
            self, user_id, helper_id, user_status, helper_status
    ):

################################################################################
# Functions
################################################################################
################################################################################
# name:        send_message
# description: Sends a message to the chat on behalf of the bot
################################################################################
def send_message(chat_id, message):
#    logging_text = "send_message: message: ".join([str(message)])
#    log_n_print(logging_text)
    BOT.send_message(chat_id, message)

################################################################################
# name:        send_message
# description: Sends a message to the chat on behalf of the bot
################################################################################
def connect_user(user_id):


################################################################################
# Handlers
################################################################################
################################################################################
# name:        message_handler(commands=['start'])
# description: 
################################################################################
@BOT.message_handler(commands=['start'])
def start_handler(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    send_message(chat_id, 'Привет')
    connect_user(user_id)

################################################################################
# name:        message_handler(content_types=['text'])
# description: 
################################################################################
@BOT.message_handler(content_types=['text'])
def text_handler(message):
    chat_id = message.chat.id
    text = message.text.lower()
    user_id = message.from_user.id
    username = message.from_user.username
    print(text)

################################################################################
# Main
################################################################################
def main():
    BOT.polling()

if __name__ == "__main__":
    main()

