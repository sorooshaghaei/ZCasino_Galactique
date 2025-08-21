# bank.py
def deposit(player, amount):
    if amount <= 0:
        print("Invalid deposit amount!")
        return
    player.balance += amount
    player.add_history({"type": "deposit", "amount": amount, "balance": player.balance})
    print(f"You deposited {amount}. New balance: {player.balance}.")


def withdraw(player, amount):
    if amount <= 0:
        print("Invalid withdrawal amount!")
        return
    if amount > player.balance:
        print("Insufficient funds!")
        return
    player.balance -= amount
    player.add_history(
        {"type": "withdrawal", "amount": amount, "balance": player.balance}
    )
    print(f"You withdrew {amount}. New balance: {player.balance}.")
