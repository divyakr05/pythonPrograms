emp = {"qa":"divya","dev":"geetha","devops":"siva","50":"java"}
print(emp)
print(type(emp))
print(emp["dev"])
print(emp.get("qa"))
emp1 = {"qa":["eldho","divya","shafeer"],"dev":["rakesh","govind","mary"]}
print(emp1["qa"][2])

#dict under dict
emp1 = {"qa":"divya","dev":{"frontend":"arun","backend":"joby"}}
print(emp1)
print("hey!!",emp1.get("dev").get("backend"))
emp2 = emp1["dev"]
print(emp2.get("qa"))
print(emp2)
print(emp1["dev"]["frontend"])

#add record
emp2["manager"]="christa"
print(emp2)
#remove record
emp1.pop("qa")
print(emp1)
print("****************")
#remove record(key-value pair) in lifo
emp3 = {"qa":"divya","dev":{"frontend":"arun","backend":"joby"},"manager":"shafeer"}
emp3.popitem()
print(emp3)

#del
del emp3['dev']
print(emp3)

#length
print(len(emp3))

#return keys
print(emp3.keys())

#return values
print(emp3.values())

#return key-value pairs in the form of tuples
print(emp.items())


