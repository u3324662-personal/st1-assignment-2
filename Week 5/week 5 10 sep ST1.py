#week 5 ST
#while is used to keep a loop for a boolean logic, ie:
A = 10
while A < 15:
    A = A + 1
print (A)

#example used
counter: int = 0
while counter  < 10:
    print (counter, "hello")
    counter = counter + 1
    #the above funtion can be replaced by counter += 1 

# for loops
values = (1, 2, 3, 4, 5)
for value in values:
    print (value)

#example used, note it goes for how much range there is, regarldess of limitations of varible
for counter in range(10):
    print (counter, "hello")

    #range function works like this, range(start, stop, jump by), (start, stop), (stop)
Checker = 1
input_Grade: str = input("Enter your grade") 
if input_Grade.replace(".", "").isnumeric():
    Grade = float(input_Grade)
    if 0<= Grade <= 100:
        print(Grade)
    else:
        print("Grade is out of valid range")
elif input_Grade == ("valid numeric digits"):
    print ("very funny, now do it properly")
    continue
else:
    print("enter valid numeric digits")
