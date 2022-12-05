import time
from revChatGPT.revChatGPT import Chatbot
import json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Get your config in JSON
config = {
        "Authorization": "<Your Bearer Token Here>", # This is optional, leave this blank
        "session_token": "<Your Session Token Here>" # https://github.com/acheong08/ChatGPT - get your session token by following the instructions here
}

chatbot = Chatbot(config, conversation_id=None)
chatbot.reset_chat() # Forgets conversation
chatbot.refresh_session() # Uses the session_token to get a new bearer token
#resp = chatbot.get_chat_response(prompt) # Sends a request to the API and returns the response by OpenAI
#resp['message'] # The message sent by the response
#resp['conversation_id'] # The current conversation id
#resp['parent_id'] # The ID of the response

# Define a function that will be called when the /sum command is received.
def chat_gpt(update, context):
    # Get the user's input.
    input_str = update.message.text[5:]

    response = chatbot.get_chat_response(input_str)

    # Send the result back to the user.
    result = "chatGPT response to the following query \n\n'" + input_str + "' is: \n\n" + response['message'] 
    context.bot.send_message(chat_id=update.effective_chat.id, text=result)

# Create an Updater object and pass in the bot's token.
updater = Updater("<Your Telegram Bot Token Here") #Make a telegram bot and receive a token by texting the 'botfather' bot on telegram

# Get the dispatcher to register handlers.
dp = updater.dispatcher

# Add a command handler for the /gpt command.
dp.add_handler(CommandHandler("gpt", chat_gpt))

# Start the Bot.
updater.start_polling()

# Run the bot until you press Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT. This should be used most of the time, since
# start_polling() is non-blocking and will stop the bot gracefully.
updater.idle()
