import person

class Maze:
    def __init__(self, rooms: Dict[str, Room], start_room: Room, monster: person.Monster):
        """
        Defines a Maze.

        Attributes:
        rooms (Dict[str, Room]): rooms in the maze
        start_room (Room): starting room
        monster (Monster): the monster in the maze
        """
        self._rooms = rooms
        for room_key in rooms:
            room = rooms[room_key]
            exits = room.get_exits()
            for exit_key in exits:
                exits[exit_key] = rooms[exits[exit_key]]
        self._start_room = start_room
        self._monster = monster

    def get_rooms(self) -> Dict[str, Room]:
        return self._rooms

    def set_rooms(self, value: Dict[str, Room]) -> None:
        self._rooms = value

    def get_start_room(self) -> Room:
        return self._start_room

    def set_start_room(self, value: Room) -> None:
        self._start_room = value

    def get_monster(self) -> person.Monster:
        return self._monster

    def set_monster(self, value: person.Monster) -> None:
        self._monster = value

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
               bosses: List[person.Boss], items: List[Items]) -> None:
        self._id = id
        self._name = name
        self._description = description
        self._sus_on_path = sus_on_path
        self._exits = {}
        for exit in exits:
            if exits[exit] is not None and exits[exit] != "None":
                self._exits[exit] = exits[exit]
        self._bosses = bosses
        self._items = items

    def get_id(self) -> str:
        return self._id

    def set_id(self, value: str) -> None:
        self._id = value

    def get_name(self) -> str:
        return self._name

    def set_name(self, value: str) -> None:
        self._name = value

    def get_description(self) -> str:
        return self._description

    def set_description(self, value: str) -> None:
        self._description = value

    def get_sus_on_path(self) -> int:
        return self._sus_on_path

    def set_sus_on_path(self, value: int) -> None:
        self._sus_on_path = value

    def get_exits(self) -> Dict[str, Room]:
        return self._exits

    def set_exits(self, value: Dict[str, Room]) -> None:
        if value[1] == None:
            try:
                del self._exits[value[0]]
            except KeyError:
                pass
        else:
            self._exits[value[0]] = value[1]

    def get_bosses(self) -> List[person.Boss]:
        return self._bosses

    def set_bosses(self, value: List[person.Boss]) -> None:
        self._bosses = value

    def get_items(self) -> List[Items]:
        return self._items

    def set_items(self, value: List[Items]) -> None:
        self._items = value
