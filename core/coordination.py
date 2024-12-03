class Coordinator:
    def __init__(self, agents):
        self.agents = agents

    def distribute_task(self, task):
        print(f"Distributing task: {task}")
        for agent in self.agents:
            agent.perform_task()

    def collect_ideas(self):
        ideas = []
        for agent in self.agents:
            if hasattr(agent, 'generate_idea'):
                ideas.append(agent.generate_idea())
        print("Collected ideas:", ideas)
        return ideas

