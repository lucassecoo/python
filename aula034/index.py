class A:
    def retorno():
        print('valor a')

class B(A):
    def retorno():
        print('valor b')

class C(B):
    def retorno(self):
        super(C, self).retorno(0)
        print('valor c')