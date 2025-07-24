class Meta(type):
    def __call__(cls, **args, **kwargs):
        return super().__call__(**args, **kwargs)
    
class Pessoa(Metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, nome):
        self.nome = nome

    def __call__(self, x, y):
        print("Call chamado", self.nome, "", x, y)


p = Pessoa("Luiz")
p(2, 2)
print(p.nome)
