from agent.creative_agent import CreativeAgent
from agent.learning_agent import LearningAgent
from core.coordination import Coordinator

def main():
    print("Initializing NeoAI System...")

    # Creating agents
    creative_agent = CreativeAgent("Agent A")
    learning_agent = LearningAgent("Agent B")

    # Coordination
    coordinator = Coordinator([creative_agent, learning_agent])

    # Distributing tasks
    print("\nDistributing Tasks:")
    coordinator.distribute_task("Generate Ideas")

    # Collecting ideas
    print("\nCollecting Ideas:")
    coordinator.collect_ideas()

    # Learning agent interaction
    print("\nLearning Agent Feedback:")
    learning_agent.learn("Great job on creativity!")

if __name__ == "__main__":
    main()
