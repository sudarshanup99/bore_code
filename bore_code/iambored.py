import requests
import random
limit=1
api_url = 'https://api.api-ninjas.com/v1/facts?limit={}'.format(limit)
response = requests.get(api_url, headers={'X-Api-Key': 'rXqMaQNJDdKtWQQ9P8Xaqg==RC8yVdmOkqwOducC'})
def generate_random_number():
    return random.randint(1,100)
def play_number_puzzle():
    target_number = generate_random_number()
    attempts = 0

    print("Welcome to the Number Puzzle!")
    print("Try to guess the target number between 1 and 100.")

    while True:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess < target_number:
            print("Too low. Try a higher number.")
        elif user_guess > target_number:
            print("Too high. Try a lower number.")
        else:
            print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts.")
            break

x=input("Enter your status:(bored,happy,excited):")
if x=="bored":
    print("I can help you make the most of your boredom!")
    print("1. Learn a new fact")
    print("2. Solve a puzzle")
    print("3. Watch an music video")

    choice=input("Enter your choices:(1/2/3):")
    if choice=='1':
        if response.status_code == requests.codes.ok:
         print(response.text)
        else:
          print("Error:", response.status_code, response.text)

    elif choice=='2':
        print("Let's solve a puzzle!")
        play_number_puzzle()

    elif choice == "3":
        print("Great choice! Here's an music video: https://www.youtube.com/watch?v=xycd6Kgk27c&list=RDxycd6Kgk27c&start_radio=1")
    else:
        print("Invalid choice. Please choose a valid option.")

elif x == "happy":
    print("That's awesome! Keep spreading the happiness.")
elif x == "excited":
    print("Fantastic! What are you excited about?")
else:
    print("Invalid input. Please enter 'bored', 'happy', or 'excited'.")

        

    