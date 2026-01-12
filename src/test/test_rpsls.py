import pytest
from rps.RPS_LizzardSpock import GameAction, Agent, ModelBasedReflexStrategy, assess_game

def test_assess_game_extended_rules():
# Check new rules of lizzard and spock
    assert assess_game(GameAction.Spock, GameAction.Scissors) == "loss"
    assert assess_game(GameAction.Lizzard, GameAction.Spock) == "loss"
    assert assess_game(GameAction.Lizzard, GameAction.Rock) == "win"
    assert assess_game(GameAction.Spock, GameAction.Spock) == "draw"

def test_alt_strategy_activation():
# Check if after 3 consecutive losses the alternative strategy works
    agent = Agent()
    strategy = ModelBasedReflexStrategy()

    for _ in range(3):
        agent.update_history(GameAction.Paper, "loss")

    action = strategy.choose_action(agent)
    assert agent.alt_strategy_rounds == 2
    assert action == GameAction.Paper

def test_agent_history_limit():
# Verify that last_results() gives the correct number
    agent = Agent()
    for i in range(5):
        agent.update_history(GameAction.Rock, "win")
    
    results = agent.last_results(3)
    assert len(results) == 3
    assert all(r == "win" for r in results)

def test_invalid_action_handling():
# Check that user cant go out of the range of possibilities
    with pytest.raises(ValueError):
        GameAction(5)