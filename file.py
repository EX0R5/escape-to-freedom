import csv

class File:
  """
  Defines the uploading of a file onto the server.

  Attributes:
  _name (str): the name of the file
  _data (List[Dict]): the data in the file
  """
  def __init__(self, name: str, fieldnames=None: List[str], data=None: List[Dict]) -> None:
    self._name = name
    self._fieldnames = fieldnames
    self._data = data

  def get_name(self) -> str:
    return self._name

  def get_fieldnames(self) -> List[str]:
    return self._fieldnames

  def set_fieldnames(self, fieldnames: List[str]) -> None:
    self._fieldnames = fieldnames

  def read(self) -> None:
    """
    Read the file with given name and store it in data.

    Attributes: None
    Returns: None
    """
    data = []
    with open(self.get_name(), "r") as f:
      reader = csv.DictReader(f)
      self.set_fieldnames(reader.fieldnames())
      for row in reader:
        data.append(row)

    self._data = data

def is_empty(self) -> bool:
  """
  Checks if file is empty.

  Attributes: None
  Returns: True if empty, else False.
  """
  self.read()
  return self._data == []
  
def append(self, data: List[Dict]) -> None:
  """
  Appends new data to the file.

  Attributes:
  data (List[Dict]): the data to be added

  Returns: None
  """
  with open(self.get_name(), "a") as f:
    writer = csv.DictWriter(f, fieldnames=self.get_fieldnames())
    if self.is_empty():
      writer.writeheader()
    for row in data:
      writer.writerow(row)
