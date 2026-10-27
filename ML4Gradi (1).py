def f(x):
    return (x + 3)**2

def derivative(x):
    return 2 * (x + 3)

x = 2
lr = 0.1

for i in range(100):
    x = x - lr * derivative(x)

print("Local Minimum x:", round(x, 4))
print("Minimum value y:", round(f(x), 4))