# List in python
# List store multiple data 
myList = ["Praty", "Rishi" , "Adi"]
# Tuple store multiple data
myTuple = ("Praty", "Rishi" , "Adi")
# Set store multiple data
mySet = {"Praty", "Rishi" , "Adi"}
# Dictionary stores multiple data in key value pair
myDict = {"name" : "Shreya", "email" : "shreya16@gmail.com", "name" : "Shreya"}

# To check the data type of all above data set
print("List: ", type(myList), "Tuple: ", type(myTuple), "Set: ",type(mySet), "Dictionary: ", type(myDict))

# how to identify list, set, tuple, dictionary
# List -> [], Tuple -> (), Set -> {}, Dictionary -> {:}

#access data from data set
print("List: ", myList[0], "Tuple: ", myTuple[0], "Dictionary: ", myDict["name"])

#access complete data from data set
for data in myList:
    print("List: ", data)
for value in myTuple:
    print("Tuple: ", value)
for item in mySet:
    print("Set: ", item)
for x in myDict.values():
    print("Dictionary: ",x)

# Add new value in data set    

myList.append("Shreya")      # List can contain duplicate items
print(myList)

#myTuple.append("Shreya")
#print(myTuple)

mySet.add("Shreya")
print(mySet)

myDict.update({"name":"Nupur"})
print(myDict)


#to update data in all data set
myList[0] = "Nupur"
print(myList)

myDict["name"] = "Nupur"
print(myDict)

# mySet[0] = "Nupur"   #updation is not possible in set bcoz Set is unordered
# print(mySet)

# myTuple[0] = "Nupur"
# print(myTuple)

#To remove data from data set
myDict.pop("name")
myList.pop(0)
mySet.remove("Shreya")
print(" after removing-----------------------------------------")

print(myList)
print(mySet)
print(myTuple)
print(myDict)


# Convert Tuple to list
convertList = list(myTuple)
print(type(convertList))

convertList.append("Neha")
print(convertList)
convertList.remove("Neha")
print(convertList)
myTuple = convertList
print(myTuple)