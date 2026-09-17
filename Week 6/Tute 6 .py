#17 September Thuesday tute 6
#functions, void, retunr, hints, documentation,
#input valdiation, modules, recursion, scope of varible


def Function1():
    ...
    #The dots do nothing but keep indentation and prevent error, pass can also be used
    print("This is function one") 
Function1()
#The above triggers the function
#void function dosnt send a value back
#return function returns a value and needs to store or print it
def Function2():
    #This is a void function, these are the defualt 
    return None
#return in a code is used to make it so after the code is run it prints something
def Function3():
    return "3"
#scopes are things like global and local, local things exist in a function and global allow other varibles to be upadted 

#how something exists. Note the design has a vertical line between int and float. This thing is bricked 
#def Addidtion(number1: int float = 0, number2: int float = 0):
    #total = float int = number1 + number2
    #return float
#print(Addidtion(Number1 = 4, 3))

#The following is a refined attempt of above but is bricked as total dosnt want to be acknoeldegd 
#total = 0
#def math(*numbers):
    #for number in range(len(numbers)):
        #total += numbers[number]
    #return total
#print(math(1,321,4,5,431,3,41))

#soc a class, file, a function should have least amount of responbility

#appearntly i dont have calculator
#import calculator as cl
#print(cl.add_numbers(2,2))

#The following is a function format
def Input():
    input_item: str = input("enter a value")
    if input_item.isnumeric():
        return int(input_item)
    else:
        print("Enter only numeric characters")
    



