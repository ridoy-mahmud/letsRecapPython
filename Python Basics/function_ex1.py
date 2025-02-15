def defineName (*name):
    print(f"My name is {name[2]}")

defineName("Mike","Abul","Sub")

#ex2
def my_function(name3 , name1, name2):
    print(name1,name2,name3)

my_function(name1 = "Mike", name2 = "Monica", name3 = "John")


#Print with the key of the function
def my_function2(**name):
    print("Name is "+ name["lname"])

my_function2(fname = "Mike", lname = "Monica")