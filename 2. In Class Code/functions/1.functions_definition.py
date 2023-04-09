# #functions
from datetime import datetime

#defintion
def greeting():
    greet =  "Good Morning"
    hour = datetime.now().hour
    if hour < 12:
        greet =  "Good Morning"
    else:
        greet = "Good Afternoon"

    print(greet)

print("Hi")  

#call
greeting()
greeting()
greeting()


# Anantomy of a function

# 1. can't start with numbers
# 2. can only contain alpha numeric & _
# 3. NAME, first_name


def say_hello():
    print("Hello!")


say_hello()
