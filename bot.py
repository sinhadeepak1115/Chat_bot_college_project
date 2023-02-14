# bot.py
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from cleaner import clean_corpus

CORPUS_FILE = "chat.txt"

chatbot = ChatBot("ChatBot")

trainer = ListTrainer(chatbot)
cleaned_corpus = clean_corpus(CORPUS_FILE)
trainer.train(cleaned_corpus)


exit_conditions = (":q","quit", "exit")

while True:
    qurey = input("> ")
    if qurey in exit_conditions:
        break
    else:
        print(f"{chatbot.get_response(qurey)}")
    
