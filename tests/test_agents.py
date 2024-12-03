from agent.creative_agent import CreativeAgent
from agent.learning_agent import LearningAgent

def test_creative_agent():
    agent = CreativeAgent("Test Creative Agent")
    assert agent.generate_idea() is not None

def test_learning_agent():
    agent = LearningAgent("Test Learning Agent")
    result = agent.learn("Positive feedback")
    assert "Improved model" in result
