print(r"""//      ________            ______                     _                ______                   
//     /_  __/ /_  ___     / ____/_  _____  __________(_)___  ____ _   / ____/___ _____ ___  ___ 
//      / / / __ \/ _ \   / / __/ / / / _ \/ ___/ ___/ / __ \/ __ `/  / / __/ __ `/ __ `__ \/ _ \
//     / / / / / /  __/  / /_/ / /_/ /  __(__  |__  ) / / / / /_/ /  / /_/ / /_/ / / / / / /  __/
//    /_/ /_/ /_/\___/   \____/\__,_/\___/____/____/_/_/ /_/\__, /   \____/\__,_/_/ /_/ /_/\___/ 
//                                                         /____/                                """)


import random

def gusse_number_fun():
    while True:   # 🟢 replay loop
        number = random.randint(1, 100)

        print("\nChoose difficulty:")
        print("1. Easy (10 attempts)")
        print("2. Medium (7 attempts)")
        print("3. Hard (5 attempts)")

        choice = input("Enter 1, 2, or 3: ")
        if choice == "1":
            max_attempts = 10
        elif choice == "2":
            max_attempts = 7
        elif choice == "3":
            max_attempts = 5
        else:
            print("Invalid choice! Defaulting to Medium.")
            max_attempts = 7

        attempts = 0

        while attempts < max_attempts:
            num = int(input(f"Attempt {attempts+1}/{max_attempts} - Enter your guess: "))
            attempts += 1

            if num == number:
                print(f"You won 🎉 in {attempts} tries!")
                break
            elif num > number:
                print("Too high")
            elif num < number:
                print("Too low")

            # Extra hint if close
            if abs(num - number) <= 10:
                print("🔥 You're very close!")

        else:
            print(f"Game Over 😢 The number was {number}")

        # 🟢 Replay choice
        again = input("Do you want to play again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing! 👋")
            break

# Run the game
gusse_number_fun()
