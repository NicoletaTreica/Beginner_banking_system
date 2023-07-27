import random


# Classes
# Defining a class called BankUser
# -> none: means it returns nothing
# serves as the constructor and is automatically called when a new BankUser object is created.
class BankUser:
    def __init__(
        self,
        first_name: str,
        second_name: str,
        card_number: int,
        pin: int,
        balance: float,
    ) -> None:
        self.first_name = first_name
        self.second_name = second_name
        self.card_number = card_number
        self.pin = pin
        self.balance = balance

    # next  a method called information() is defined inside the BankUser class.
    def information(self) -> None:
        print(f"First Name: {self.first_name}")
        print(f"Second Name: {self.second_name}")
        print(f"Card Number: {self.card_number}")
        print(f"Pin: {self.pin}")
        print(f"Balance: {self.balance}")

    # allow the user to deposit money into their account
    def deposit(self) -> None:
        # Adds money to an existing balance

        # 1 - Ask how much money to add
        # "while True" This starts an infinite loop that will repeatedly prompt the user
        # to enter the amount they want to deposit until a valid input is provided
        # "break" breaks the loop, must be indented right
        # if invalid value a ValueError
        while True:
            try:
                amount_to_deposit = float(
                    input("How much money would you like to deposit: ")
                )
                break
            except ValueError:
                print("Try again ")

        # Add money
        self.balance = self.balance + amount_to_deposit

        # Print new balance
        print(f"New balance is: {self.balance}")

    # allows the user to withdraw money from their bank account
    # as long as they have enough balance
    def withdraw(self) -> None:
        while True:
            try:
                amount_to_withdraw = float(
                    input("How much money would you like to withdraw: ")
                )
            except ValueError:
                print("Try again")
                continue

            if self.balance < amount_to_withdraw:
                print("insufficient funds")
                continue

            break
        self.balance = self.balance - amount_to_withdraw
        print(f"your new balance is: {self.balance}")

    # shows the current balance
    def current_balance(self) -> None:
        print(f"your balance is {self.balance}")


# Functions
def generate_password() -> str:
    choices = random.choices(
        [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ],
        k=8,
    )
    # joins the strings into one string so that it comes out as one word
    # you can you "/".join or -/-".join or "".join to join the strings
    return "".join(choices)


def options() -> None:
    print("choose one of the options below")
    print("1. deposit")
    print("2. withdraw")
    print("3. current balance")
    print("4. exit")


def main() -> None:
    # greeting
    print("Welcome, let's find out which type of bank account you will need.")

    # questions of eligibility
    # asking for age of user
    while True:
        try:
            age_of_user = int(input("Q1. How old are you: "))
        except ValueError:
            print("invalid number, please try again")
            continue
        break

    if age_of_user < 18:
        print("Oops you're too young to jump abroad.")
        return
    elif age_of_user >= 18:
        print("Perfect! Let's carry on!")
    else:
        print("You have achieved the impossible")

    # asking about occupation
    # making a set of responses and then asking if the responses are in the user input, "ok" should be printed
    while True:
        occupation_of_user = str(input("Q2. Are you a student?: "))
        positive_occupation_response = {
            "yes",
            "ya",
            "ye",
            "yaur",
            "ofcourse",
            "duh",
            "I am",
            "i am",
            "indeed",
        }
        if occupation_of_user in positive_occupation_response:
            print("You are eligible for a student account.")
            break

        # checking for "no" answers from user
        negative_occupation_response = {"no", "never", "naur", "nu", "no", "nope"}
        if occupation_of_user in negative_occupation_response:
            print("You are eligible for a standard account.")
            break
        # if it gets here then the occupation want entered correctly because it did not break
        print("invalid answer, please try again")

    username = str(input("Enter your first and last name: "))
    print(f"hello {username} let's set up your password!")

    # asking user if they would like to use their own password or a generated password
    decide = input("If you would like to have a password generated for you type 'yes'")
    if decide == "yes" or decide == "Yes":
        password = generate_password()
        print(f"Here is your generated password: {password}")
    else:
        password = input("input your password: ")
        print("Your account has now been created!")

    #
    card_holder_database = []
    card_holder_database.append(
        BankUser(
            first_name="Nicoleta",
            second_name="Treica",
            card_number=123456789,
            pin=1234,
            balance=0.00,
        )
    )
    card_holder_database.append(
        BankUser(
            first_name="Axen",
            second_name="Georget",
            card_number=987654321,
            pin=4321,
            balance=0.00,
        )
    )

    # asks for the card number and then sees if it matches the info seen in card_holder_database
    while True:
        try:
            user_information = int(input("Insert your card number: "))
        except ValueError:
            print("personal details not recognized, please try again.")
            continue

        bank_user = None
        for holder in card_holder_database:
            if holder.card_number == user_information:
                bank_user = holder
                break

        if bank_user is None:
            print("incorrect login, please try again")
            continue

        break

    bank_user.information()
    print("")
    print("welcome")
    print("")

    # calls options (the menu of 1,2,3,4)
    options()

    while True:
        choice = input("Enter your choice (1/2/3/4): ")
        if choice == "1":
            print("You have chosen to deposit your money")
            bank_user.deposit()
        elif choice == "2":
            print("You have chosen to Withdraw money")
            bank_user.withdraw()
        elif choice == "3":
            print("You have chosen to see your current balance")
            bank_user.current_balance()
        elif choice == "4":
            print("You have chosen to exit")
            print("Have a nice day!")
            break
        else:
            print("error")


# Call the main function if file is called as a script
if __name__ == "__main__":
    main()
