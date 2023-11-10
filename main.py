while True:
    user_input = input("Please enter a command: ")

    if user_input.lower() == "hello":
        print("Hello, how can I assist you?")
    elif user_input.lower() == "goodbye":
        print("Goodbye!")
        break
    elif user_input.lower() == "how are you":
        print("I'm an AI, so I don't have feelings, but thanks for asking!")
    elif user_input.lower() == "help":
        print("I can assist you, just let me know what you need.")
    elif user_input.lower() == "what is your name":
        print("I am EnigmaScript, a large language model trained by Now AI.")
    elif user_input.lower() == "tell me a joke":
        print("Why don't scientists trust atoms? Because they make up everything!")
    elif user_input.lower() == "tell me a fact":
        print("The Eiffel Tower can be 15 cm taller during the summer due to expansion from the heat.")
    elif user_input.lower() == "thank you":
        print("You're welcome! If you need any more assistance, just let me know.")
    elif user_input.lower() == "what is the meaning of life":
        print("The meaning of life is subjective and varies for each individual.")
    elif user_input.lower() == "open website":
        print("Opening website...")  # Add code here to open a specific website
    elif user_input.lower() == "search":
        query = input("Enter your search query: ")
        print("Searching for", query)  # Add code here to perform a web search
    elif user_input.lower() == "play music":
        print("Playing music...")  # Add code here to play music
    elif user_input.lower() == "set a reminder":
        reminder = input("Enter your reminder: ")
        print("Reminder set:", reminder)  # Add code here to set a reminder
    else:
        print("Sorry, I don't understand that command. Please try again.")
