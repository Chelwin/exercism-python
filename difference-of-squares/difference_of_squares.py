def square_of_sum(count):
    return pow(sum([x for x in range(1,count+1)]),2)


def sum_of_squares(count):
    return sum([pow(x,2) for x in range(1,count+1)])


def difference(count):
    return square_of_sum(count)-sum_of_squares(count)
