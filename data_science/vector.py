from typing import List

Vector = List[float]

height_weight_age = [
    70,
    170,
    40
]


def add(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w)
    return [v_i + w_i for v_i, w_i in zip(v, w)]


assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]


def subtract(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w)
    return [v_i - w_i for v_i, w_i in zip(v, w)]


assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]


def vector_sum(vectors: List[Vector]) -> Vector:
    """Sums all corresponding elements"""  # Check that vectors is not empty
    assert vectors, "no vectors provided!"

    # Check the vectors are all the same size
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sizes!"

    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]


assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]


def scalar_multiply(scalar: float, v: Vector) -> Vector:
    """Multiplies every element by c"""
    return [scalar * v_i for v_i in v]


assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]


def vector_mean(vectors: List[Vector]) -> Vector:
    """Computes the element-wise average"""
    n = len(vectors)
    return [sum(v[i] for v in vectors) / n for i in range(len(vectors[0]))]

assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]


def dot_product(v1: Vector, v2: Vector) -> float:
    """Computes v_1 * w_1 + ... + v_n * w_n"""
    assert len(v1) == len(v2)
    return sum(v1_i * v2_i for v1_i, v2_i in zip(v1, v2))

assert dot_product([1, 2, 3], [4, 5, 6]) == 32


def sum_of_squares(v: Vector) -> float:
    return dot_product(v, v)

assert sum_of_squares([1, 2, 3]) == 14 # 1 * 1 + 2 * 2 + 3 * 3



import math

def magnitude(v: Vector) -> float:
    """"
    Returns
    the
    magnitude( or length) of
    v
    """

    return math.sqrt(sum_of_squares(v))

assert magnitude([3, 4]) == 5


# def squared_distance(v1: Vector, v2: Vector) -> float:
