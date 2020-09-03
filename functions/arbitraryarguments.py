def my_sum(*numbers):
    total = 0
    for number in numbers:
        total += number
    print("Total : " + str(total))

my_sum(1,2,3,4)
