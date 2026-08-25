class Dialogue:
    """
    Defines a dialogue object.
  
    Attributes:
    display_text (str): text to be displayed
    gift_item (Item): any items that will be given when the dialogue runs
    added_sus (int): suspicion level increment if the dialogue runs
    options (List[Dialogue]): the next dialogue options
    """
    def __init__(self, display_text: str, gift_item: Item, added_sus: int, options: List[Dialogue]):
        self._display_text = display_text
        self._gift_item = gift_item
        self._added_sus = added_sus
        self._options = options
