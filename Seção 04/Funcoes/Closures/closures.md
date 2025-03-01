# Closures em Python

Em Python, **closures** são funções que capturam variáveis locais da função que as envolve.  
Isso permite que uma função "lembre" do estado de variáveis mesmo após a execução da função externa.  

Isso é útil para criar **funções especializadas e reutilizáveis**, facilitando a manutenção do código.

---

## 🔹 Exemplo 1: Funções com Argumentos

```python
def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y

def criar_funcao(funcao):
    def executar(*args):
        return funcao(*args)
    return executar

# Criando funções especializadas
soma_com_cinco = criar_funcao(soma)
multiplica_por_dez = criar_funcao(multiplica)

# Utilizando as funções criadas
print(soma_com_cinco(5, 3))  # Saída: 8
print(multiplica_por_dez(10, 5))  # Saída: 50


```
## 📌 Explicação:

A função criar_funcao recebe uma função como argumento e retorna outra função (executar).
A função executar pode acessar funcao, mesmo após criar_funcao ter sido executada.
Isso permite criar funções reutilizáveis sem precisar reescrever a lógica.

## 📌 Benefícios de usar Closures

✔ Evitam o uso de variáveis globais.

✔ Permitem criar funções especializadas e reutilizáveis.

✔ Melhor organização e manutenção do código.

Closures são uma das poderosas funcionalidades de Python para criar código mais modular e eficiente!