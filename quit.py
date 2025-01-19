# Program to stop when the user enters 'quit'

"""    # Program to stop when the user enters 'quit'
while True:
    user_input = input("Enter something (or type 'quit' to exit): ")
    if user_input.lower() == 'quit':
        print("Exiting the loop.")
        break  # Exits the loop when 'quit' is entered
    print(f"You entered: {user_input}")"""


while True:
    input=input("Enter something (or type 'quit' to exit): ")
    if input.lower() == 'quit':
        print("Exiting the loop.")
        break
    print(f"You entered: {input}")
