import random
otp=random.randint(100000,999999)
user_name=input("Username:")
print("Hello..!",user_name)
print("Here's your otp for login",otp)
password=input("Enter the otp digit to login:")
if password == str(otp):
    print("Login successful")
else:
    password != str(otp)
    print("Login failed")