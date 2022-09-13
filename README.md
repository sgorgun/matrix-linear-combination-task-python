# Matrices. Computing the linear combination task

A set of programming assignments that checks your abilities to compute linear combination of vectors. 
The source vectors are passed by the columns of the initial matrix. 
The weights that are used for computing the linear combination are passed 
by the array `weights`. The initial `matrix` of numbers has dimensions $`m\times n`$ and
has to be passed as a list of lists of numbers. The target function has signature 
`linear_combination(matrix: List[List[float]], weights: List[float]) -> List[float]` and produces a list of numbers.

For example, if the given vectors are presented by the columns of the `matrix`

```math
\begin{pmatrix}
   3 & 4 \\
   2 & 1
\end{pmatrix}
```
and `weights` are presented by vector
```math
\begin{pmatrix}
   2 \\
   3 
\end{pmatrix}
```
then, their linear combination is computed as 
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

There are two requirements:
- Target objective should be calculated correctly;
- The dimensionality of given `matrix` and `weights` have to be checked before the linear combination calculation.

Please use a template for the implementation (`tasks/linear_combination:linear_combination`).
