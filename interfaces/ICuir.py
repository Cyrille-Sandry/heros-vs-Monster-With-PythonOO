from abc import ABC, abstractmethod

class ICuir(ABC):

    @property
    @abstractmethod
    def cuir(self):
        pass