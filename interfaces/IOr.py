from abc import ABC, abstractmethod


class IOr(ABC):

    @property
    @abstractmethod
    def piece_or(self):
        pass