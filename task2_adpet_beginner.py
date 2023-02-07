def fibonacci(num1=0, num2=1, n=0):
    if n > 0:
        print(num1)

        fibonacci(num2, num1+num2, n-1)

n = int(input('Number of terms: '))
fibonacci(n=n)