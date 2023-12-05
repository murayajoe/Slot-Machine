MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

# collect user input that gets deposit from the user
def deposit():
    while True:
        amount = input("How much do you want to deposit? ")
        # check if they entered a valid number
        if amount.isdigit():
            # then convert to a num
            amount = int(amount)

            if amount > 0:
                break
            else:
                print("Amount must be greater than 0!")
        else:
            print("Please enter a number!")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a Valid Number of lines ")
        else:
            print("Please enter a number!")

    return lines

def get_bet():
    while True:
        amount = input("How much do you want to bet on each line $? ")
        # check if they entered a valid number
        if amount.isdigit():
            # then convert to a num
            amount = int(amount)

            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET}-${MAX_BET}.")

        else:
            print("Please enter a number!")

    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    total_bet = bet * lines
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

main()
