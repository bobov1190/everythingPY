def calculate_factorial(number):
    
    factorial = 1
    
    for i in range(1,number+1):
        factorial = factorial * i
    
    
    print(factorial)

numbers = int(input("Enter a number..."))



print(calculate_factorial(numbers))