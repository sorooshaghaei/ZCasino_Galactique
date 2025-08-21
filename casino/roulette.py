# roulette.py
import random


def play_roulette(player):
    print(f"\nWelcome to Roulette, {player.name}!")

    while True:
        # Check if balance is zero
        if player.balance <= 0:
            print(
                "Your balance is 0. You cannot play roulette. Please deposit first or return to the main menu."
            )
            return  # exit back to main menu

        # Ask for the bet
        bet_input = input(
            f"How much do you want to bet? Current balance: {player.balance} (or type 'exit' to go back): "
        )
        if bet_input.lower() == "exit":
            print("Returning to main menu...")
            return  # exit the game

        try:
            bet = int(bet_input)
        except ValueError:
            print("Invalid bet! Try again.")
            continue

        if bet <= 0 or bet > player.balance:
            print("Invalid bet! Try again.")
            continue

        # Ask for the number (0-6)
        try:
            number = int(input("Choose a number between 0 and 6: "))
        except ValueError:
            print("Invalid number! Try again.")
            continue
        if number < 0 or number > 6:
            print("Invalid number! Try again.")
            continue

        # Generate random result (0-6)
        result = random.randint(0, 6)
        print(f"The result is: {result}")

        # Calculate gain/loss
        if result == number:
            gain = bet * 6  # payout for correct number
            player.balance += gain
            print(
                f"Congratulations {player.name}, you won {gain}! New balance: {player.balance}."
            )
        else:
            gain = -bet
            player.balance += gain
            print(
                f"Sorry {player.name}, you lost {bet}! New balance: {player.balance}."
            )

        # Add to history
        player.add_history(
            {
                "game": "roulette",
                "bet": bet,
                "choice": number,
                "result": result,
                "gain": gain,
                "final_balance": player.balance,
            }
        )

        # Ask if the player wants to play again
        replay = input("Do you want to play again? (y/n): ")
        if replay.lower() != "y":
            break

    print("\nThank you for playing Roulette!")
