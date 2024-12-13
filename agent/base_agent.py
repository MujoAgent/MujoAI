class BaseAgent:
    def __init__(self, name, role):
        self.name = name
        self.role = role
 
    def send_message(self, recipient, message):
        print(f"[{self.name} -> {recipient.name}]: {message}")

    def receive_message(self, sender, message):
        print(f"[{sender.name} -> {self.name}]: {message}")

    def perform_task(self):
        print(f"{self.name} ({self.role}) is performing its task.")

