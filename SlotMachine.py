# Global Constant 
MAX_LINES = 3
MAX_BET = 500
MIN_BET = 1

# Function "deposit" 
def deposit ():
    while True:             # This a while loop so it will continur to run until "break".
        amount = input ("What would you like to deposit? £")
        if amount.isdigit():              # Check the input is a number. 
            amount = int(amount)          # Convert to integer.
            if amount > 0:                # Check if the input is greater then 0. 
                break                     # While loops break here. 
            else:
                print("Amount must be greater than 0.")
        else: 
            print("Please enter a number.")

    return amount         # If the while loop breaks with required input then return amount. Otherwise, print else statement. 

def get_number_of_lines(): 
    
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ") #
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES: 
                break                     
            else:
                print("Enter a valid number of lines.")
        else: 
            print("Please enter a number.")

    return lines 

def get_bet():

    while True:             
        amount = input ("What would you like to bet on each line? £")
        if amount.isdigit():              
            amount = int(amount)          
            if MIN_BET <= amount <= MAX_BET:               
                break                    
            else:
                print(f"Amount must be between £{MIN_BET} - £{MAX_BET}.")
        else: 
            print("Please enter a number.")

    return amount

def main():
    balance = deposit() 
    lines = get_number_of_lines() 
    while True: 
        bet = get_bet()
        total_bet = bet * lines 

        if total_bet > balance:
            print(f"You do not have enough deposit to bet £{balance}.")
        else:
            break
        
    print(f"You are betting £{bet} on {lines} lines. Total bet is equal to: £{total_bet}")

main() 