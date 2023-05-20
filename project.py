import random
import cowsay
import sys

def main():
    name = input("Thank you, for visiting! May I have your name please? ")
    try:
        first, last = validate_name(name)
    except:
        sys.exit("Usage: first last")
    cowsay.dragon(f"Hello, {first}! Welcome to Dragon land!")
    input(f"{first} said, 'Thank you! I don't know why I'm here!' (press enter to continue) ")
    cowsay.dragon("That's okay! I'm here to guide you! There's a cottage over there. Let's head in!")
    choice = get_choice()
    answer = generate_game(choice)
    simulate_round(answer)
    input("You entered the next room, and saw a cat. (press enter to continue) ")
    cowsay.kitty("Hello there! ")
    input("This cat is very particular about how she's greeted, make sure you greet her back. (press enter to continue) ")
    greeting = input("Greet the cat back! (Hint: hello or hi)")
    if greeting == "hello" or greeting == "hi":
        print(f"you received {value(greeting)} coins from the cat. ")
    else:
        print("The cat was not happy with your greeting and feed you to the dragon. ")
        cowsay.dragon("Thanks for playing!!! YUUUUUMMMM!!!!")
        sys.exit()
    input("You continued to the next door and reached the backyard, where you you meet the great wizard for the first time. (press enter to continue) ")
    cowsay.beavis(f"Oh hello there, {first}! I've heard so much about you, and I would need your help now. ")
    while True:
        yesorno = input("Would you help the wizard out? (y/n) ")
        if yesorno == "y":
            break
        elif yesorno == "n":
            sys.exit("The wizard is deeply disappointed in you and feed you to the dragon. ")
    input("He gave you a list of items from his grimoire. (press enter to continue) ")
    cowsay.beavis("I need one more item to create a strength potion. Which one from this list should I pick? ")
    print("Only one of the following item will work to successfully create a strength potion: ")
    print("wolfsbane ")
    print("vervaine ")
    print("dragon's blood ")
    print("pansies ")
    print("fish oil ")
    print("moonstone ")
    print("You have 3 chances to guess the correct answer. ")
    the_game = simulate_grimoire()
    if the_game == True:
        cowsay.beavis("Thank you so much for helping me out. Make a wish before you sleep tonight and it shall be granted! 🪄")
    else:
        cowsay.beavis("You're a disappointment. ")

def validate_name(x):
    first, last = x.split(" ")
    return first, last

def get_choice():
    while True:
        choice = input("In the cottage, you met three interesting people, which one would you like to talk to? (stimpy/ tux/ cheese) ")
        if choice == "stimpy":
            cowsay.stimpy("Hi! Nice to meet you! Let's play a game!")
            cowsay.stimpy("Because you have chosen me, we'll start the easiest level of guessing game. You have 3 chances of guessing the right number. if you lose, you'll have to restart from the beginning! ")
            print("Please guess the number. It's between 0 - 5!")
            return "stimpy"
        elif choice == "tux":
            cowsay.tux("Hi! Nice to meet you! Let's play a game!")
            cowsay.tux("Because you have chosen me, we'll start the medium level of guessing game. You have 3 chances of guessing the right number. if you lose, you'll have to restart from the beginning! ")
            print("Please guess the number. It's between 0 - 10!")
            return "tux"
        elif choice == "cheese":
            cowsay.cheese("Hi! Nice to meet you! Let's play a game!")
            cowsay.cheese("Because you have chosen me, we'll start the hardest level of guessing game. You have 3 chances of guessing the right number. if you lose, you'll have to restart from the beginning! ")
            print("Please guess the number. It's between 0 - 15!")
            return "cheese"
        else:
            print("please choose one: stimpy, tux, or cheese")


def generate_game(level):
    if level == "stimpy":
        x = random.randint(0, 5)
    elif level == "tux":
        x = random.randint(0, 10)
    elif level == "cheese":
        x = random.randint(0, 15)
    return x

def simulate_round(x):
    attempts = 0
    while attempts < 3:
        response = int(input("Submit your response: "))
        if response == x:
            cowsay.dragon("That's the correct answer. Let's move on to the next room! 🪄")
            return True
        elif response > x:
            attempts += 1
            print("Not quite. Choose a smaller number!")
        elif response < x:
            attempts += 1
            print("Not quite right. Choose a larger number!")
    attempts += 1
    print("Wrong answer! The dragon ate you!! :( maybe in another life!)")

def value(greeting):
    greeting = greeting.lower().strip()
    if greeting.startswith("hello"):
        return 100
    elif greeting.startswith("hi"):
        return 50
    else:
        return 0

def simulate_grimoire():
    attempt = 0
    while attempt < 3:
        grimoire = input("Let him know the correct answer: ")
        the_answer = simulate_answer(grimoire)
        if the_answer == True:
            return True
        elif the_answer == False:
            print("Not quite")
            attempt += 1
    sys.exit("The wizard grew inpatient and feed you to the dragon. :( ")

def simulate_answer(grimoire):
    if grimoire == "dragon's blood":
        return True
    else:
        return False

if __name__ == "__main__":
    main()