from tasks.linear_combination import linear_combination


def compare_result(matrix, weights, result) -> bool:
    return linear_combination(matrix, weights) == result


def test_linear_combination_1():
    assert compare_result([[1, 0], [0, 1]], [2, 3], [2, 3]), True


def test_linear_combination_2():
    assert compare_result([[1, 1], [1, 1]], [2, 3], [5, 5]), True
