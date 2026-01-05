import random
from enum import IntEnum


class GameAction(IntEnum):

    Rock = 0
    Paper = 1
    Scissors = 2

class Agent:
    def __init__(self):
        self.user_history = []
        self.results_history = []

    def update_history(self,user_move : GameAction, result: str):
        self.user_history.append(user_move)
        self.results_history.append(result)

    def last_pick(self):
        return self.user_history[-1] if self.user_history else None    

    def last_results(self, n=3):
        return self.results_history[-n:] if len(self.results_history) >= n else self.results_history

class ModelBasedReflexStrategy:
    def choose_action(self, state: Agent) -> GameAction:
        last = state.last_pick()
        last_results = state.last_results(3)
        
        # New strategy in case we detect the rival knows our strategy
        if len(last_results) == 3 and all(r == "loss" for r in last_results):
            return GameAction(last)
        
        # History strategy
        if last is None:
            return random.choice(list(GameAction))
        return GameAction((last + 1) % 3)

# Initialize new classes
agent_state = Agent()
strategy = ModelBasedReflexStrategy()

def assess_game(user_action, computer_action):
    if user_action == computer_action:
        print(f"User and computer picked {user_action.name}. Draw game!")
        return "draw"

    elif user_action == GameAction.Rock:
        if computer_action == GameAction.Scissors:
            print("Rock smashes scissors. You won!")
            return "loss"  # perspectiva del computador
        else:
            print("Paper covers rock. You lost!")
            return "win"

    elif user_action == GameAction.Paper:
        if computer_action == GameAction.Rock:
            print("Paper covers rock. You won!")
            return "loss"
        else:
            print("Scissors cuts paper. You lost!")
            return "win"

    elif user_action == GameAction.Scissors:
        if computer_action == GameAction.Rock:
            print("Rock smashes scissors. You lost!")
            return "win"
        else:
            print("Scissors cuts paper. You won!")
            return "loss"


def get_computer_action():
    computer_action = strategy.choose_action(agent_state)
    print(f"Computer picked {computer_action.name}.")

    return computer_action


def get_user_action():
    # Scalable to more options (beyond rock, paper and scissors...)
    game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
    game_choices_str = ", ".join(game_choices)
    user_selection = int(input(f"\nPick a choice ({game_choices_str}): "))
    user_action = GameAction(user_selection)

    return user_action


def play_another_round():
    another_round = input("\nAnother round? (y/n): ")
    return another_round.lower() == 'y'


def main():

    while True:
        try:
            user_action = get_user_action()
        except ValueError:
            range_str = f"[0, {len(GameAction) - 1}]"
            print(f"Invalid selection. Pick a choice in range {range_str}!")
            continue

        computer_action = get_computer_action()
        result = assess_game(user_action, computer_action)
        agent_state.update_history(user_action, result)

        if not play_another_round():
            break


if __name__ == "__main__":
    main()