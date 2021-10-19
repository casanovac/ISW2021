from vacuumagent import VacuumAgent, MoveDirection
import Pyro4

uri = "PYRONAME:vacuumworld"

vacuumenv = Pyro4.Proxy(uri)

vacuumenv.build_env(length=2, dirty_locations=1)
agent = VacuumAgent(vacuumenv)

agent.print_state()
agent.actuators["cleaner"].act()
agent.print_state()
agent.actuators["mover"].act(direction=MoveDirection.RIGHT)
agent.print_state()
agent.actuators["cleaner"].act()
agent.print_state()
agent.actuators["mover"].act(direction=MoveDirection.LEFT)
agent.print_state()
