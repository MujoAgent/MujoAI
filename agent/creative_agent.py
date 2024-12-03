from .base_agent import BaseAgent

class CreativeAgent(BaseAgent):
    def __init__(self, name):
        super().__init__(name, "Creative Agent")

    def generate_idea(self):
        idea = f"Creative idea from {self.name}: {self._generate_random_concept()}"
        print(idea)
        return idea

    def _generate_random_concept(self):
        return "A groundbreaking design concept"

