# 1. greet the customer
# 2. ask the number passengers
# 3. suggest suitable vehicle
#   Van has 10 seaters
#   Mini Van has 7 seaters
#   Car has 4 seaters
#   Tuk has 3 seaters
#   Bike has 1 seater

from datetime import datetime # import statement


messsage = "Welcome to RIDE-ME"
print(messsage)

customer_name = input("Please enter your name : ")


hour = datetime.now().hour

if hour < 12:
    greet = "Good Morning"
elif hour  < 18 : 
    greet = "Good Afternoon"
else:
    greet = "Good Evening"


print(greet + " " + customer_name)

number_of_passengers = input("How many people are there to travel? ")
number_of_passengers = int(number_of_passengers) # type casting


if number_of_passengers <= 10:
    print("1. You can choose Van which has 10 seaters")
    if number_of_passengers <= 7 :
        print("2. You can choose Mini Van which has 7 seaters")
        if number_of_passengers <= 4:
            print("3. You can choose Car which has 4 seaters")
            if number_of_passengers <= 3:
                print("4. You can choose Tuk which has 3 seaters")
                if number_of_passengers == 1:
                    print("5. You can choose Bike which has 1 seaters")

    option = input("Please provide your option : ")

    if option == "1":
        print("Thank for booking a the van")
    elif option == "2":
        print("Thank for booking a the Mini van")
    elif option == "3":
        print("Thank for booking a the Car")
    elif option == "4":
        print("Thank for booking a the Tuk")
    elif option == "5":
        print("Thank for booking a the Bike")
else:
    print(f"Sorry , We don't have a vehicle for {number_of_passengers} passengers, Please book multiple vehciles")











