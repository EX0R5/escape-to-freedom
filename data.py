import csv

class File:
  """
  Defines the uploading of a file onto the server.

  Attributes:
  _name (str): the name of the file
  _data (List[Dict]): the data in the file
  """
  def __init__(self, name) -> None:
    self._name = name
    self._data = None

  def get_name(self) -> str:
    return self._name

  def read(self) -> None:
    data = []
    with open(self.get_name()) as f:
      reader = csv.DictReader(f)
      for row in reader:
        data.append(row)

    self._data = data
