from abc import ABC, abstractmethod

class agent(ABC):
    """
    A representation of the agent.
    """
    agent_name = "agent"

    @abstractmethod
    def choose(board):
        """
        Return the board with the move choose but the agent.
        """
        return board

    @abstractmethod
    def do_rollout(board):
        return None

    @abstractmethod
    def train_model(self, total_games, learning_rate =0.9, loadPre = True):
        return None
