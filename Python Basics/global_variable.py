def myFunc():
    global x
    x = "Inside from My Function"
myFunc()
print(f"This is from {x}")