print("Welcome to my chatbot!")
print("Type 'exit' to end the chat.\n")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hello! How are you?")
    elif user == "hi":
        print("Bot: Hi there!")
    elif user == "how are you":
        print("Bot: I am good. Thanks for asking!")
    elif user == "what is your name":
        print("Bot: My name is ChatBot.")
    elif user == "who made you":
        print("Bot: I was made by Tanu Kushwah during her AI internship.")
    elif user == "what can you do":
        print("Bot: I can reply to your messages using simple rules. I'm still learning! 😊")
    elif user == "bye":
        print("Bot: Bye! Have a nice day!")
        break
    else:
        print("Bot: Sorry, I didn’t understand that. Can you try something else?")
