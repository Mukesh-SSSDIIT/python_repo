def studentname(firstname,lastname):
    if firstname == None and  lastname == None:
        print("Please pass arguments")
    elif lastname == None:
        print("Welcome " + firstname)
    elif firstname == None:
        print("Welcome " + lastname)
    else:       
        print("Welcome " + firstname + " " + lastname)

def studentdata(name,age):
    print("Name : " + name)
    print("Age : " + str(age))

# fn = input("Enter your firstname : ")
# ln = input("Enter your lastname : ")
#studentname("Mital","Rakholiya")

studentdata("Mital",20)