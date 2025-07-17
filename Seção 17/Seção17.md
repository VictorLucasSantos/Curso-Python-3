# 🐍 Princípios SOLID em Python

Os princípios SOLID são fundamentais para escrever código Python limpo e sustentável. Veja como aplicá-los:

## 📊 Visão Geral

| Princípio         | Pythonic Way                          | Exemplo Comum                     |
|-------------------|---------------------------------------|-----------------------------------|
| **Single Responsibility** | Usar módulos e funções pequenas       | Separar lógica de negócios de I/O |
| **Open/Closed**   | Herança e composição                  | ABC (Abstract Base Classes)       |
| **Liskov Substitution** | Polimorfismo com duck typing         | Sobrescrita de métodos            |
| **Interface Segregation** | Protocolos e ABCs                   | Múltiplas interfaces pequenas     |
| **Dependency Inversion** | Injeção de dependências              | Type hints com interfaces         |

---

## 1️⃣ S - Single Responsibility Principle (SRP)

```python
# ❌ Violação
class Usuario:
    def __init__(self, nome):
        self.nome = nome
    
    def salvar(self):
        # Lógica de persistência
        with open('usuarios.txt', 'a') as f:
            f.write(f"{self.nome}\n")
    
    def enviar_email(self, mensagem):
        # Lógica de email
        print(f"Enviando email para {self.nome}: {mensagem}")

# ✅ Solução
class Usuario:
    def __init__(self, nome):
        self.nome = nome

class UsuarioRepository:
    @staticmethod
    def salvar(usuario):
        with open('usuarios.txt', 'a') as f:
            f.write(f"{usuario.nome}\n")

class EmailService:
    @staticmethod
    def enviar(usuario, mensagem):
        print(f"Enviando email para {usuario.nome}: {mensagem}")
2️⃣ O - Open/Closed Principle (OCP)
python
from abc import ABC, abstractmethod

# ✅ Solução usando ABC
class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def area(self):
        return self.largura * self.altura

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        return 3.14 * self.raio ** 2

def calcular_area_total(formas: list[Forma]):
    return sum(forma.area() for forma in formas)

# Pode adicionar novas formas sem modificar a função calcular_area_total
3️⃣ L - Liskov Substitution Principle (LSP)
python
# ❌ Violação
class Pássaro:
    def voar(self):
        print("Voando...")

class Pinguim(Pássaro):
    def voar(self):
        raise Exception("Pinguins não voam!")

# ✅ Solução
class Pássaro:
    pass

class PássaroVoador(Pássaro):
    def voar(self):
        print("Voando...")

class Pinguim(Pássaro):
    def nadar(self):
        print("Nadando...")

def fazer_voar(pássaro: PássaroVoador):
    pássaro.voar()
4️⃣ I - Interface Segregation Principle (ISP)
python
from abc import ABC, abstractmethod

# ❌ Interface "gorda"
class Trabalhador(ABC):
    @abstractmethod
    def trabalhar(self):
        pass
    
    @abstractmethod
    def comer(self):
        pass
    
    @abstractmethod
    def dormir(self):
        pass

# ✅ Interfaces segregadas
class Trabalhador(ABC):
    @abstractmethod
    def trabalhar(self):
        pass

class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass

class Dorminhoco(ABC):
    @abstractmethod
    def dormir(self):
        pass

class Humano(Trabalhador, Comedor, Dorminhoco):
    def trabalhar(self):
        print("Trabalhando...")
    
    def comer(self):
        print("Comendo...")
    
    def dormir(self):
        print("Dormindo...")

class Robo(Trabalhador):  # Não precisa comer ou dormir
    def trabalhar(self):
        print("Trabalhando 24/7...")
5️⃣ D - Dependency Inversion Principle (DIP)
python
from abc import ABC, abstractmethod
from typing import Protocol

# Definindo abstração
class BancoDeDados(Protocol):
    def salvar(self, dados: dict):
        ...

# ❌ Alto acoplamento
class ServicoRelatorio:
    def __init__(self):
        self.db = MySQLDatabase()  # Dependência concreta
    
    def gerar(self):
        dados = {...}
        self.db.salvar(dados)

# ✅ Com DIP
class ServicoRelatorio:
    def __init__(self, db: BancoDeDados):  # Dependência abstrata
        self.db = db
    
    def gerar(self):
        dados = {...}
        self.db.salvar(dados)

# Pode usar qualquer implementação
class MySQLDatabase:
    def salvar(self, dados: dict):
        print("Salvando no MySQL...")

class MongoDB:
    def salvar(self, dados: dict):
        print("Salvando no MongoDB...")

# Uso:
servico = ServicoRelatorio(MongoDB())
servico.gerar()
🐍 Dicas Pythonicas para SOLID
Use Protocol para definir interfaces (Python 3.8+)

Prefira composição sobre herança

Utilize type hints para deixar as dependências explícitas

ABCs são úteis para implementar OCP

Módulos pequenos ajudam a manter o SRP

python
# Exemplo de Protocol
class Notificador(Protocol):
    def enviar(self, mensagem: str) -> bool:
        ...

class EmailNotificador:
    def enviar(self, mensagem: str) -> bool:
        print(f"Enviando email: {mensagem}")
        return True

class SMSNotificador:
    def enviar(self, mensagem: str) -> bool:
        print(f"Enviando SMS: {mensagem}")
        return True

def processar(notificador: Notificador):
    notificador.enviar("Mensagem importante")
