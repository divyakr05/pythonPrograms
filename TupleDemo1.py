tupl = (1,"python",0.90,True,1,1,1,2,2,2,2)
print(tupl)
print(tupl[1])
print(tupl[-1])
print(tupl.count(1)) #internally python considers True as 1
print(tupl.count(2))
print(tupl.index(0.90))
print(tupl[1:5])

print("*********************")
print(type(tupl))
"""tupl[0]="divya" #tuple is immutable
print(tupl)"""

#convert tuple into list
l1 = list(tupl)
print(l1)
print(type(l1))

#convert tuple tuple into set
set1 = set(tupl)
print(type(set1))
print(set1)

#unpack tuple
tup2 = ("divya","qa","automation")
x,y,z=tup2
print(x)
print(y)
print(z)