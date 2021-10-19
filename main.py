from vacuumworld import VacuumEnvironment
from vacuumagent import VacuumAgent, MoveDirection


if __name__ == '__main__':
    env = VacuumEnvironment(2, True)

    agent = VacuumAgent(env)
    print(agent.id)

    agent.print_state()
    agent.actuators["mover"].act(direction=MoveDirection.RIGHT)
    agent.print_state()
    agent.actuators["mover"].act(direction=MoveDirection.LEFT)
    agent.print_state()

