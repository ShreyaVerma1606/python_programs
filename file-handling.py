#open func.will create the file
# if file does not exit,it will create one
mypassword=open("password.txt","w")

# write laptop password in the file
mypassword.write("my laptop password-hey\n") 

# take input from user
mypassword.write(input("enter the text:\n"))

#read the password from the file
mypassword=open("password.txt","r")
print(mypassword.read())

#read password from the file
mypassword=open("password.txt","r")
mydata=mypassword.read()
if "mac" in mydata:
    print("yes")
else:
    print("no")

# to close a file
mypassword.close()

# delete a file
import os
os.remove("password.txt")

# create read write delete csv ,excel,json,txt
# create csv file
myCsv=open("myfile.csv","w")
myCsv.write("hey ,tell, me, your, name")

myexcel=open("myexcel.xlsx","w")
myexcel.write("my,name,is, shreya")

