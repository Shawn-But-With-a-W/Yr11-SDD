'''It's slightly uncentred but we don't talk about that'''

def fibonacci(num1=0, num2=1, n=0, final=0):
    if n > 0:
        print(' ' * ((final-num1)//2), end='')
        print('α'*num1)
        print(' ' * ((final-num1)//2))

        fibonacci(num2, num1+num2, n-1, final)


def final_fibonacci(num1=0, num2=1, n=0):
    if n > 1:
        return(final_fibonacci(num2, num1+num2, n-1))
    else:
        return num1


n = int(input('Number of terms: '))
fibonacci(n=n, final=final_fibonacci(n=n))