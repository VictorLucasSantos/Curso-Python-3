from time import sleep
from threading import Thread


class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo
        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)


t1 = MeuThread("Thread 1", 5)
t1.start()


t1 = MeuThread("Thread 2", 2)
t1.start()


for i in range(10):
    print(i)
    sleep(1)


# 0
# 1
# 2
# 3
# 4
# Thread 1
# 5
# 6
# 7
# 8
# 9
def demora(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=demora, args=("Teste 1", 2))
t1.start()

t2 = Thread(target=demora, args=("Teste 2", 4))
t2.start()

t3 = Thread(target=demora, args=("Teste 3", 6))
t3.start()

t4 = Thread(target=demora, args=("Teste 4", 6))
t4.start()

while t4.is_alive():
    print("Esperando fim da Thread Teste 4")
    sleep(0.5)
