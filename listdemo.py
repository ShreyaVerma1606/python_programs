# list can store multiple data,data can bre different types int str
# list can store the duplicate data 
# list is an ordered data set -sorting ascending descending

# create list and store your friend name
friendlist=["praty","adeeba","rishita","aditi"]
#   print list of friend names
print(friendlist)
# add the age of your friends into list
# append will add the data at the end of the list
fru=['a','c','s']
friendlist.append(36)
friendlist.append(26)
friendlist.append(29)
friendlist.append(5)
print(friendlist)
friendlist.append(fru)
print(friendlist)

# add data into the list using index
friendlist.insert(2,"shreya")
print(friendlist)
# to access the data using index no.
print(friendlist[2])
# extend func.=puts the data of one list to the other list
friendlist.extend(fru)
print(friendlist)
# remove the data from the list
friendlist.remove('a')
print(friendlist)
# pop will delete the data usimg index
friendlist.pop(9)
print(friendlist)
# remove->removes that element from the list when we write that element in the brackets
# pop=>element is popped when the index of that element is written within brackets
# access the complete list
# print(name)
fav=['mumbai','kanpur','ghaziabad']
fav.insert(0,"kasol")
fav.pop(2)
fav.sort()
print(fav)

# add the 5 favt.city name in list
# add my favt.city in index 0
# remove the last city in list -usimg pop
# sorting the list data
# print the list data
