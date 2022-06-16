def knapSack(max_capacity, weight, value, n):
    K = [[0 for x in range(max_capacity + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner 
    for i in range(n + 1):
        for w in range(max_capacity + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weight[i - 1] <= w:
                K[i][w] = max(value[i - 1]
                              + K[i - 1][w - weight[i - 1]],
                              K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][max_capacity]


# Driver code 
value = [135, 139, 149, 150, 156, 163, 173, 184, 192, 201, 210, 214, 221, 229, 240]
weight = [70, 73, 77, 80, 82, 87, 90, 94, 98, 106, 110, 113, 115, 118, 120]
max_capacity = 750
n = len(value)
print(knapSack(max_capacity, weight, value, n))
