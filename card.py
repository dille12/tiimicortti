import random
from node import getNodes, Node

class Card:
    def __init__(self, game):
        self.game = game

        self.attack = random.randint(1,5)
        self.health = 10
        self.mana = 10
        self.level = 2
        self.name = "Paska"
        self.nodes = {"On Attack" : [], "On Take Damage" : [], "On Special Ability" : []}
        self.nodeListKeys = list(self.nodes.keys())
        self.nodeListIndex = 0

        NODES = getNodes(self, self.game)
        print("NODES:", NODES)
        for x in NODES:
            self.nodes[random.choice(self.nodeListKeys)].append(x)

    
