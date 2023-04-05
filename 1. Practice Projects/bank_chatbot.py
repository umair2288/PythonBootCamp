print("Welcome to bank of Agoda!!")

customer_name = input("May I know your name? : ")
gender = input("Are you a Male or Female? : ")
age = int(input("How old are you ? :"))
amount = float(input("How much money you want to inverst with us? : "))


interest_amounts = {}

if age >= 60:
    interest_amounts["3 Months"] = ((amount * 0.15)/12) * 3
    interest_amounts["6 Months"] = ((amount * 0.18)/12) * 6
    interest_amounts["12 Months"] = ((amount * 0.18)/12) * 12
else:
    interest_amounts["3 Months"] = ((amount * 0.10)/12) * 3
    interest_amounts["6 Months"] = ((amount * 0.12)/12) * 6
    interest_amounts["12 Months"] = ((amount * 0.15)/12) * 12

if gender.lower() == "female":
    interest_amounts["24 Months"] =  ((amount * 0.20)/12) * 24

print(interest_amounts)



