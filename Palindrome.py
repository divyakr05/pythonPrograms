strInput = input("Enter input:")
length = len(strInput)
max = int(length/2)
isPalindrome = False

for i in range(0,max) :
    if strInput[i]== strInput[length-i-1]:
        isPalindrome = True
    else:
        isPalindrome = False

if isPalindrome==True:
    print("palindrome") 
else:
    print("not palindrome")    