class Item:
  def __init__(self, name: str, description: str):
    self.name = name
    self.description = description

class Map(Item):
   def __init__(self, name: str, description: str, vicinity: int):
     super().__init__(name, description)
     self.vicinity = vicinity

class Weapon(Item):
  def __init__(self, name: str, description: str, damage: int):
     super().__init__(name, description)
     self.damage = damage
    
class HealthItem(Item):
  def __init__(self, name: str, description: str, heal: int):
    super().__init__(name, description)
    self.heal = heal

class StealthItem(Item):
  def __init__(self, name: str, description: str):
    super().__init__(name, description)
