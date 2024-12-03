from .base_agent import BaseAgent

class LearningAgent(BaseAgent):
    def __init__(self, name):
        super().__init__(name, "Learning Agent")

    def learn(self, feedback):
        print(f"{self.name} is learning from feedback: {feedback}")
        return f"Improved model based on feedback: {feedback}"

