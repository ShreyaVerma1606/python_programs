name = input("Enter your name: ")
for x in name:
  print(x)

# print 1 to 10 using for loop
# for(int i=1; i<11; i++)
for x in range(1,11):
 print(x)

# WAP to create table of any no.
tableno = int(input("Enter no. to create table"))
for a in range(1,11):
  print((a * tableno))

#WAP to print even no. from 1 to 10 using for loop
for e in range(1,11):
  if e % 2 == 0:
    print(e)  

#print this pattern -> 1 4 7 10 13
for p in range(1,14,3):
  print(p)

#print this  pattern -> 1 3 7 11 13 15
for b in range(1,16,2):
  if b == 5 or b ==9:
    continue     #to skip the current iteration
  else: 
     print(b)
#conditional statement will check condition is true or not
#to check the condition we use if else

#WAP to check user eligible for voting
userAge=int(input("Enter your age: "))
#note the default input function return type is string
# for vote the age must be greater than 18
if userAge  > 18:
     print("you're elligible for voting")
else:
     print("you're not elligible for voting")

#to check user is male or female
gen=input("enter your gender:")
if gen == "M":
       print("u are not elligible to sit in first compartment of metro")
elif gen == "F":
       print("you are elligible to sit in first compartment of metro")
else:
     print("You can sit in any compartment")    

#WAP if gender is female and age is greater than 18 -> govt job apply
# else male and age is greater than 18 -> private job apply        
 
gender=input("Enter your gender: ")
age=int(input("Enter your age: "))
if age > 18: 
   if gender == "Female": 
     print("You can apply for govt job")
   elif gender == "Male":
     print("You can apply for private job")
   else:
     print("Sorry there is no opening")  
else:
  print("You are under age")