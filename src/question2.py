"""
    Considerando a sequência numérica a seguir (11, 18, 25, 32, 39... ) faça uma função que recebe como entrada uma posição e devolve 
    qual o valor do número naquela posição, considerando a sequência numérica apresentada, para todos os efeitos, a sequência começa 
    da posição 1.
    
    Ex:
        print_valor(x=1) retornará 11; print_valor(x=2) retornará 18; print_valor(x=200) retornará 1404;
        print_valor(x=254) retornará 1.782;
        print_valor(x=3.542.158) retornará 24.795.110;
"""

first_term = 11
common_difference = 7

def get_sequence_value(position: int) -> int:
    return first_term + (position - 1) * common_difference

if __name__ == '__main__':
    print(get_sequence_value(1))        # 11
    print(get_sequence_value(2))        # 18
    print(get_sequence_value(200))      # 1404
    print(get_sequence_value(254))      # 1782
    print(get_sequence_value(3542158))  # 24795110
