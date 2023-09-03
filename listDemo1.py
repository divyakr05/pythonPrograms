#add two numbers
'''My first python program'''
a=b=c=500
print(a,b,c)
p = "Hello"
q = "Divya"
r = "How are you?"
print(p+" "+q+" "+r)
number1 = 9
number2 = 5
dev_name = 'divya'
print(type(dev_name))
result = number1 - number2
print(result)
print(type(result))
print(dev_name)
x = 99
print(type(x))
print(str(x))
print(type(str(x)))
#list
languages = ["java","python","cpp"]
print(languages[1])
print(languages)
#list with different data types and dup elements
list1 = ["hello","divya",123,5.55,123,"divya"]
print(list1)
#python allows negative indexing
print(list1[-1])
#slicing of list
print(list1[2:4])
print(list1[1:5])
print(list1[:])
#append - list is mutable
list1.append(32)
print("List after append:",list1)
#extend
list2 = ["dkr","1","10.10"]
list1.extend(list2)
print("List after extend:",list1)
#insert
list1.insert(1,"new")
print(list1)
#deleting an item by index
del list1[2]
print("List after deleting an element:",list1)
#pop - remove last element or by index
list1.pop(1)
print("List after pop:",list1)
#remove - remove 1st occurrence of particular element
list1.remove(123)
print("List after removing an element",list1)
print("Length of list:",len(list1))
print('new' in list1) #returns true if present 
for s in list1:
    print("-->",s,"\n")
numbers = []
for n in range(1,6):
    numbers.append(n**2)
print(numbers)
