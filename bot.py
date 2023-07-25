from chatterbot import Chatbot
#create a chatbot class
bot = Chatbot("JEFFO")

bot = Chatbot(
	"JEFFO",
	storage_adapter="chatterbot.storage.SQLStorageAdapter",
	database_uri="sqlite:///database.sqlite2"
	)

bot = Chatbot(
	"JEFFO",
	logic_adapters=[
	'chatterbot.logic.BestMatch',
	'chatterbot.logic.TimeLogicAdapter'],
	)

#import list trainer
from chatterbot.trainers import ListTrainer

trainer.train([
"Hi",
"HELLO"
"vipi",
"Sasa"
"Niaje",
"poa sana",
"I need your assistance regarding my order",
"please provide me with your order ID",
"i have a complaint",
"Elaborate your concern please",
"How long does it take to recieve an order depending on area of delivery"
"an order takes an hour to be processed and a day or two for delivery "
"Okay Thanks",
"No poblem have a good day!",
"Who are you?",
"i am Jeffo, and assistant designed to guide you in your online shopping",
])


response = bot.get_response("i have a complaint")
print("Bot Response:", response)


name = input("Enter your name:")
print("welcome to the Bot service")
while True:
	request = input(name+ ":")
	if request == "bye" or request == "Bye":
		print("Bot: Bye")
		break
	else:
response = bot.get_response(request)
	print("Bot:", response)
