from abc import ABC, abstractmethod

class agent(ABC):
    """
    A representation of the agent.
    """

    @abstractmethod
    def choose(board):
        """
        Return the board with the move choose but the agent.
        """
        return board

    @abstractmethod
    def do_rollout(board):
        return None
