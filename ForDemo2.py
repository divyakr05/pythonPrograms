name = "python"

for a in name:
    print(a)

finalMarks = 0
l1 = [15,25,35,45,5]
for n in l1:
    finalMarks = finalMarks + n
    print(finalMarks)

print("Final marks:",finalMarks)    
print("Final marks:" +str(finalMarks))    

print("**********************")

msg1 = "I love python"
msg2 = {"I love python","divya","qa"}
msg3 = {"1":"python","2":"java","3":"js","4":"c#"}
for i in msg1:
    print(i)

for i in msg2:
    print(i)

#gives only keys    
for i in msg3:
    print(i)

#gives key-value pairs     
for i in msg3.items():
    print(i)

#gives key&value separately
for i,j in msg3.items():
    print(i) 
    print(j)   

#gives only values
for i in msg3.values():
    print(i) 

print("**********************")

for i in range(1,50):
    print(i**2) 

print("**********************")

evenlist = []
oddlist =[]

for i in range(0,50):
    if i%2==0:
        evenlist.append(i)
    else:
        oddlist.append(i)    
print("Even numbers:",evenlist)
print("Odd numbers:",oddlist)
