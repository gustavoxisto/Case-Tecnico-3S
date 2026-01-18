import math
from dataclasses import dataclass

@dataclass
class BoardGameInfo:
    min_turns: int
    optimal_probability: float
    no_loop_combinations: int

class BoardGame:

    def __init__(self, board_size: int):
        if board_size < 3:
            raise ValueError("Board size must be at least 3.")
        
        self.board_size = board_size
        self.distance = board_size - 1
        self._min_turns = None
        self._optimal_sequences = None
        self._optimal_probability = None
        self._no_loop_combinations = None
        self._paths_cache = {}

    def get_min_turns(self) -> int:
        return self._get_min_turns()

    def get_optimal_probability(self) -> float:
        return self._get_optimal_probability()

    def get_no_loop_combinations(self) -> int:
        return self._get_no_loop_combinations()

    def get_info(self) -> BoardGameInfo:
        return BoardGameInfo(
            min_turns= self.get_min_turns(),
            optimal_probability= self.get_optimal_probability(),
            no_loop_combinations= self.get_no_loop_combinations()
        )
    
    def _get_min_turns(self) -> int:
        if self._min_turns is None:
            self._min_turns = math.ceil(self.distance / 3)
        return self._min_turns

    def _get_optimal_sequences(self) -> int:
        if self._optimal_sequences is None:
            remainder = self.distance % 3
            if remainder == 0:
                self._optimal_sequences = 1
            else:
                self._optimal_sequences = self._get_min_turns()
        return self._optimal_sequences

    def _get_optimal_probability(self) -> float:
        if self._optimal_probability is None:
            min_turns = self._get_min_turns()
            optimal_sequences = self._get_optimal_sequences()
            self._optimal_probability = optimal_sequences / (3 ** min_turns)
        return self._optimal_probability

    def _count_paths(self, remaining: int) -> int:
        if remaining in self._paths_cache:
            return self._paths_cache[remaining]
        
        if remaining == 0:
            return 1
        if remaining < 0:
            return 0
        
        result = (
            self._count_paths(remaining - 1)
            + self._count_paths(remaining - 2)
            + self._count_paths(remaining - 3)
        )
        
        self._paths_cache[remaining] = result
        return result

    def _get_no_loop_combinations(self) -> int:
        if self._no_loop_combinations is None:
            self._no_loop_combinations = self._count_paths(self.distance)
        return self._no_loop_combinations


if __name__ == '__main__':
    range_test = [3, 4, 5, 6, 7, 8, 9, 10]
    for number in range_test:
        game = BoardGame(number)
        result = game.get_info()
        print(f"Result for board size {number}: {result}")