pwd = "123@HA"
user_password = input("Type your password: ")
while user_password != pwd:
    print("Wrong password, Please try again!")
    user_password = input("Type your password: ")

print("Correct Password")