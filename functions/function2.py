def function1(age,firstname,lastname):
    if type(age) is not int:
        print("Age is not integer")
    else:
        print("Age : " + str(age))
        print(firstname + " " + lastname)

function1(20,"Sanket","Patel")