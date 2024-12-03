class CommunicationManager:
    def __init__(self):
        self.messages = []

    def broadcast(self, agents, message):
        for agent in agents:
            print(f"Broadcasting to {agent.name}: {message}")
            agent.receive_message("System", message)

    def record_message(self, sender, recipient, message):
        self.messages.append({"sender": sender, "recipient": recipient, "message": message})
        print(f"Message recorded: {sender} -> {recipient}: {message}")

