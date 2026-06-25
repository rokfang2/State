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

  def click(self):
    self._state.click(self)

  def complete(self):
    self._state.complete

  def timeout(self):
    self._state.timeout(self)

  def status(self) ->  str:
    return self._state.status()

class DoorClosed(DoorState):
  def click(self, door):
    print("[Closed] -> Clicou: Abrindo a porta...")
    door.set_state(DoorOpening())

  def complete(self, door): pass
  def timeout(self, door)> pass
  def status(self) -> str: return "Closed"
