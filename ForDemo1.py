status = False
names =["python", "java", "c#", "selenium"]
print(names)
for name in names:
    if(name=="c#"):
        status = True
    else:
        print("no match found")    
if status:
    print("!!Found the match!!")        

print("********************")
num1 = input("Enter num1:")
num1 = int(num1)
num2 = input("Enter num1:")
num2 = int(num2)
sum = num1+num2
print("Sum is: ",sum)