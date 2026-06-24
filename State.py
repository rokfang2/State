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

class Door:
  def __init__(self):
    self._state = DoorClosed()
    self._observers = []

  def set_state(self, state: DoorState):
    self._state = state
    self.notify_observers()
  
  def add_observer(self, callback):
    self._observers.append(callback)

  def notify_observers(self):
    for observer in self._observers:
      observer(self.status())
