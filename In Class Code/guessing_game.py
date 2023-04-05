from random import randint

number = randint(1,100)
guess = int(input("Guess the number : "))
count = 1

while (guess != number) and (count < 10):  
    if number > guess:
        print("Greater")
    else:
        print("Lower") 
    guess = int(input("Guess the number : "))    
    
    count += 1

if count < 10:
    print(f"Congratulations! You guessed the number in {count} chances!")
else:
    print("Sorry, You didn't guess the number")