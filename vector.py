#! usr/lib/python3
# coding:utf-8

def is_correct(func):
    def inner(self, second):
        if len(self.vector) == len(second.vector):
            return func(self, second)
        else:
            raise IndexError('Vectors must have the same numbers of coordinates')
    return inner


class Vector:
    def __init__(self, *coord):
        self.vector = list(coord)

    @is_correct
    def __add__(self, second):
        sum_of_vectors = []
        for x in zip(self.vector, second.vector):
            sum_of_vectors.append(sum(x))
        return tuple(sum_of_vectors)

    @is_correct
    def __sub__(self, second):
        difference = []
        for x, y in zip(self.vector, second.vector):
            difference.append(x - y)
        return tuple(difference)

    @is_correct
    def __matmul__(self, second):
        return sum(x * y for x, y in zip(self.vector, second.vector))

    @is_correct
    def __mul__(self, second):
        if isinstance(second, int):
            product = [second * x for x in self.vector]
        else:
            if len(self.vector) == 3:
                product = [
                    self.vector[1] * second.vector[2] -
                    self.vector[2] * second.vector[1],
                    self.vector[0] * second.vector[2] -
                    self.vector[2] * second.vector[0],
                    self.vector[0] * second.vector[1] -
                    self.vector[1] * second.vector[0]
                ]
            else:
                return "Vector must be 3-dimensional"
        return tuple(product)
