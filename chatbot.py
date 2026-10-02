# ============================================
# Basic Chatbot
# CodeAlpha Internship - Task 4
# ============================================

from datetime import datetime


# Display chatbot information
def show_help():
    print("\n" + "=" * 60)
    print("                    CHATBOT HELP")
    print("=" * 60)
    print("You can use the following commands:")
    print()
    print("hello       - Get a greeting")
    print("how are you - Ask how the chatbot is doing")
    print("name        - Ask the chatbot's name")
    print("time        - Display the current time")
    print("date        - Display today's date")
    print("calculate   - Perform a simple calculation")
    print("help        - Display available commands")
    print("bye         - Exit the chatbot")
    print("=" * 60)


# Get current time
def get_time():
    current_time = datetime.now().strftime("%I:%M:%S %p")
    return f"The current time is {current_time}."


# Get current date
def get_date():
    current_date = datetime.now().strftime("%d-%m-%Y")
    return f"Today's date is {current_date}."


# Simple calculator
def calculate():
    print("\n" + "-" * 50)
    print("SIMPLE CALCULATOR")
    print("-" * 50)

    try:
        first_number = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ").strip()
        second_number = float(input("Enter second number: "))

        if operator == "+":
            result = first_number + second_number

        elif operator == "-":
            result = first_number - second_number

        elif operator == "*":
            result = first_number * second_number

        elif operator == "/":
            if second_number == 0:
                print("Error: Division by zero is not allowed.")
                return

            result = first_number / second_number

        else:
            print("Invalid operator. Please use +, -, *, or /.")
            return

        print(f"Result: {result:g}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")


# Process user message
def chatbot_response(user_input):

    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey", "hii"]:
        return "Hello! Nice to meet you. How can I help you?"

    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking."

    elif "your name" in user_input or user_input == "name":
        return "My name is PyBot, your Python chatbot."

    elif "what can you do" in user_input:
        return (
            "I can greet you, tell you the date and time, "
            "perform simple calculations, and answer basic questions."
        )

    elif user_input == "time" or "current time" in user_input:
        return get_time()

    elif user_input == "date" or "today's date" in user_input:
        return get_date()

    elif "thank" in user_input:
        return "You're welcome! I'm happy to help."

    elif "bye" in user_input or "exit" in user_input or "quit" in user_input:
        return "Goodbye! Have a great day!"

    elif user_input == "help":
        show_help()
        return None

    elif "who created you" in user_input:
        return "I was created as a Python internship project."

    elif "python" in user_input:
        return "Python is a popular programming language used for many applications."

    elif "internship" in user_input:
        return "This chatbot was developed as part of a CodeAlpha Python internship project."

    else:
        return (
            "I'm sorry, I don't understand that yet. "
            "Type 'help' to see what I can do."
        )


# Main chatbot program
def main():

    print("=" * 60)
    print("                  PYBOT - BASIC CHATBOT")
    print("=" * 60)

    print("\nHello! I am PyBot.")
    print("Type 'help' to see what I can do.")
    print("Type 'bye' to exit the chatbot.")

    while True:

        user_input = input("\nYou: ").strip()

        if not user_input:
            print("PyBot: Please type something.")
            continue

        response = chatbot_response(user_input)

        if response is not None:
            print(f"PyBot: {response}")

        if (
            user_input.lower()
            in ["bye", "exit", "quit"]
        ):
            break

        if user_input.lower() == "calculate":
            calculate()


# Program entry point
if __name__ == "__main__":
    main()