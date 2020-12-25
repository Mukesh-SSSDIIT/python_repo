try:
    num = int(input("Enter any number : "))
    print("You entered " + str(num))
except:
    print("Invalid input, please try again")
finally:
    print("This is finally block")