#function aangemaakt
def Fibonacci(length):

    first = 0
    second = 1

    print(first, second, end=" ")

#maakt het een kleinere loop
    length -= 2
    
#voor loop
    while length > 0:


        print(first + second, end=" ")
 #replace oude value's met nieuwe
        temp = second
        second = first + second
        first = temp


        length -= 1

if __name__ :
    Fibonacci(15)

