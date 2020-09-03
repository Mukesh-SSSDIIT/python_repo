def fibonacci_recursion(n,current_number=0,next_number=1):
    if n==1:
        return 0
    if current_number == 0:
        print (current_number)
        print (next_number)
    else:
        print(next_number)
    no = next_number
    next_number = current_number + next_number
    current_number = no
    fibonacci_recursion(n-1,current_number,next_number)

fibonacci_recursion(10)