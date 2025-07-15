MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1 




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
    bet = get_bet()
    total_bet = bet * lines

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")




main()            

   