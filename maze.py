class maze:
  def __init__(self, rooms: List[Room], start_room: Room, monster: Monster):
    self._rooms = rooms
    self._start_room = start_room
    self._monster = monster

class Room:
  def __init__(self, name: str, description: str, sus_on_path: int, exits: Dict[str, Room],
               bosses: List[Boss], items: List[Items]):
    self._name = name
    self._description = description
    self._sus_on_path = sus_on_path
    self._exits = exits
    self._bosses = bosses
    self._items = items    
