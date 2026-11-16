
# 0/1 Knapsack using Dynamic Programming

def knapsack(capacity, weight, profit, n):

    # Create DP table
    dp = [[0 for j in range(capacity + 1)]
          for i in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):

        for w in range(1, capacity + 1):

            if weight[i - 1] <= w:

                dp[i][w] = max(
                    profit[i - 1] + dp[i - 1][w - weight[i - 1]],
                    dp[i - 1][w]
                )

            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Main Program
n = int(input("Enter number of items: "))

weight = []
profit = []

for i in range(n):
    w = int(input("Enter weight: "))
    p = int(input("Enter profit: "))

    weight.append(w)
    profit.append(p)

capacity = int(input("Enter knapsack capacity: "))

result = knapsack(capacity, weight, profit, n)

print("Maximum Profit:", result)
