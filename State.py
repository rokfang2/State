from abc import ABC, abstractmethod

class DoorState(ABC):
  @abstractmethod
  def click(self, door):
    pass

  @abstractmethod
  def complete(self, door):
    pass

  @abstractmethod
  def timeout(self, door):
    pass

  @abstractmethod
  def status(self, door):
    pass
