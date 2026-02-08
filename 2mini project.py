# Rule Based Ai ChatBot


print("Namaste!,Hola!,Ciao!,Vadakam!: Rule Based ChatBot Here!!!!")
print("You can ask me a  basic question's, Type 'bye' to exit fom the bot o_o")

# Chatbot Memomry Creation [ dictinary of resposes]

responses = {
    "hello": "HI, How can I help you dear?",
    "how are you": "I am very fine, thanks to ask buddy!!!",
    "who are you": "I am smart AI chatbot",
    "motivate me": "Keep going, u are making ur future bright! My makinng mistake u learnd bro keep it up!!",
    "function kya hota he":"kuch tho  hota he google kar le :)",
}

# method to get resposend of chatbot
def getResposeBot(userQuestion):
    userQuestion= userQuestion.lower()
    for eachkey in responses:
        if eachkey in userInput :
            return responses[eachkey]
    return "I am not able to tell that yet. Main jaldi seekh lunga "

# Take user input
while True:
    userInput= input("ur question is here! ask anything:")
    reply= getResposeBot(userInput)
    print("bot Response :",reply)

    if "bye" in userInput.lower():
        break

    