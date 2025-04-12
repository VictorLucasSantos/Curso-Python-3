# 🔹 Diferença entre Closures e Funções Decoradoras em Python  

Closures e funções decoradoras são conceitos relacionados, pois ambos envolvem **funções que retornam outras funções**, mas têm propósitos e usos diferentes.  

---

## 1️⃣ **Closures**  
Um **closure** é uma função que "lembra" do escopo onde foi criada, mesmo depois que esse escopo foi encerrado.  

✅ **Objetivo:** Criar funções personalizadas e reutilizáveis mantendo contexto.  
✅ **Uso comum:** Criar funções especializadas a partir de um modelo genérico.  

### 📌 Exemplo de Closure  

```python
def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar  # Retorna a função interna

# Criando funções especializadas
dobrar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)

print(dobrar(10))  # Saída: 20
print(triplicar(10))  # Saída: 30s
```
```python
def decorador(func):
    def wrapper():
        print("Executando algo antes da função...")
        func()
        print("Executando algo depois da função...")
    return wrapper  # Retorna a função modificada

@decorador
def minha_funcao():
    print("Essa é a função original!")


# Chamando a função decorada
minha_funcao()

# Executando algo antes da função...
# Essa é a função original!
# Executando algo depois da função...
```


## Principais Diferenças 
| Característica | Closures | Funções Decoradoras |
|-------------|-------------|-------------|
| Propósito    | Criar funções especializadas com contexto fixo.     | Adicionar funcionalidades extras sem modificar a função.    |
| Estrutura     | Função dentro de outra função, capturando variáveis do escopo externo.     | Função que recebe outra função como argumento e retorna uma versão modificada.    |
| Uso comum     | Criar multiplicadores, saudações, filtros de dados, etc.   | Logging, controle de acesso, monitoramento de desempenho.    |
| Chamada     |A função retorna outra função e você armazena essa nova função.    | Usa @decorador diretamente sobre uma função.    |
O que é? | Uma função que "lembra" das variáveis do escopo onde foi criada. | Uma função que recebe outra função e altera seu comportamento.|
Objetivo | 	Criar funções especializadas e com memória. | Adicionar funcionalidades extras a funções sem modificar seu código diretamente.|




## 📌 Resumo Final
**Closures** são mais usados para criar funções específicas a partir de uma função genérica.
**Decoradores** servem para modificar funções existentes de forma transparente e reutilizável.
 Ambos utilizam funções dentro de funções, mas decoradores são uma aplicação mais estruturada dos closures.
🔥 Dica: Todo decorador usa closures, mas nem todo closure é um decorador! 🚀