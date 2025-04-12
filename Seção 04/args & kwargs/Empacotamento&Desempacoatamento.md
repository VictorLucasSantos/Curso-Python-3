# Empacotamento e Desempacotamento de Parâmetros em Python

## 1. O que são `*args` e `**kwargs`?
Em Python, `*args` e `**kwargs` são usados para empacotar e desempacotar argumentos em funções:

- `*args`: recebe uma quantidade **variável** de argumentos posicionais e os empacota em uma tupla.
- `**kwargs`: recebe uma quantidade **variável** de argumentos nomeados e os empacota em um dicionário.

## 2. Exemplo de Uso de `*args`
### Empacotamento:
```python
# Função que aceita vários argumentos posicionais
def soma(*args):
    return sum(args)

print(soma(1, 2, 3, 4))  # Saída: 10
```

Aqui, `*args` empacota os valores `(1, 2, 3, 4)` em uma tupla `(1, 2, 3, 4)`.

### Desempacotamento:
```python
numeros = [1, 2, 3, 4]
print(soma(*numeros))  # Usa o * para desempacotar a lista
```

O `*numeros` desempacota a lista `[1, 2, 3, 4]` em argumentos individuais para a função.

## 3. Exemplo de Uso de `**kwargs`
### Empacotamento:
```python
# Função que aceita vários argumentos nomeados
def exibir_dados(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

exibir_dados(nome="Victor", idade=30, linguagem="Python")
```

Aqui, `**kwargs` empacota os argumentos nomeados em um dicionário:
```python
{
    "nome": "Victor",
    "idade": 30,
    "linguagem": "Python"
}
```

### Desempacotamento:
```python
dados = {"nome": "Lucas", "idade": 25}
exibir_dados(**dados)  # Desempacotando dicionário
```

O `**dados` desempacota o dicionário e passa os valores como argumentos nomeados.

## 4. Usando `*args` e `**kwargs` juntos
Podemos combinar os dois para criar funções flexíveis:
```python
def exibir_tudo(a, b, *args, **kwargs):
    print(f"a: {a}, b: {b}")
    print("args:", args)
    print("kwargs:", kwargs)

exibir_tudo(1, 2, 3, 4, 5, nome="Victor", linguagem="Python")
```

Saída:
```
a: 1, b: 2
args: (3, 4, 5)
kwargs: {'nome': 'Victor', 'linguagem': 'Python'}
```

## 5. Conclusão
- `*args` → empacota argumentos posicionais em uma **tupla**.
- `**kwargs` → empacota argumentos nomeados em um **dicionário**.
- Ambos podem ser desempacotados com `*` e `**` ao passar para uma função.
- Podem ser combinados para criar funções dinâmicas e flexíveis.

