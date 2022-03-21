class B(A):
    def __init__(self, a, b):
        A.__init__(self, a)
        self.b = b