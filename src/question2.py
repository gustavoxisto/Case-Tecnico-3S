def get_sequence_value(position: int) -> int:
    first_term = 11
    common_difference = 7
    return first_term + (position - 1) * common_difference

if __name__ == '__main__':
    print(get_sequence_value(1))        # 11
    print(get_sequence_value(2))        # 18
    print(get_sequence_value(200))      # 1404
    print(get_sequence_value(254))      # 1782
    print(get_sequence_value(3542158))  # 24795110
