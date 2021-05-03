# Jeffrey Stockman
# This program will output a list of Armstrong numbers and a total count based
# on user input. Only integer input is allowed in the range of [10-100,000,000];
# else an error and re-prompt will appear.
# Extra Credit attempted for non-integer input.
# BigO notation is O(N log(N)); The calculate_armstrong is O(1) for digit_count
# and sum, and O(logN) for power; iterating over a range of numbers is O(N).
# Time spent programming = 12 hours.
# No bugs detected.


# function verifies 1) an integer is entered and 2) range between 10 and
# 100,000,000; re-prompt if invalid input
def verify_int():
    user_input = input('Please enter an integer from 10 through 100,000,000 '
                       '(without the commas):')
    try:
        user_num = int(user_input)
    except ValueError:
        print('You entered a non-integer value.  Please try again.')
        return (verify_int())
    if user_num < 10:
        print('Your integer must be 10 or more.')
        return (verify_int())
    if user_num > 100000000:
        print('Your integer must be less than 100,000,000:')
        return (verify_int())
    else:
        return (user_num)


# function calculates and prints Armstrong Numbers from a list, prints a count.
def calculate_armstrong():
    total_count = 0
    for x in num_list:
        # count number of digits in integer
        digit = int(x)
        digit_count = 0
        while digit > 0:
            digit_count += 1
            digit = digit // 10

        # powers each digit by digit count, sums total
        string = str(x)
        sum = 0
        for y in string:
            sum += int(y)**digit_count

        # compare sum to integer
        if sum == x:
            print(x)
            total_count += 1

    print('\nThe total number of Armstrong numbers found was', total_count)

# initial prompt
print('Welcome to the Armstrong number calculator.')
user_input = verify_int()

# create list of integers based on user input
num_list = []
start, end = 10, user_input + 1
num_list.extend(range(start, end))

print('\nThe Armstrong numbers from 10 through 100000000 are:\n')
calculate_armstrong()