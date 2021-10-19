import random

from environments import SimulatedEnvironment


class VacuumEnvironment(SimulatedEnvironment):
    def __new__(cls, length: int, random_dirt=False):
        if length <= 0:
            raise ValueError
        else:
            return super().__new__(cls)

    def __init__(self, length: int, random_dirt=False):
        super(VacuumEnvironment, self).__init__()
        self._length = length
        self._agents_locations = {}                     # maps agent id with its location
        self._dirt_locations = set()
        if random_dirt:
            self.random_dirt(length // 2)

    def add(self, agent_id: int) -> None:
        super(VacuumEnvironment, self).add(agent_id)
        self._agents_locations[agent_id] = 0

    def remove(self, agent_id: int) -> None:
        super(VacuumEnvironment, self).remove(agent_id)
        self._agents_locations.pop(agent_id, None)

    def random_dirt(self, number_dirty_locations):
        self._dirt_locations = self._dirt_locations.union(set(random.sample(range(self._length),
                                                                            k=number_dirty_locations)))

    def _is_dirty_in_location(self, x: int) -> bool:
        return x in self._dirt_locations

    def _location_of(self, agent_id: int) -> int:
        return self._agents_locations[agent_id] if agent_id in self._agents_locations else None

    def get_property(self, agent_id: int, property_name: str) -> dict:
        if agent_id in self._agents:
            response = {"agent": agent_id}
            if property_name == "location":
                response["location"] = self._location_of(agent_id)
            elif property_name == "dirty":
                response["dirty"] = self._is_dirty_in_location(self._location_of(agent_id))
            return response
        else:
            return {}

    def _move_agent_left(self, agent_id: int):
        self._agents_locations[agent_id] = max(self._agents_locations[agent_id] - 1, 0)

    def _move_agent_right(self, agent_id: int):
        self._agents_locations[agent_id] = min(self._agents_locations[agent_id] + 1, self._length - 1)

    def _make_clean(self, agent_id: int):
        location = self._location_of(agent_id)
        self._dirt_locations.discard(location)

    def take_action(self, agent_id: int, action_name: str, params: dict = {}) -> None:
        if agent_id in self._agents:
            if action_name == "move":
                if "direction" in params and params["direction"] == "left":
                    self._move_agent_left(agent_id)
                elif "direction" in params and params["direction"] == "right":
                    self._move_agent_right(agent_id)
            elif action_name == "clean":
                self._make_clean(agent_id)
