from rps.RPS_Implementacion import GameAction, Agent, ModelBasedReflexStrategy, assess_game

def test_assess_game_logic():
# Check of a correctly logic of the rules
    assert assess_game(GameAction.Rock, GameAction.Scissors) == "loss"
    assert assess_game(GameAction.Rock, GameAction.Paper) == "win"     
    assert assess_game(GameAction.Rock, GameAction.Rock) == "draw"

def test_strategy_reflex_logic():
# Check the basic functionality of the agent of picking last opponent move
    agent = Agent()
    strategy = ModelBasedReflexStrategy()

    agent.update_history(GameAction.Rock, "win")
    action = strategy.choose_action(agent)
    assert action == GameAction.Paper

def test_alt_strategy_activation():
# Check if after 3 consecutive losses the alternative strategy works
    agent = Agent()
    strategy = ModelBasedReflexStrategy()
    
    for _ in range(3):
        agent.update_history(GameAction.Rock, "loss")

    action = strategy.choose_action(agent)
    assert agent.alt_strategy_rounds == 2
    assert action == GameAction.Rock

def test_history_tracking():
# Check if the history its updating
    agent = Agent()
    agent.update_history(GameAction.Scissors, "win")
    assert agent.last_pick() == GameAction.Scissors
    assert agent.results_history == ["win"]