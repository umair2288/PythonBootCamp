# Write a program that calculates the sum of all the numbers between 1 and 1000 
# that are divisible by 3 or 5 using a while loop.


number = 1
sum_of_numbers = 0
while number <= 1000:
    if (number % 3 == 0) or (number % 5 == 0):
        sum_of_numbers += number
    number += 1

print(sum_of_numbers)

