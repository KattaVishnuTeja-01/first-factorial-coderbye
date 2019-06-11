def FirstFactorial(num): 

    fact = 1
    # code goes here 
    for i in range(1, num + 1):
        fact = fact * i
    return fact
    
# keep this function call here  
num = raw_input()
print FirstFactorial(num)
