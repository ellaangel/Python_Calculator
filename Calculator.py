# Function to run calculator menu

def calculator():
    while True:
        print(" ------------------- ")
        print("|     Options:      |")
        print(" ------------------- ")
        print("|      1. Add       |")
        print(" ------------------- ")
        print("|    2. Subtract    |")
        print(" ------------------- ")
        print("|    3. Multiply    |")
        print(" ------------------- ")
        print("|    4. Divide      |")
        print(" ------------------- ")
        print("|     5. Root       |")
        print(" ------------------- ")
        print("| 6. Check if prime |")
        print(" ------------------- ")
        print("|      7. Quit      |")
        print(" ------------------- ")

        user_input = input("Enter your choice: ")
        print(f"You selected: {user_input}")

        if user_input == "7":
          print("Exit...")
          break

# Prime - menu                       
        if user_input == "6":
            num1, = get_input(single=True, only_int=True)
            print(f"The {num1} is {'prime' if is_prime(num1) else 'not prime'}")
            continue

        elif user_input in ("1", "2", "3", "4", "5"):
            if user_input == "5":
                num1, = get_input(single=True)
                result = root(num1)
                print(f"The square root of {num1} is: {round(result, 2)}")
            else:
                num1, num2 = get_input()

# Add - menu
            if user_input == "1":
                result = add(num1, num2)
                print(f"The sum {num1} + {num2} is: {round(result, 2)}")
# Substract - menu
            elif user_input == "2":
                result = subtract(num1, num2)
                print(f"The sum {num1} - {num2} is: {round(result, 2)}")
# Multiply - menu      
            elif user_input == "3":
              result = multiply(num1, num2)
              print(f"The sum {num1} x {num2} is: {round(result, 2)}")

# Divide - menu   
            elif user_input == "4":
                result = divide(num1, num2)
                if result == "Cannot divide by zero (0)":
                    print(result)
                else:
                    print(f"The sum {num1} / {num2} is: {round(result, 2)}")      
            continue

# Check if user select valid number in the menu
        else:
          print(" *************************************************** ")
          print("|   Invalid selection, enter a number in the menu   |")
          print(" *************************************************** ")

# Ask to user enter the numbers, if its not a number print error 
def get_input(single=False, only_int=False):
    value1 = input("Enter a first number: ")
    while only_int and not value1.isdigit() or not is_number(value1):
        print(" *************************************************** ")
        print("             Its not a valid number!")
        print(" *************************************************** ")
        value1 = input("Enter a first number: ")
    
    if single:
        return int(value1) if only_int else float(value1),

    value2 = input("Enter a second number: ")
    while not is_number(value2):
        print(" *************************************************** ")
        print("             Its not a valid number!")
        print(" *************************************************** ")
        value2 = input("Enter a second number: ")

    return float(value1), float(value2)

# Add - Function
def add(num1, num2):
    return num1 + num2

# Substract - Function
def subtract(num1, num2):
    return num1 - num2

# Multiply - Function 
def multiply(num1, num2):
    return num1 * num2

# Divide - Function  
def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero (0)"
    return num1 / num2

# Prime - Function 
def is_prime(n):

    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Root - Function 
def root(num1):
    return num1 ** 0.5


def is_number(num_string):
    if num_string.count('.') == 1:
        without_dot = num_string.replace('.', '', 1)
        if without_dot.isdigit() or (without_dot.startswith('-') and without_dot[1:].isdigit()):
            return True
    elif num_string.startswith('-') and num_string[1:].isdigit():
        return True
    elif num_string.isdigit():
        return True
    return False

calculator()
