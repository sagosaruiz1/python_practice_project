import random

MAX_LINES = 3 # Set the lines to MAXIMUM of 3
MAX_BET = 1000 # MAX BET $1000
MIN_BET = 1 # MIN BET $1

ROWS = 3 # SET THE ROWS TO 3
COLS = 3 # SET THE COLUMNS TO 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []

    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(lines + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols): # Slot Machine
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols): # Get random value for column
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
            
        print()



def deposit(): # Your Deopsit as well as your Balance
    while True: 
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount must be greater than 0.")
        else: 
            print("please enter a number.")
    
    return amount

def get_number_of_lines(): # Choose the number of lines you want to bet on
    while True:
        lines = input("Enter the number of lines you want to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("please enter a number")
    
    return lines

def get_bet(): # Will take the amount of $ you will bet on
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"The amount must between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number.") 
    
    return amount

def game(balance):
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough balance to bet on that amount. Your current balance is ${balance}")
        else:
            break

    print(f"You are betting on ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main(): # MY MAIN FUNCTION
    balance = deposit()
    while True:
        print(f"Current balance us ${balance}")
        spin = input("Press enter to play. (q to quit): ")
        if spin == "q":
            break
        balance += game(balance)

    print(f"You left with ${balance}.")

main() # CALL OUT FUNCTION