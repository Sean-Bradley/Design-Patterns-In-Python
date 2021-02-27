"Decorator Use Case Example Code"
from value import Value
from add import Add
from sub import Sub

A = Value(1)
B = Value(2)
C = Value(5)

print(Add(A, B))
print(Add(A, 100))
print(Sub(C, A))
print(Sub(Add(C, B), A))
print(Sub(100, 101))
print(Add(Sub(Add(C, B), A), 100))
print(Sub(123, Add(C, C)))
print(Add(Sub(Add(C, 10), A), 100))
print(A)
print(B)
print(C)
