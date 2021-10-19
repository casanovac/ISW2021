from environments import SimulatedSensor, SimulatedActuator, SimulatedEnvironment
from agents import Agent


class LocationSensor(SimulatedSensor):

    def sense(self):
        response = self._env.get_property(self._agent.id, property_name="location")
        return response["location"]


class DirtSensor(SimulatedSensor):

    def sense(self):
        response = self._env.get_property(self._agent.id, property_name="dirty")
        return response["dirty"]


from enum import Enum, unique


@unique
class MoveDirection(Enum):
    LEFT = -1
    RIGHT = 1


class MoverActuator(SimulatedActuator):

    def act(self, direction: MoveDirection = MoveDirection.RIGHT):
        request_info = {"direction": ("right" if direction is MoveDirection.RIGHT else "left")}
        self._env.take_action(self._agent.id, "move", request_info)


class CleanerActuator(SimulatedActuator):

    def act(self):
        self._env.take_action(self._agent.id, "clean")


class VacuumAgent(Agent):

    def function(self, percept):
        pass

    def __init__(self, env: SimulatedEnvironment):
        super().__init__()
        env.add(self.id)

        mover = MoverActuator(env)
        mover.agent = self
        self.add_actuator("mover", mover)

        cleaner = CleanerActuator(env)
        cleaner.agent = self
        self.add_actuator("cleaner", cleaner)

        locator = LocationSensor(env)
        locator.agent = self
        self.add_sensor("location_sensor", locator)

        dirt_sensor = DirtSensor(env)
        dirt_sensor.agent = self
        self.add_sensor("dirt_sensor", dirt_sensor)

        # self.setup_function()

    def print_state(self):
        print("Estoy en la posición {} y la celda está {}".format(self._sensors["location_sensor"].sense(),
                                                                  "Sucia" if self._sensors[
                                                                      "dirt_sensor"].sense() else "Limpia"))
