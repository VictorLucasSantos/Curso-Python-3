"""
O padrão Observer tem a intenção de
definir uma dependência de um-para-muitos entre
objetos, de maneira que quando um objeto muda de
estado, todo os seus dependentes são notificados
e atualizados automaticamente.

Um observer é um objeto que gostaria de ser
informado, um observable (subject) é a entidade
que gera as informações.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Dict


class IObservable(ABC):

    @property
    @abstractmethod
    def state(self):
        return self._state

    @abstractmethod
    def add_observer(self, observer: IObserver):
        pass

    @abstractmethod
    def remove_observer(self, observer: IObserver):
        pass

    @abstractmethod
    def notify_observers(self, observer: IObserver):
        pass


class WheaterStation(IObservable):
    def __init__(self):
        self._obsevers = []
        self._state = {}

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state_update: Dict):
        new_state = Dict = {**self._state, **state_update}

        if new_state != self._state:
            self._state = new_state
            self.notify_observers()

    def reset_state(self):
        self._state = {}
        self.notify_observers()

    def add_observer(self, observer: IObserver):
        self._obsevers.append(observer)

    def remove_observer(self, observer: IObserver):
        if observer not in self._observers:
            return
        self._obsevers.remove(observer)

    def notify_observers(self):
        for observer in self._obsevers:
            observer.update()
        print()


class IObserver(ABC):
    @abstractmethod
    def update(self):
        pass


class Smartphone(IObserver):
    def __init__(self, name, observable: IObservable):
        self.name = name
        self.observable = observable

    def update(self):
        observable_name = self.observable.__class__.__name__
        print(
            f"{self.name} o objeto {observable_name}"
            f"acabou de ser atualizado => {self.observable.state}"
        )


if __name__ == "__main__":
    wheater_station = WheaterStation()

    smartphone = Smartphone("IPhone", wheater_station)
    outro_smartphone = Smartphone("OutroSmarphone", wheater_station)

    wheater_station.add_observer(smartphone)
    wheater_station.add_observer(outro_smartphone)

    wheater_station.state = {"temperature": "30"}
