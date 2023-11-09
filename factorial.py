#!/usr/bin/env python3

# Created by: Lily Carroll
# Created on: Nov/3/2023
# This program will calculate the factorial of the number entered by the user.


def main():
    # Setting my variables equal to 1.
    factorial = 1
    counter = 1

    # Explaining my program to the user.
    print("My program will calculate the factorial of the integer that is inputted.")

    # Getting user input for my variable.
    user_number_as_string = input("Enter a positive integer: ")

    # Initiating Try Catch.
    try:
        user_number_as_integer = int(user_number_as_string)

        # If statement for if integer is a negative.
        if user_number_as_integer < 0:
            print(
                "The integer {} is not a positive number.".format(
                    user_number_as_integer
                )
            )
        # Else statement to run loop.
        else:
            # Initiating do while loop.
            while True:
                # Multiply the factorial by the counter.
                factorial = factorial * counter

                # Increment the counter by 1 each time.
                counter = counter + 1

                # Display to the user the times tracking through the loop.
                print("Tracking {} times through the loop.".format(counter))

                # If statement to run the loop.
                if counter > user_number_as_integer:
                    # If the counter is greater than the user input, then stop the loop.
                    break

            # Displaying the factorial of the user's integer back to them.
            print(
                "The factorial of your number {}, is {}.".format(
                    user_number_as_integer, factorial
                )
            )

    # Catching any errors.
    except:
        print("Invalid input.")


if __name__ == "__main__":
    main()
