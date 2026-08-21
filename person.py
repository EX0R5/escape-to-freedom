class Person:
  """
  Defines a person.

  Attributes:
  name (str): the name of the person
  current_room (Room): the room the person is in
  inventory (List[item]): items that the person has
  information (List[Dict[str, str]]): the pieces of information that the person has, can be true or false
  """
  def __init__(self, name, current_room) -> None:
    self.name = name
    self.current_room = current_room
    self.inventory = None
    self.information = None
