class KnowledgeBase:
    def __init__(self):
        self.knowledge = {}

    def add_entry(self, topic, content):
        self.knowledge[topic] = content
        print(f"Knowledge added: {topic}")

    def get_entry(self, topic):
        return self.knowledge.get(topic, "No knowledge on this topic.")

    def list_topics(self):
        return list(self.knowledge.keys())

