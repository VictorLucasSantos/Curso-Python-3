"""
Classes abstratas - Abstract Base Class (abc)
ABCs são usadas como contratos para a definição
de novas classes. Elas podem forçar outras classes
a criarem métodos concretos. Também podem ter
métodos concretos por elas mesmas.
@abstractmethods são métodos que não têm corpo.
As regras para classes abstratas com métodos
abstratos é que elas NÃO PODEM ser instânciadas
diretamente.
Métodos abstratos DEVEM ser implementados
nas subclasses (@abstractmethod).
Uma classe abstrata em Python tem sua metaclasse
sendo ABCMeta.
É possível criar @property @setter @classmethod
@staticmethod e @method como abstratos, para isso
use @abstractmethod como decorator mais interno.

"""

from abc import ABC, abstractmethod


# criando uma classe abstrata
class Log(ABC):
    # definindo um metodo abstrato (deve conter um metodo abstrato para que não seja instanciada)
    @abstractmethod
    def _log(self, msg): ...

    def log_error(self, msg):
        return self._log(f"Error: {msg}")

    def log_success(self, msg):
        return self._log(f"Success: {msg}")


class LogPrintMixin(Log):
    # quando utilizado a classe abstrata sempre utilizar a mesma assinatura para a classe filha da abstrata
    def _log(self, msg):
        print(f"{msg} ({self.__class__.__name__})")
