#  Write a program that asks the user to enter a positive integer
# and then prints out all the factors of that integer.


number = int(input("Please enter a number : ")) 

divisor = 1
while divisor <= number:
    if number % divisor == 0:
        print(divisor)
    divisor += 1
