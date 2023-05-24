def greet():
    print("Hello! How can I assist you today?")

def farewell():
    print("Goodbye! Have a great day.")

def assist():
    while True:
        user_input = input("> ")

        if user_input.lower() == "hello":
            greet()
        elif user_input.lower() == "bye":
            farewell()
            break
        else:
            print("I'm sorry, I didn't understand that. Can you please rephrase or ask a different question?")

assist()
