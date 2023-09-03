mySet = {90,65,23,88,93,93}
print(mySet)
#add - adds value at random places
mySet.add(85)
print(mySet)
#remove - remove specific element
mySet.remove(65)
print(mySet)
#discard - removes element if present, will not throw error if the element doesnot exist
mySet.discard(80)
print(mySet)
#pop - removes random element
mySet.pop()
print("Set after pop: ",mySet)
#copy
mySet2 = mySet.copy()
print(mySet2)
#clear
mySet.clear()
print(mySet)
print("*********************************")
#set from list
set1 = set(["python",12.90,1,2,3,4])
print(set1)
#set from tuple
set2 = set(("python",12.90,1,2,3,4))
print(set2)

set3 = set1.copy()
print(set3)