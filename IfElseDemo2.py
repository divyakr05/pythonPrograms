print("yes") if 5>10 else print("no")
marks = 95

print("A+") if marks>=95 else print("A")

#salary = 100001
salary = input("please enter your salary: ")
salary = int(salary)
if salary>40000:
    print("Eligible for car loan")
    if(salary>80000):
        print("Eligible for home loan")
        if(salary>100000):
            print("premium customer-Eligible for all kind of loan")
else:
    print("Sorry!!we cannot serve you")
        