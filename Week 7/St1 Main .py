#St1  
from tkinter import *

window = Tk()

try:
    file = open("Appointments.txt", "r")
    file.close()
except FileNotFoundError:
    file = open("Appointments.txt", "w")
    file.write("Id | Date | Time | Patient | Practitoner | Notes | Status \n")
    file.close()
finally:
    pass


def Check_Entries():
    if Appointment_Date.get() == "":
        print("Please enter an appointment date")
        return False

    if Appointment_Time.get() == "":
        print("Please enter an appointment time")
        return False

    if Appointment_Patient.get() == "":
        print("Please enter a patient")
        return False

    if Appointment_Pratitoner.get() == "":
        print("Please enter a practitioner")
        return False

    if Appointment_Notes.get() == "":
        print("Please enter appointment notes")
        return False

    if Appointment_Status.get() == "":
        print("Please enter an appointment status")
        return False

    return True

def Clear():
    Appointment_ID.set("")
    Appointment_Date.set("")
    Appointment_Time.set("")
    Appointment_Patient.set("")
    Appointment_Pratitoner.set("")
    Appointment_Notes.set("")
    Appointment_Status.set("")

def Create_TXT():
    if Check_Entries() == False:
        return

        Highest_ID = 0
        File = open("Appointments.txt", "r")
        next(File)
        for line in File:
            Check = line.strip().split("|")
            if Check[0].startswith("A"):
                Checker = int(Check[0][1:])
                if Checker > Highest_ID:
                    Highest_ID = Checker
        New_ID = "A" + str(Highest_ID + 1).zfill(4)
        Appointment_ID.set(New_ID)
        File.close()
 
        Appointment = {"Appointment ID:": New_ID, "Date:": Appointment_Date.get(),
                "Time:": Appointment_Time.get(), "Patinet:": Appointment_Patient.get(),
                "Practitioner:": Appointment_Pratitoner.get(), "Notes:": Appointment_Notes.get(),
                "Appointment Status:": Appointment_Status.get()}
        File = open("Appointments.txt", "a")
        File.write(Appointment["Appointment ID:"] + "|" + Appointment["Date:"] + "|" +
                Appointment["Time:"] + "|" + Appointment["Patinet:"] + "|" + 
                Appointment["Practitioner:"] + "|" + Appointment["Notes:"] + "|" + 
                Appointment["Appointment Status:"] + "\n")
        File.close()
    
def Change_TXT():
    ID = Appointment_ID.get()
    File = open("Appointments.txt", "r")
    Lines = File.readlines()
    File.close()

    File = open("Appointments.txt", "w")
    for Line in Lines:
        Entry = Line.strip().split("|")
        if Entry[0] == ID:
            Appointment = {"Appointment ID:": Appointment_ID.get(), "Date:": Appointment_Date.get(),
                "Time:": Appointment_Time.get(), "Patinet:": Appointment_Patient.get(),
                "Practitioner:": Appointment_Pratitoner.get(), "Notes:": Appointment_Notes.get(),
                "Appointment Status:": Appointment_Status.get()}
            File.write(Appointment["Appointment ID:"] + "|" + Appointment["Date:"] + "|" +
                Appointment["Time:"] + "|" + Appointment["Patinet:"] + "|" + 
                Appointment["Practitioner:"] + "|" + Appointment["Notes:"] + "|" + 
                Appointment["Appointment Status:"] + "\n")
        else:
            File.write(Line)
    File.close()

def Load_TXT():
    Search = Appointment_ID.get()
    File = open("Appointments.txt", "r")
    Found = False
    for Line in File:
        Entry = Line.strip().split("|")
        if Entry[0] == Search:
            Appointment_ID.set(Entry[0])
            Appointment_Date.set(Entry[1])
            Appointment_Time.set(Entry[2])
            Appointment_Patient.set(Entry[3])
            Appointment_Pratitoner.set(Entry[4])
            Appointment_Notes.set(Entry[5])
            Appointment_Status.set(Entry[6])
            Found = True

        
    File.close()
    if Found == False:
        print("Unable to find appoitment")
            
    

#Terms and varibles 
Appointment_ID = StringVar()
Appointment_Date = StringVar()
Appointment_Time = StringVar()
Appointment_Patient = StringVar()
Appointment_Pratitoner = StringVar()
Appointment_Notes = StringVar()
Appointment_Status = StringVar()


#UI
Label (window, text = "Appointment ID").grid(row=0,column=0,padx=5,pady=10)
Label (window, text = "Appointment Date").grid(row=1,column=0,padx=5,pady=10)
Label (window, text = "Appointment Time").grid(row=2,column=0,padx=5,pady=10)
Label (window, text = "Patinet").grid(row=3,column=0,padx=5,pady=10)
Label (window, text = "Practitioner").grid(row=4,column=0,padx=5,pady=10)
Label (window, text = "Appointment Notes").grid(row=5,column=0,padx=5,pady=10)                    
Label (window, text = "Appointment Status").grid(row=6,column=0,padx=5,pady=10)
                    
Entry (window, width=10,textvariable = Appointment_ID).grid(row=0,column=1,padx=5,pady=10)
Entry (window, width=10,textvariable = Appointment_Date).grid(row=1,column=1,padx=5,pady=10)
Entry (window, width=10,textvariable = Appointment_Time).grid(row=2,column=1,padx=5,pady=10)
Entry (window, width=10,textvariable = Appointment_Patient).grid(row=3,column=1,padx=5,pady=10)
Entry (window, width=10,textvariable = Appointment_Pratitoner).grid(row=4,column=1,padx=5,pady=10)
Entry (window, width=10,textvariable = Appointment_Notes).grid(row=5,column=1,padx=5,pady=10)
Entry (window, width=10,textvariable = Appointment_Status).grid(row=6,column=1,padx=5,pady=10)
                    
Button(window,text="Change Appointment",command=Change_TXT).grid(row=0,column=2,padx=5,pady=10)
Button(window,text="Load Appointment",command=Load_TXT).grid(row=1,column=2,padx=5,pady=10)
Button(window,text="Create New Appointment",command=Create_TXT).grid(row=2,column=2,padx=5,pady=10)
Button(window,text="Clear Entires",command=Clear).grid(row=3,column=2,padx=5,pady=10)
              
window.title("SmartCare Appointment User Interface")

mainloop()
