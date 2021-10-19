from abc import ABCMeta, abstractmethod
import uuid

class Sensor(metaclass=ABCMeta):

    @abstractmethod
    def sense(self):
        pass


class Actuator(metaclass=ABCMeta):
    @abstractmethod
    def act(self):
        pass


class Agent(metaclass=ABCMeta):
    def __init__(self):
        self._uuid = uuid.uuid1()
        self._sensors = {}
        self._actuators = {}

    @property
    def id(self):
        return self._uuid.int

    def add_sensor(self, name: str, s: Sensor):
        self._sensors[name] = s

    def remove_sensor(self, name: str):
        self._sensors.pop(name, None)

    @property
    def sensors(self):
        return self._sensors

    def add_actuator(self, name: str, a: Actuator):
        self._actuators[name] = a

    def remove_actuator(self, name: str):
        self._actuators.pop(name, None)

    @property
    def actuators(self):
        return self._actuators

    @abstractmethod
    def function(self, percept):
        """
        Agent function that must be overriden with an agent program in order to calc actions
        :type percept: object
        :rtype action
        """
        pass