try:
    num = int(input("Enter any number : "))
    if num < 0:
        raise TypeError("Value can not be less than zero")
    elif num >= 0 and num <= 10:
        raise ValueError("Value can not be between 1 to 10")
    elif num >= 11 and num <= 20:
        raise Exception("Value can not be between 11 to 20")
    print("Valid input")
except ValueError:
    print("This is value error")
except TypeError:
    print("This is type error")
except:
    print("Other type of error")
