import random

# Function to generate random integer within a specified range
def minmax(min, max):
    """
    Function returns a random integer within given specified range

    - min (int): Minimum value of range given in parameter
    - max (int): Maximum value of range given in parameter

    Returns a random integer between the minimum and maximum values
    """
    return random.randint(min, max)

# Function to generate random arithmetic operator from given operators
def randomsign():
    """
    Function returns random arithmetic operator from given set {'+', '-', '*'}
    """
    return random.choice(['+', '-', '*'])

# Function to calculate the result of selected operation
def operation(num1, num2, op):
    """
    Function calculates the result of the specified arithmetic operation

    Parameters -
    - num1 (int): First operand
    - num2 (int): Second operand.
    - op (str): Arithmetic operator ('+', '-', '*')

    Returns a tuple containing the formatted arithmetic expression and the result
    """
    pholder = f"{num1} {op} {num2}"
    if op == '+': ans = num1 + num2
    elif op == '-': ans = num1 - num2
    else: ans = num1 * num2
    return pholder, ans

# Verify user input
def check_input():
    while True:
        try:
            user_input = input("Your answer: ")
            if not user_input.isdigit():
                raise ValueError("Invalid input! Please enter a valid integer.")            
            # Check for special characters
            if any(not c.isdigit() for c in user_input):
                raise ValueError("Invalid input! Special characters are not allowed.")            
            return int(user_input)
        except ValueError as e:
            print(e)

# Main function of the Math Quiz Game
def math_quiz():
    score = 0
    totalq = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    # Loop through a specified totalq
    for _ in range(totalq):
        n1 = minmax(1, 10); n2 = minmax(1, 5); o = randomsign()

        # Generate the problem and answer
        PROBLEM, ANSWER = operation(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = check_input()

        # Check user's answer and update the score
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    # Display final score to user
    print(f"\nGame over! Your score is: {score}/{totalq}")

if __name__ == "__main__":
    math_quiz()