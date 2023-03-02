def Fibonacci(x): #fibonacci function

    if(x == 0):
        return 0
    elif(x==1):
        return 1
    elif(x>1):
        f = Fibonacci(x-1) + Fibonacci(x-2)
        return f
    #end of the function

#taking the first input
x = int(input('Enter the number:'))

#beginning of the while loop
while x != -1:
    
    a = Fibonacci(x)
    print('answer is',a)
    x = int(input('Enter the number:'))
