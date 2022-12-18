# Import necessary libraries
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new ChatBot instance
bot = ChatBot("Example Bot")

# Use the ChatterBotCorpusTrainer to train the chatbot
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

# Start the chatbot loop
while True:
    try:
        # Get input from the user
        user_input = input("User: ")

        # Get a response from the chatbot
        bot_response = bot.get_response(user_input)

        # Print the chatbot's response
        print("Bot: ", bot_response)
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
