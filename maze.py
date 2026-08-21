class maze:
  def __init__(self, rooms: List[Room], start_room: Room, monster: Monster):
    self.rooms = rooms
    self.start_room = start_room
    self.monster = monster

class Room:
  def __init__(self, name: str, description: str, sus_on_path: int, exits: Dict[str, Room],
               bosses: List[Boss], items: List[Items]):
    self.name = name
    self.description = description
    self.sus_on_path = sus_on_path
    self.exits = exits
    self.bosses = bosses
    self.items = items    
