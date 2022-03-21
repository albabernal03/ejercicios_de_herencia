class A:
    def __init__(self, a):
        self.a = a
class B(A):
    def __init__(self, a, b):
        A.__init__(self, a)
        self.b = b
class C(A):
    def __init__(self, a, c):
        A.__init__(self, a)
        self.c = c
class D(B, C):
    def __init__(self, a, b, c):
        B.__init__(self, a, b)
        C.__init__(self, a, c)