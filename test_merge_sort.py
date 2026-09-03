import random

from merge_sort import merge, merge_sort


def brief(value, limit=60):
    text = repr(value)
    return text if len(text) <= limit else text[:limit] + "..."


def check(name, actual, expected):
    if actual == expected:
        print(f"[PASS] {name}: {brief(actual)}")
    else:
        print(f"[FAIL] {name}: got {brief(actual)}, expected {brief(expected)}")


def main():
    # merge_sort: base and simple cases
    check("empty", merge_sort([]), [])
    check("single", merge_sort([7]), [7])
    check("two sorted", merge_sort([1, 2]), [1, 2])
    check("two reversed", merge_sort([2, 1]), [1, 2])

    # merge_sort: ordering variants
    check("already sorted", merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
    check("reverse sorted", merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
    check("random odd length", merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]),
          [1, 1, 2, 3, 4, 5, 5, 6, 9])
    check("random even length", merge_sort([8, 3, 5, 1, 9, 2]), [1, 2, 3, 5, 8, 9])

    # merge_sort: duplicates and negatives
    check("all equal", merge_sort([4, 4, 4, 4]), [4, 4, 4, 4])
    check("duplicates", merge_sort([2, 1, 2, 1, 3]), [1, 1, 2, 2, 3])
    check("negatives", merge_sort([-3, 5, 0, -1, 2]), [-3, -1, 0, 2, 5])

    # merge_sort: other comparable types
    check("floats", merge_sort([2.5, 0.1, -1.5]), [-1.5, 0.1, 2.5])
    check("strings", merge_sort(["pear", "apple", "fig"]), ["apple", "fig", "pear"])
    check("tuples", merge_sort([(2, "b"), (1, "a"), (2, "a")]),
          [(1, "a"), (2, "a"), (2, "b")])

    # merge_sort: input must not be mutated
    original = [3, 1, 2]
    merge_sort(original)
    check("input unchanged", original, [3, 1, 2])

    # merge: direct unit checks
    check("merge both empty", merge([], []), [])
    check("merge left empty", merge([], [1, 2]), [1, 2])
    check("merge right empty", merge([1, 2], []), [1, 2])
    check("merge interleaved", merge([1, 4, 7], [2, 3, 8]), [1, 2, 3, 4, 7, 8])
    check("merge disjoint", merge([1, 2], [3, 4]), [1, 2, 3, 4])
    check("merge uneven lengths", merge([5], [1, 2, 3]), [1, 2, 3, 5])
    check("merge equal heads", merge([1, 1], [1, 1]), [1, 1, 1, 1])

    # merge: stability - equal keys keep left-before-right order
    left = [(1, "L1"), (2, "L2")]
    right = [(1, "R1"), (2, "R2")]
    check("merge stable", merge(left, right),
          [(1, "L1"), (1, "R1"), (2, "L2"), (2, "R2")])

    # merge_sort: large randomized input against sorted()
    random.seed(42)
    for size in (50, 101, 500):
        data = [random.randint(-1000, 1000) for _ in range(size)]
        check(f"random size {size}", merge_sort(data), sorted(data))


if __name__ == "__main__":
    main()
