x = 1

while x<4:
    print(x)
    x=x+1

print("***********************")

x=12345

reverse = str(x)[::-1]
print(reverse)

print("***********************")

x=12345
sum=0
while x!=0:
    n = x%10
    sum = sum*10 + n
    x = int(x/10)

print(sum)