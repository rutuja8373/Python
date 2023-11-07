Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from sympy import*
>>> A=Matrix([[1,2,2],[2,1,2],[2,2,1]])
>>> A.eigenvals()
{5: 1, -1: 2}
>>> A.eigenvects()
[(-1, 2, [Matrix([
[-1],
[ 1],
[ 0]]), Matrix([
[-1],
[ 0],
[ 1]])]), (5, 1, [Matrix([
[1],
[1],
[1]])])]
>>> A.is_diagonalizable()
True
>>> P,D=A.diagonalize()
>>> P
Matrix([
[-1, -1, 1],
[ 1,  0, 1],
[ 0,  1, 1]])
>>> D
Matrix([
[-1,  0, 0],
[ 0, -1, 0],
[ 0,  0, 5]])
