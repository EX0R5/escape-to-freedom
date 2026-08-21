class Item:
  def __init__(self, name: str, description: str):
    self._name = name
    self._description = description

class Map(Item):
   def __init__(self, name: str, description: str, vicinity: int):
     super().__init__(name, description)
     self._vicinity = vicinity

class Weapon(Item):
  def __init__(self, name: str, description: str, damage: int):
     super().__init__(name, description)
     self._damage = damage
    
class HealthItem(Item):
  def __init__(self, name: str, description: str, heal: int):
    super().__init__(name, description)
    self._heal = heal

class StealthItem(Item):
  def __init__(self, name: str, description: str):
    super().__init__(name, description)
