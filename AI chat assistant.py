
# AI STUDEY BUDDY (RULE - BASED CHAT ASSISTANT)

import datetime
import time
presentHour = datetime.datetime.now().hour
name = input("Welcome , Enter your name : ")
if 5 <= presentHour <= 11:
    print("Good Morning = " , name)
elif 11 <= presentHour <= 17:
    print("Good afternoon = " , name)
elif 17 <= presentHour <= 20:
    print("Good evening = " , name)
else:
    print("Good night = " , name)
    



import random
print("Namaste ! Welcome to your ChatBot ❤️")
print("You can ask me a question, type 'bye' to exit 😊")

# chatbot memory creation [dictionary of responses]
response = {
    "hello": ["Hi, Welcome! How can I help you sir?"],
    "how are you": [ "Doing great, thanks for asking!"],
    "who are you": ["I am a smart AI Chatbot.", "Just your friendly chatbot assistant."],
    "motivate me": ["Keep going! Every bug makes you a better developer.", "Don’t give up, progress takes time."],
    "happy": ["Great to hear that!", "Happiness looks good on you!"],
    "how was your day": ["Excellent sir, and how was yours?", "My day was wonderful, thank you!"]
}

# method to get response of chatbot
def getResponseBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachKey in response:
        if eachKey in userQuestion:
            return random.choice(response[eachKey])
    return "I am not able to tell that yet. I am still in learning mode."

# Take user input
while True:
    userInput = input("Please ask your question: ")
    reply = getResponseBot(userInput)
    print("Bot response:", reply)

    if "bye" in userInput.lower():
        print("Goodbye! Have a great day 😊")
        break

