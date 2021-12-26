print('multiplication table')

#   Write a program to print multiplication table of a given number

num = int(input('Please enter a number'))
value = 0

for i in range(11):

#   I am creating a loop with all the numbers that lead up to 11 (not including)
#   The function shall occur 10 times and stop when it reaches 11

    print(num*i)
#   I am printing the number input of the user by the current range value