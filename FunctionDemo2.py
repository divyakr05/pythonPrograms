#args will receive values as tuple
def print_names(*args):
    print(args)

print_names("java","python","c","c#")

print("********************")

#using in built sum
def print_sum(*args):
    print(sum(args))

#using in built max
def print_max(*args):
    print(max(args))    

#using in built min
def print_min(*args):
    print(min(args))   

print_sum(5,10,15,20)
print_max(5,10,15,20)
print_min(5,10,15,20)