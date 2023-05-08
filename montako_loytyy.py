"""
How many numbers?

Program asks the user to input the amount of how many numbers the user wants
to process and then the numbers to be processed. After inputting the numbers
to be processed, the program asks the user to input a number to be found. If
number is found from the list, program prints how many times the number has
occurred and if it doesn't occur at all, program prints that the number wasn't
among the input numbers.

Writer of the program: EILeh

"""


def input_to_list():
    """
    Function asks how many number does the user process and then asks to
    enter that many numbers. Function input_to_list also calls function
    searched_number.
    """

    numbers = []
    valid_number = True

    amount_of_number = int(input("How many numbers do you want to process: "))
    print(f"Enter {amount_of_number} numbers:")

    while amount_of_number > len(numbers):
        input_number = int(input())

        if input_number:
            numbers.append(input_number)

        else:
            valid_number = False

    searched_number(numbers)


def searched_number(numbers):
    """
    Function goes through the list that has been formed in function
    input_to_list and checks how many times searched number appears in the list.
    :param numbers: saves the length of the list
    """
    searched = int(input("Enter the number to be searched: "))

    amount_of_numbers = numbers.count(searched)

    if amount_of_numbers > 0:
        print(f"{searched} shows up {amount_of_numbers} times among the "
              f"numbers you have entered.")

    else:
        print(f"{searched} is not among the numbers you have entered.")


def main():

    input_to_list()

if __name__ == "__main__":
    main()