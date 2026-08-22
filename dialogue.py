class Dialogue:
  def __init__(self, display_text: str, gift_item: Item, added_sus: int, options: List[Dialogue]):
    self._display_text = display_text
    self._gift_item = gift_item
    self._added_sus = added_sus
    self._options = options
