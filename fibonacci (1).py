def fibonacci_iterative(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c


# Recursive Function
def fibonacci_recursive(n):

    if n == 0:
        return 0

    elif n == 1:
        return 1

    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

n = int(input("Enter the number of terms: "))

print("\nNon-Recursive Fibonacci Series:")
fibonacci_iterative(n)

print("\nRecursive Fibonacci Series:")
for i in range(n):
    print(fibonacci_recursive(i), end=" ")
