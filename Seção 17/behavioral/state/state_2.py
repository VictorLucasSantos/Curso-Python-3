from __future__ import annotations
from abc import ABC, abstractmethod


class Sound:
    def __init__(self):
        self.mode: PlayMode = RadioMode()


class PlayMode(ABC):
    def __init__(self, sound: Sound):
        self.mode = sound
        self.playing = 0

    def change_mode(self, mode: PlayMode):
        self.playing = 0
        self.mode = mode

    @abstractmethod
    def press_next(self):
        pass

    @abstractmethod
    def press_prev(self):
        pass


class RadioMode(PlayMode):
    def press_next(self):
        self.sound.playing += 1

    def press_prev(self):
        self.sound.playing -= 1000 if self.sound.playing > 0 else 0
