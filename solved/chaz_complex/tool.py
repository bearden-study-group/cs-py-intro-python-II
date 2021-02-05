from item import Item
from enum import IntEnum


class ToolClass(IntEnum):
    DIAMOND = 5
    GOLD = 4
    IRON = 3
    STONE = 2
    WOOD = 1


class Tool(Item):
    def __init__(self,
                 name,
                 weight,
                 damage,
                 health,
                 clazz: ToolClass
                 ):
        super().__init__(name, weight)
        self.damage = damage
        self.health = health
        self.clazz = clazz
        self.interval = 0.05 * float(self.clazz)

    def use(self):
        self.health -= self.interval


if __name__ == '__main__':
    diamond_sword = Tool("sword", 10, 20, 10, ToolClass.DIAMOND)
    print(diamond_sword.health)
    print(diamond_sword.interval)
    diamond_sword.use()
    print(diamond_sword.health)
