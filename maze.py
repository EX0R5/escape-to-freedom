class Maze:
    def __init__(self, rooms: list[Room], start_room: Room, monster: Monster):
        """
        Defines a Maze.

        Attributes:
        rooms (List[Room]): rooms in the maze
        start_room (Room): starting room
        monster (Monster): the monster in the maze
        """
        self._rooms = rooms
        self._start_room = start_room
        self._monster = monster

class Room:
    """
    Defines a Room.

    Attributes:
    name (str): name of room
    description (str): description of room
    sus_on_path (int): suspicion increased on entering room
    exits (Dict[str, Room]): exits of the room
    bosses (List[Boss]): bosses found in room
    items (List[Items]): items found in room
    """
    def __init__(self, id: str, name: str, description: str, sus_on_path: int, exits: Dict[str, Room],
               bosses: List[Boss], items: List[Items]) -> None:
        self._id = id
        self._name = name
        self._description = description
        self._sus_on_path = sus_on_path
        self._exits = exits
        self._bosses = bosses
        self._items = items
