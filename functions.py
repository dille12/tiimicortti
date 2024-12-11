from typing import List, Tuple, TYPE_CHECKING

if TYPE_CHECKING:
    from card import Card
    from node import Node
    from nodeMaker import Game

def add(n1: int, n2: int) -> int:
    return n1 + n2

def minus(n1: int, n2: int) -> int:
    return n1 - n2

def Multiply(n1: int, n2: int) -> float:
    return n1 * n2

def GameTurnsPassed(GAME: "Game") -> int:
    return GAME.turnsPassed

def beersDrank() -> int:
    return 5

def balls() -> int:
    return 2

def one() -> int:
    return 1

def zero() -> int:
    return 0



def Display(NODE: "Node", n) -> None:
    NODE.disp = n

def CardAttack(PARENT: "Card") -> int:
    return PARENT.attack

def setCardAttack(NODE: "Node", CARD: "Card", n1: int) -> None:
    CARD.attack = n1
    NODE.disp = CARD.attack

def ParentCard(PARENT: "Card") -> "Card":
    return PARENT

def isGreater(n1: int, n2: int) -> bool:
    if n1 <= n2:
        return False
    else:
        return True

def ifElse(b: bool, n1, n2):
    if b:
        return n1
    else:
        return n2
    

def dualNum() -> Tuple[int, int]:
    return 1, 2


def getAttribute(PARENT: "Card", NODE: "Node") -> int:
    """
    DROPDOWN
    attack
    health
    mana
    level
    """
    return PARENT.__dict__[NODE.dropDown.dropDownSelections[NODE.dropDown.dropDownIndex]]

def setAttribute(PARENT: "Card", NODE: "Node", n1: int) -> None:
    """
    DROPDOWN
    attack
    health
    mana
    level
    """
    PARENT.__dict__[NODE.dropDown.dropDownSelections[NODE.dropDown.dropDownIndex]] = n1
    NODE.disp = n1