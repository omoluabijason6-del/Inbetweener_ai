from typing import Dict


class AnimationKernel:
    """
    The Animation Kernel is the heart of the application.

    Responsibilities:
    - Register agents
    - Start the system
    - Shut down the system
    - Keep track of loaded agents
    """

    def __init__(self):
        self.agents: Dict[str, object] = {}

    def register_agent(self, agent):
        """Register an agent with the kernel."""

        self.agents[agent.name] = agent
        print(f"[Kernel] Registered: {agent.name}")

    def get_agent(self, name):
        """Return a registered agent."""

        return self.agents.get(name)

    def list_agents(self):
        """Display all registered agents."""

        print("\nLoaded Agents")

        print("----------------")

        for name in self.agents:
            print(f"• {name}")

    def start(self):
        """Start every registered agent."""

        print("\n[Kernel] Starting...")

        for agent in self.agents.values():

            if hasattr(agent, "start"):
                agent.start()

        print("\n[Kernel] System Ready.")

    def shutdown(self):
        """Shutdown the application."""

        print("\n[Kernel] Shutdown Complete.")