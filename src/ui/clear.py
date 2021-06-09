from os import system, name

def clear() -> None:
    system('cls' if name == 'nt' else 'clear')