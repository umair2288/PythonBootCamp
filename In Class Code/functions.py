#functions
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