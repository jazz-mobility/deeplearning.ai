def test_planner_agent(planner_agent):
    print("Testing planner_agent...")
    try:
        result = planner_agent("test topic")
        assert isinstance(result, list), "planner_agent should return a list"
        assert len(result) > 0, "planner_agent should return at least one step"
        assert all(isinstance(step, str) for step in result), "All steps should be strings"
        print("✅ All tests passed for planner_agent!")
    except Exception as e:
        print(f"❌ Test failed: {e}")


def test_research_agent(research_agent):
    print("Testing research_agent...")
    try:
        import inspect
        source = inspect.getsource(research_agent)
        assert "arxiv_search_tool" in source, "research_agent should use arxiv_search_tool"
        assert "tavily_search_tool" in source, "research_agent should use tavily_search_tool"
        assert "wikipedia_search_tool" in source, "research_agent should use wikipedia_search_tool"
        assert "tool_choice" in source, "research_agent should set tool_choice"
        assert "max_turns" in source, "research_agent should set max_turns"
        print("✅ All tests passed for research_agent!")
    except Exception as e:
        print(f"❌ Test failed: {e}")


def test_writer_agent(writer_agent):
    print("Testing writer_agent...")
    try:
        import inspect
        source = inspect.getsource(writer_agent)
        assert "system" in source, "writer_agent should have a system message"
        assert "user" in source, "writer_agent should have a user message"
        print("✅ All tests passed for writer_agent!")
    except Exception as e:
        print(f"❌ Test failed: {e}")


def test_editor_agent(editor_agent):
    print("Testing editor_agent...")
    try:
        import inspect
        source = inspect.getsource(editor_agent)
        assert "system" in source, "editor_agent should have a system message"
        assert "user" in source, "editor_agent should have a user message"
        print("✅ All tests passed for editor_agent!")
    except Exception as e:
        print(f"❌ Test failed: {e}")
