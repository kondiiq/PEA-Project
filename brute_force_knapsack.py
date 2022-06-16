def knapSack(max_capaxity, weight, value, n):
    # initial conditions
    if n == 0 or max_capaxity == 0:
        return 0
    # If weight is higher than capacity then it is not included
    if weight[n - 1] > max_capaxity:
        return knapSack(max_capaxity, weight, value, n - 1)
    # return either nth item being included or not
    else:
        return max(value[n - 1] + knapSack(max_capaxity - weight[n - 1], weight, value, n - 1),
                   knapSack(max_capaxity, weight, value, n - 1))


# To test above function
value = [135, 139, 149, 150, 156, 163, 173, 184, 192, 201, 210, 214, 221, 229, 240]
weight = [70, 73, 77, 80, 82, 87, 90, 94, 98, 106, 110, 113, 115, 118, 120]
max_capaxity = 750
n = len(value)
print(knapSack(max_capaxity, weight, value, n))
