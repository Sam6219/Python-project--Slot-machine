# Slot Machine Project

This project is a simple command-line based slot machine game written in Python. The user can deposit money, choose the number of lines to bet on, and place bets within a specified range.

## Features

- **Deposit Money**: The user is prompted to deposit money which will be used for placing bets.
- **Select Number of Lines**: The user can choose to bet on up to 3 lines.
- **Place Bets**: The user can place bets on each line within a minimum and maximum bet range.
- **Validation**: The program includes input validation to ensure only valid numbers are entered for deposits, number of lines, and bets.

## Global Constants

- `MAX_LINES`: Maximum number of lines on which the user can bet.
- `MAX_BET`: Maximum amount the user can bet on each line.
- `MIN_BET`: Minimum amount the user can bet on each line.

## How It Works

1. **Deposit**: The user is asked to input an amount to deposit. The input must be a positive number.
2. **Choose Lines**: The user selects the number of lines to bet on, between 1 and the maximum number of lines (`MAX_LINES`).
3. **Place Bet**: The user inputs the amount to bet on each line. The bet must be within the range of `MIN_BET` and `MAX_BET`.
4. **Total Bet Calculation**: The total bet is calculated by multiplying the bet per line by the number of lines chosen.
5. **Check Balance**: The total bet is checked against the user’s balance to ensure they have enough funds to cover the bet.
6. **Bet Confirmation**: If the user has sufficient funds, the bet is confirmed and the details are displayed.

## Running the Program

To run the slot machine program, follow these steps:

1. Ensure you have Python installed on your system.
2. Save the slot machine script (`slot_machine.py`) to your local machine.
3. Open a terminal or command prompt.
4. Navigate to the directory where the script is saved.
5. Execute the script using the command:
    ```sh
    python slot_machine.py
    ```

## Example Usage

1. Start the program.
2. When prompted, enter the amount to deposit.
3. Enter the number of lines to bet on (1-3).
4. Enter the amount to bet on each line.
5. The program will calculate the total bet and check it against your balance.
6. If the bet is valid, the details of the bet will be displayed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

