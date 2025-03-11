# SUPER

Por exemplo, imagine que você tenha uma classe **Animal** com um método **fazer_som()**. Se você criar uma classe Cachorro que herda de **Animal**, e quiser adicionar um comportamento específico para latir, você pode fazer assim:
````python
class Animal:
    def fazer_som(self):
        print("Som genérico de animal")

class Cachorro(Animal):
    def fazer_som(self):
        super().fazer_som()
        print("Au au!")

# Exemplo de uso:
rex = Cachorro()
rex.fazer_som()
````
Nesse caso, **super().fazer_som()** chama o método **fazer_som()** da classe **Animal**, e depois o **Cachorro** adiciona o som específico dele, resultando em "Som genérico de animal" seguido de "Au au!".

## Conclusão 🎯
É uma maneira elegante de garantir que a funcionalidade da classe pai seja preservada enquanto você personaliza o comportamento na classe filha.