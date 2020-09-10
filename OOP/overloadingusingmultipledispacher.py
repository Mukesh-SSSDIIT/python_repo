# pip3 install multipledispatch

from multipledispatch import dispatch 

#passing two parameter 
@dispatch(int,int) 
def product(first,second): 
	result = first*second 
	print("Function with 2 arguments ",result); 

#passing three parameters 
@dispatch(int,int,int) 
def product(first,second,third): 
	result = first * second * third 
	print("Function with 3 arguments ",result); 

#you can also pass data type of any value as per requirement 
@dispatch(float,float,float) 
def product(first,second,third): 
	result = first * second * third 
	print("Function with float arguments ",result); 

@dispatch(float,int)
def product(first,second):
	result = first * second 
	print("Function with float and int arguments ",result); 

def test(a):
    print(a)

#calling product method with 2 arguments 
product(2,3) #this will give output of 6 
product(2,3,2) #this will give output of 12 
product(2.2,3.4,2.3) # this will give output of 17.985999999999997 
product(2.2,5)

test("abc")