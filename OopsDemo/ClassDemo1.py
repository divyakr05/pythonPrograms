class Person:
    def welcome(self):
        print("Hello python")

    def hello_world(self):
        print("Hello world")    

#does not belong to the class
def hello_java():
    print("Hello Java")        

#bound methods belong to certain class
p=Person()
p.welcome()  #or we can write Person.welcome(p), thats why the usage of self
Person.welcome(p)
p.hello_world()  
#function belong to file, not class
hello_java()    