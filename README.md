# LOOPS

## e.g For Loop
```
def for_method(x, n):
    sum = 0

    for i in range(1, n+1):
    
        if i % 2 == 0:
            sum -= x*i/factorial(i)
        else:
            sum += x*i/factorial(i)

    sum += 1

    return sum
```
