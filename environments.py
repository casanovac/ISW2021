import agents
from abc import ABCMeta, abstractmethod


class SimulatedEnvironment(metaclass=ABCMeta):

    def __init__(self):
        self._agents = []

    def add(self, agent_id: int) -> None:
        self._agents.append(agent_id)

    def remove(self, agent_id: int) -> None:
        if agent_id in self._agents:
            self._agents.remove(agent_id)

    @abstractmethod
    def get_property(self, agent_id: int, property_name: str) -> dict:
        pass

    @abstractmethod
    def take_action(self, agent_id: int, action_name: str, params: dict = {}) -> None:
        pass


class SimulatedSensor(agents.Sensor):

    def __init__(self, e: SimulatedEnvironment):
        self._agent = None
        self._env = e

    @property
    def agent(self):
        return self._agent

    @agent.setter
    def agent(self, a: agents.Agent):
        self._agent = a


class SimulatedActuator(agents.Actuator):

    def __init__(self, e: SimulatedEnvironment):
        self._env = e
        self._agent = None

    @property
    def agent(self):
        return self._agent

    @agent.setter
    def agent(self, a: agents.Agent):
        self._agent = a
