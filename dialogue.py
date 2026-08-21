class Dialogue:
  def __init__(self, display_text: str, gift_item: Item, added_sus: int, options: List[Dialogue]):
    self.display_text = display_text
    self.gift_item = gift_item
    self.added_sus = added_sus
    self.options = options
