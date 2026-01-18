""" 
    Um jogo com tabuleiro unidirecional comporta dois jogadores. Vence quem chegar primeiro a última casa do tabuleiro com menos turnos.

    Para caminhar com as peças, os jogadores utilizam uma roleta que sorteia se devem andar 1, 2 ou 3 casas.

    Caso tire um número maior na roleta, que casas faltantes, o jogador deve iniciar novamente o percurso (como um looping), por exemplo, 
    se faltam apenas duas casas para eu ganhar, e tiro 3 na roleta, devo caminhar as duas faltantes mais uma até a primeira casa do 
    tabuleiro, reiniciando todo o percurso.

    Regra: O tamanho mínimo do tabuleiro deve ser 3 casas sem um máximo.
    
    Crie uma função que recebe o número de casas do tabuleiro e devolve:
        1 - Quantidade mínimo de turnos para se chegar ao destino (caminho ótimo);
        2 - Probabilidade de um usuário conseguir executar o caminho ótimo;
        3 - Quantas combinações de movimentos diferentes um jogador conseguiria executar sem efetuar nenhum looping no tabuleiro.
"""

import math

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

    def get_min_turns(self) -> int:
        return self._get_min_turns()

    def get_optimal_probability(self) -> float:
        return self._get_optimal_probability()

    def get_no_loop_combinations(self) -> int:
        return self._get_no_loop_combinations()

    def get_info(self) -> dict:
        return {
            "min_turns": self.get_min_turns(),
            "optimal_probability": self.get_optimal_probability(),
            "no_loop_combinations": self.get_no_loop_combinations()
        }

if __name__ == '__main__':
    for number in [3, 4, 5, 6, 7, 8, 9, 10]:
        game = BoardGame(number)
        result = game.get_info()
        print(f"Result for board size {number}: {result}")