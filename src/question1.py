"""
    Escreva uma função que determina se uma string termina com 'A' e começa com 'B'.
"""

def starts_with_b_and_ends_with_a(text: str) -> bool:
    return text.upper().startswith('B') and text.upper().endswith('A')

print(starts_with_b_and_ends_with_a("BANANA"))   # True
print(starts_with_b_and_ends_with_a("BOLA"))     # True
print(starts_with_b_and_ends_with_a("BETA"))     # True
print(starts_with_b_and_ends_with_a("bETA"))     # True
print(starts_with_b_and_ends_with_a("COLA"))     # False
print(starts_with_b_and_ends_with_a("BINOCULO"))     # False
