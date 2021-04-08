# S = 1 + x/1! - x2/2! + x3/3! - ... + xn/n!

def factorial(x):
    if x > 1:
        return x * factorial(x-1)
    else:
        return x


def recursive_method(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return recursive_method(x, n - 1) - x*n/factorial(n)
    else:
        return recursive_method(x, n - 1) + x*n/factorial(n)

def for_method(x, n):
    sum = 0

    for i in range(1, n+1):
    
        if i % 2 == 0:
            sum -= x*i/factorial(i)
        else:
            sum += x*i/factorial(i)

    sum += 1

    return sum
def while_method(x, n):
    sum = 0
    while n != 0:
    
        if n % 2 == 0:
            sum -= x*n/factorial(n)
        else:
            sum += x*n/factorial(n)

        n -= 1


    sum += 1

    return sum
def dowhile_method(x, n):
    sum = 0
    while True:
    
        if n % 2 == 0:
            sum -= x*n/factorial(n)
        else:
            sum += x*n/factorial(n)

        n -= 1

        if n == 0:
            sum += 1
            break


    return sum


def main():
    n = 10
    for x in range(0, 50):

        print("-" * 36)
        print("↓ {}th iteration ↓".format(x))
        print("| x = {}, n = {} |".format(x, n))
        print("-" * 36)

        # recursive method
        print("Recursive Method: {:18.10f}".format(recursive_method(x, n)))

        # for method 
        print("For Method: {:24.10f}".format(for_method(x, n)))

        # while
        print("While Method: {:22.10f}".format(while_method(x, n)))

        # do while
        print("Do While Method: {:19.10f}".format(dowhile_method(x, n)))

    


if __name__ == "__main__":
    main()