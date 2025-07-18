import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1 


ROWS = 3
COL = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)



    columns = []
    for _ in range(cols):
         column = []
         current_symbols = all_symbols[:]
         for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)

         columns.append(column)

    return columns


    def print_slot_machine(columns):
        for row in range(len(column[0])):
            for i, column in enumerate(columns):
                if i != len(columns) - 1:
                    print(column[row], "|")
                else:
                    print(column[row])
                                





def deposit():
    while True:
        amount = input("enter the number of dollars you wanna add $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Enter a number bigger than 0")
        else:
            print("please enter a number")

    return amount 


def get_number_of_lines():
    while True:
        lines = input("Enter the the number of lines you wanna bet on (1- " + str(MAX_LINES)  + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number")
        else:
            print("please enter a number")

    return lines   



def get_bet():
    while True:
        amount = input("How much you wanna bet")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print("Amount must be between 1 and 100")
        else:
            print("please enter a number")

    return amount 





def main():
    balance = deposit()
    lines = get_number_of_lines()
    
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You dont havbe enough money to bet that much, your current balance is: ${balance}")

        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")




main()            

   