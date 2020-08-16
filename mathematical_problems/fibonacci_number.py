# Fibonacci number

# definition: Each number is the sum of the two processinf ones starting from 0 and 1

def Fibonacci(n):
    container = []
    if n==1:
        container.append(0)
        return "First"+" "+str(n)+" Fibonnacci numbers are " + str(container)
    elif n==2:
        container.append(0)
        container.append(1)
        return "First"+" "+str(n)+" Fibonnacci numbers are " + str(container)
    else:
        container.append(0)
        container.append(1)
        k = 0
        for i in range(n-2):
            dummy = container[k]+container[k+1]
            container.append(dummy)
            k += 1
        return "First"+" "+str(n)+" Fibonnacci numbers are " + str(container)

#Test the function        
print(Fibonacci(10))

    


