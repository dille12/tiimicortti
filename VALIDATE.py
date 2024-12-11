from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from card import Card
    from node import Node

def add(n1: int, n2: int) -> int:
    if not isinstance(n1, int) or not isinstance(n2, int):
        raise ValueError("Both arguments to add must be integers.")
    return n1 + n2

def minus(n1: int, n2: int) -> int:
    if not isinstance(n1, int) or not isinstance(n2, int):
        raise ValueError("Both arguments to minus must be integers.")
    return n1 - n2

def Multiply(n1: int, n2: int) -> float:
    if not isinstance(n1, (int, float)) or not isinstance(n2, (int, float)):
        raise ValueError("Both arguments to Multiply must be int or float.")
    return n1 * n2

def beersDrank() -> int:
    # No inputs to validate here, the function always returns 5
    return 5

def balls() -> int:
    # No inputs to validate here, the function always returns 2
    return 2

def Display(NODE: "Node", n1: int) -> None:
    if not isinstance(NODE, Node):
        raise ValueError("NODE must be an instance of Node.")
    if not isinstance(n1, int):
        raise ValueError("n1 must be an integer.")
    NODE.disp = n1

def CardAttack(PARENT: "Card") -> int:
    if not isinstance(PARENT, Card):
        raise ValueError("PARENT must be an instance of Card.")
    if not hasattr(PARENT, 'attack') or not isinstance(PARENT.attack, int):
        raise ValueError("PARENT must have an integer 'attack' attribute.")
    return PARENT.attack

def setCardAttack(NODE: "Node", PARENT: "Card", n1: int) -> None:
    if not isinstance(NODE, Node):
        raise ValueError("NODE must be an instance of Node.")
    if not isinstance(PARENT, Card):
        raise ValueError("PARENT must be an instance of Card.")
    if not isinstance(n1, int):
        raise ValueError("n1 must be an integer.")
    if not hasattr(PARENT, 'attack'):
        raise ValueError("PARENT must have an 'attack' attribute.")
    print("Setting attack as", n1)
    PARENT.attack = n1
    NODE.disp = PARENT.attack

def ParentCard(PARENT: "Card") -> "Card":
    if not isinstance(PARENT, Card):
        raise ValueError("PARENT must be an instance of Card.")
    return PARENT
