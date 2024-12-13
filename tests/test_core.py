from core.knowledge_base import KnowledgeBase
 
def test_knowledge_base():
    kb = KnowledgeBase()
    kb.add_entry("AI", "Artificial Intelligence")
    assert kb.get_entry("AI") == "Artificial Intelligence"
