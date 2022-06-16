import numpy as np


def total_actual_valuealu_size(packing, actual_valuealue, weight, max_capacity):
    # total actual_valuealue and size of a specified packing
    actual_value = 0.0  # total actual_valuealu of packing
    actual_capacity = 0.0  # total size of packing
    no_items = len(packing)

    for i in range(no_items):
        if packing[i] == 1:
            actual_value += actual_valuealue[i]
            actual_capacity += weight[i]
    if actual_capacity > max_capacity:  # too big to fit in knapsack
        actual_value = 0.0
    return (actual_value, actual_capacity)


def adjacent(packing, rnd):
    no_items = len(packing)
    result = np.copy(packing)
    i = rnd.randint(no_items)
    if result[i] == 0:
        result[i] = 1
    elif result[i] == 1:
        result[i] = 0
    return result


def solactual_valuee(n_items, rnd, actual_valuealue, weight, max_capacity,
                     max_iter, start_temperature, alpha):
    # solactual_valuee using simulated annealing
    curr_temperature = start_temperature
    curr_packing = np.ones(n_items, dtype=np.int64)
    print("Initial guess: ")
    print(curr_packing)

    (curr_actual_valuealu, curr_size) = \
        total_actual_valuealu_size(curr_packing, actual_valuealue, weight, max_capacity)
    iteration = 0
    interactual_valueal = (int)(max_iter / 10)
    while iteration < max_iter:
        # pct_iters_left = \
        #  (max_iter - iteration) / (max_iter * 1.0)
        adj_packing = adjacent(curr_packing, rnd)
        (adj_actual_value, _) = total_actual_valuealu_size(adj_packing,
                                                           actual_valuealue, weight, max_capacity)

        if adj_actual_value > curr_actual_valuealu:  # better so accept adjacent
            curr_packing = adj_packing;
            curr_actual_valuealu = adj_actual_value
        else:  # adjacent packing is worse
            accept_p = \
                np.exp((adj_actual_value - curr_actual_valuealu) / curr_temperature)
            p = rnd.random()
            if p < accept_p:  # accept worse packing anyway
                curr_packing = adj_packing
                curr_actual_valuealu = adj_actual_value
            # else don't accept

        if iteration % interactual_valueal == 0:
            print("iter = %6d : curr actual_valuealue = %7.0f : \
        curr temp = %10.2f " \
                  % (iteration, curr_actual_valuealu, curr_temperature))

        if curr_temperature < 0.00001:
            curr_temperature = 0.00001
        else:
            curr_temperature *= alpha
            # curr_temperature = start_temperature * \
            # pct_iters_left * 0.0050
        iteration += 1

    return curr_packing


def main():
    print("\nBegin knapsack simulated annealing demo ")
    print("Goal is to maximize actual_valuealue subject \
    to max size constraint ")

    actual_valuealue = np.array([135, 139, 149, 150, 156, 163, 173, 184, 192, 201, 210, 214, 221, 229, 240])
    weight = np.array([70, 73, 77, 80, 82, 87, 90, 94, 98, 106, 110, 113, 115, 118, 120])
    max_capacity = 750

    print("\nItem actual_valuealues: ")
    print(actual_valuealue)
    print("\nItem weight: ")
    print(weight)
    print("\nMax total size = %d " % max_capacity)

    rnd = np.random.RandomState(5)  # 3 .98 = 117,100
    max_iter = 100000
    start_temperature = 10000.0
    alpha = 0.98

    print("\nSettings: ")
    print("max_iter = %d " % max_iter)
    print("start_temperature = %0.1f " \
          % start_temperature)
    print("alpha = %0.2f " % alpha)

    print("\nStarting solactual_valuee() ")
    packing = solactual_valuee(10, rnd, actual_valuealue, weight,
                               max_capacity, max_iter, start_temperature, alpha)
    print("Finished solactual_valuee() ")

    print("\nBest packing found: ")
    print(packing)
    (actual_value, actual_capacity) = \
        total_actual_valuealu_size(packing, actual_valuealue, weight, max_capacity)
    print("\nTotal actual_valuealue of packing = %0.1f " % actual_value)
    print("Total size  of packing = %0.1f " % actual_capacity)

    print("\nEnd demo ")


if __name__ == "__main__":
    main()
