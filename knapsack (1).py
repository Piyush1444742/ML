
# Fractional Knapsack using Greedy Method

def fractional_knapsack(profit, weight, capacity):

    n = len(profit)

    # Calculate profit/weight ratio
    ratio = []

    for i in range(n):
        ratio.append(profit[i] / weight[i])

    # Sort items according to ratio in descending order
    for i in range(n):
        for j in range(i + 1, n):
            if ratio[i] < ratio[j]:
                ratio[i], ratio[j] = ratio[j], ratio[i]
                profit[i], profit[j] = profit[j], profit[i]
                weight[i], weight[j] = weight[j], weight[i]

    total_profit = 0

    # Select items
    for i in range(n):

        if weight[i] <= capacity:
            total_profit += profit[i]
            capacity -= weight[i]

        else:
            total_profit += ratio[i] * capacity
            break

    return total_profit


# Main Program
n = int(input("Enter number of items: "))

profit = []
weight = []

for i in range(n):
    p = float(input("Enter profit: "))
    w = float(input("Enter weight: "))

    profit.append(p)
    weight.append(w)

capacity = float(input("Enter knapsack capacity: "))

result = fractional_knapsack(profit, weight, capacity)

print("Maximum Profit:", result)
