

def fibonacci(n):
    """
    Calculates the nth Fibonacci number.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    print('Hello World!')
    print('Fibonnachi of 10 is:', fibonacci(10))
    
    