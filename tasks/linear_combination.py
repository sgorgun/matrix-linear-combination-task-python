from typing import List


def linear_combination(matrix: List[List[float]], weights: List[float]) -> List[float]:
    """Returns a linear combination of columns for a given matrix using a list of corresponding weights.

    Args:
        matrix: List[List[float]], a given numeric matrix.
        weights: List[float], a list of weights that correspond to the columns of the matrix

    Returns:
        The resulting linear combination.

    Raises:
        ValueError: If the given matrix and weights are not compatible (dimensionalities don't match).
    """
    if len(matrix[0]) != len(weights):
        raise ValueError("Dimensionalities of matrix and weights don't match.")
    
    result = []
    for i in range(len(matrix)):
        linear_sum = 0
        for j in range(len(matrix[i])):
            linear_sum += matrix[i][j] * weights[j]
        result.append(linear_sum)
    
    return result
