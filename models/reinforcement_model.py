class ReinforcementModel:
    def init(self, name):
        self.name = name
        self.rewards = 0
 
    def update_rewards(self, value):
        self.rewards += value
        print(f"{self.name} rewards updated to: {self.rewards}")

    def act(self, state):
        print(f"{self.name} is acting based on state: {state}")
        return "Action"
