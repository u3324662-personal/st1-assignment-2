#ST week 7 TUTE 24 sep|
# ... as shown below allows the code to be shown while deactivating the print 
#data types, for each loops, 2d list, file handling, exepction, matplotlib
#lyst means list but due to list being pre-assigned
#index error is prescribed when a list part dosnt exist but is called upon 
students: list = ["alice", "bob", "fred", "dave"]
students.append("lilly")
#'lilly' is added as the last item in the list
students.insert(1, "greg")
#This adds 'greg' in the listed space, pushing all items to the right
students.remove("bob")
#This removes the first instance of 'bob'
students.pop(1)
#This removes the attribute in the attached varible, deafulting to the last one if none are given 
students.extend(["Tom", "Jane"])
#This adds the listed items to the list 
students.extend(["Tom", "Tom", "Tom"])
students.remove("Tom")
#This also removes the first instance of 'Tom'
for count in range(len(students)):
    ...
    #print(students[count], count)
#len(list) gives how many values are in a list, the above is a basic thing to count things in a list
for student in students:
    ...
    #print(student)
#This also works
for index, student in enumerate(students, start=0):
    ...
    #print(index, student)
#the above also works for the preivous idea 

lyst1 = [1,2,3,4]
lyst2 = lyst1
#print(lyst1, lyst2)
lyst2[1] = 9
#print(lyst1, lyst2)
#The above augments lyst1 when lyst2 gets an update, i dont think thats meant to happen

lyst3: list[str|bool] = ["values", True]
#The above creates a list that accepts only str and ints, the | symbol is the and symbol
#| is create by shift \, which is the slash above the enter

lyst4: list = [[1,2,3], [4,5,6], [7,8,9]]
lyst4[1][1] = 99
lyst4[0][1] = [1,2,3,4,5,6,7]
#print(lyst4)
#The above creates a list of lists then augments an aspect of the sublist, and inserts a list in a list in a list

from copy import deepcopy
#This activates deepcopy which is good to compltly copy another list

#a tuple is a list that cannot be modified

lyst5: dict = {"name": "David", "Age": 25, "unit": "St1", "name": "John"}
#print(lyst5["name"])
#Dictionaies relate a name item to another item, the above prints the most recent 'name' of john
for key, value in lyst5.items():
    ...
    #print(key, value)
#The above prints the dictionary with the kay and value
lyst5["key"] = "value"
#print(lyst5)
#The above adds something to the dictionaries
#You can put diciotnaties in dictionaires to show and rleate information to a code

#Big o annotations also exist and are rather complicated 



file = open("file.txt", "w")
file.write("core text")
file = open("file.txt", "a")
file.write("Extra text")
file = open("file.txt", "r")
FileContents = file.read()
FileOther = file.readline(1)
#print(FileContents)
#print(FileOther, "3q")
#FileNotFoundError exists and means that file.txt dosnt exist
#The finally funciton is used generally to shut down
#exepct Execption as expection: this function generally is used to identify the error wihtout being specific

file.close

import matplotlib.pyplot as plt
#This has failed 
