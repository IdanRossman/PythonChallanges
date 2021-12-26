print('Count the total number of digits in a number')

#   Write a program to count the total number of digits in a number using a while loop.
#   For example, the number is 75869, so the output should be 5.

num = int(input('Please enter a natural number (positive and without a decimal point)'))
digits = 1

#   numbers must be natural, so if a number is smaller then 10, it must only have 1 digit

if num <= 0:
    print('are you dumb? i told u a natural number! run me again and enter a natural number')

elif num<10:
    print(digits)

while num >= 10:
    digits += 1
    num = num/10
    continue

print('There are ' + str(digits) + ' digits in the number you entered')