# Linear combination

## Purpose

Linear combination of vectors is used in many applications. This programming task will give you some practice using linear combination. 

## Overview

Write a function that produces the linear combination for a matrix of the size 
$(m,n)$ and with $n$ numbers.

## Coding exercises

### Exercise 1: Compute a linear combination

Your task is to implement the following function that returns the linear combination of columns for a given matrix:

```python
def linear_combination(matrix: List[List[float]], weights: List[float]) -> List[float]:
    """Returns a linear combination of columns for a given matrix using a list of corresponding weights.

    Args:
        matrix: List[List[float]], a given numeric matrix.
        weights: List[float], a list of weights that correspond to columns

    Returns:
        The result linear combination.

    Raises:
        ValueError: If given matrix and weights are not compatible (dimensionalities don't match).
    """
    pass
```
The function should return the linear combination of columns of the given `matrix` using the given list `weights`. The  items in `weights`correspond to the columns. 

**Example 1:**

```math
matrix=\begin{pmatrix}
   3 & 4 \\
   2 & 1
\end{pmatrix}

weights=\begin{pmatrix}
   2 \\
   3 
\end{pmatrix}
```


Expected output: 

```math
2\times\begin{pmatrix}
   3 \\
   2 
\end{pmatrix}
+3\times
\begin{pmatrix}
   4 \\
   1 
\end{pmatrix}=
\begin{pmatrix}
   6 + 12\\
   4 + 3
\end{pmatrix}=
\begin{pmatrix}
   18\\
   7
\end{pmatrix}
```

**Example 2:**

```math
matrix = \begin{pmatrix}
   1 & 0 \\
   0 & 1
\end{pmatrix}

weights = \begin{pmatrix}
   2 \\
   3 
\end{pmatrix}
```

Expected output: 

```math
\begin{pmatrix}
   2\\
   3
\end{pmatrix}
```

**Example 3:**

```math
matrix = \begin{pmatrix}
   1 & 0 \\
   0 & 1
\end{pmatrix}

weights = \begin{pmatrix}
   2
\end{pmatrix}
```

Expected output: `ValueError` exception is raised as the matrix and the weights are not compatible.

Please use a template for the implementation (`tasks/linear_combination:linear_combination`).
