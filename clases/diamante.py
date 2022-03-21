class A:
    def __init__(self, a):
        self.a = a

class B(A):
    def __init__(self, a, b):
        self.a = a
        self.b = b

class C(A):
    def __init__(self, a, c):
        self.a = a
        self.c = c

class D(B, C):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

d = D(1, 2, 3)
print(d.a, d.b, d.c)