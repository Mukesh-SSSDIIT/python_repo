try:
    num1 = int(input("Enter any number : "))
    num2 = int(input("Enter any number : "))
    num3 = num1 / num2
    print("Answer is ",num3)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Second value can not be zero")
except:
    print("Other error")
else:
    print("No Errors...Greate.. You are good Programmer")
finally:
    print("Try..Except block completed")