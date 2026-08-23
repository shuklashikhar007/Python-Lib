# exception handling
# try except ( same as try/catch in javascript )
try:
    a = 10
    b = 0
    print(a / b)
except:
    print("Something went wrong")
# else with try 
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Error")
else:
    print("Result:", x)
# finally keyword
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Error")
finally:
    print("This always executes")
with open("data.txt","w") as file:
    file.write("Shikhar Shukla ki file")
    # write mode overwrites everything
    # so instead we can use append mode here
with open("data.txt","a") as file:
    file.write("College IIT BHU , Branch Chemical Engineering")
with open("data.txt", "r") as f:
    content = f.read()
# rb -> read binary
# wb -> write binary 
# both above are used for images purpose 

