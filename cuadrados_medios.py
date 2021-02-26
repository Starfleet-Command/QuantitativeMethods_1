import math


def split_int(x_squared):
    decomposed_x = [char for char in str(x_squared)]
    size = len(str(x_squared))
    if(size == 8):
        next_x = str(decomposed_x[2]) + str(decomposed_x[3]) + \
            str(decomposed_x[4]) + str(decomposed_x[5])
    else:
        next_x = str(decomposed_x[size-6]) + str(decomposed_x[size-5]) + \
            str(decomposed_x[size-4]) + str(decomposed_x[size-3])
    return int(next_x)


def mean_squares(x, iterations):
    x = int(x)
    iterations = int(iterations)
    r_list = []

    while(iterations > 0):
        x_squared = x * x

        next_x = split_int(x_squared)

        if(next_x == 0):
            break

        percent = float("0." + str(next_x))
        r_list.append(percent)
        x = next_x
        iterations = iterations - 1

    return r_list
