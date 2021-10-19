from vacuumworld import VacuumEnvironment
import Pyro4


class VacuumWorldPyroAdapter:
    def __init__(self):
        self._vacuumenv = None

    @Pyro4.expose
    def build_env(self, length: int, dirty_locations: int):
        self._vacuumenv = VacuumEnvironment(length, random_dirt=False)
        self._vacuumenv.random_dirt(number_dirty_locations=dirty_locations)

    @Pyro4.expose
    def add(self, agent_id: int) -> None:
        if self._vacuumenv is not None:
            self._vacuumenv.add(agent_id)

    @Pyro4.expose
    def remove(self, agent_id: int) -> None:
        if self._vacuumenv is not None:
            self._vacuumenv.remove(agent_id)

    @Pyro4.expose
    def get_property(self, agent_id: int, property_name: str) -> dict:
        response = {}
        if self._vacuumenv is not None:
            response = self._vacuumenv.get_property(agent_id, property_name)
        return response

    @Pyro4.expose
    def take_action(self, agent_id: int, action_name: str, params: dict) -> None:
        if self._vacuumenv is not None:
            self._vacuumenv.take_action(agent_id, action_name, params)

if __name__ == '__main__':
    daemon = Pyro4.Daemon(host="localhost")
    ns = Pyro4.locateNS()
    uri = daemon.register(VacuumWorldPyroAdapter)
    ns.register("vacuumworld", uri)
    print(uri)
    daemon.requestLoop()
