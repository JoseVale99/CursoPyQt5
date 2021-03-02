class A:
    """
    Example of multiple inheritance
    """
    def a(self):
        print("- From to A")

class B:
    def b(self):
        print("- From to B")

class  C(A,B):

    def c(self):
        print("- From to C")


letter = C()
letter.a()
letter.b()
letter.c()