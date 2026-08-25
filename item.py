class Item:
    """
    Defines an item.

    Attributes:
    name (str): name of item
    description (str): description of item
    """
    def __init__(self, name: str, description: str) -> None:
        self._name = name
        self._description = description

class Map(Item):
    """
    Defines a map.

    Additional attributes:
    vicinity (int): the number of rooms away from current room that the map will reveal
    """
    def __init__(self, name: str, description: str, vicinity: int) -> None:
        super().__init__(name, description)
        self._vicinity = vicinity

class Weapon(Item):
    """
    Defines a weapon.

    Additional attributes:
    damage (int): damage of weapon
    """
    def __init__(self, name: str, description: str, damage: int) -> None:
        super().__init__(name, description)
        self._damage = damage
    
class HealthItem(Item):
    """
    Defines an item that heals you.

    Additional attributes:
    heal (int): the number of HP that the item heals you on use
    """
    def __init__(self, name: str, description: str, heal: int) -> None:
        super().__init__(name, description)
        self._heal = heal

class StealthItem(Item):
  def __init__(self, name: str, description: str):
    super().__init__(name, description)
