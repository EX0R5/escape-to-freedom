class Dialogue:
    """
    Defines a dialogue object.
  
    Attributes:
    display_text (str): text to be displayed
    gift_item (Item): any items that will be given when the dialogue runs
    added_sus (int): suspicion level increment if the dialogue runs
    options (List[Dialogue]): the next dialogue options
    """
    def __init__(self, display_text: str, gift_item: Item, added_sus: int, options: List[Dialogue]) -> None:
        self._display_text = display_text
        self._gift_item = gift_item
        self._added_sus = added_sus
        self._options = options

    def get_display_text(self) -> str:
        return self._display_text

    def get_gift_item(self) -> Item:
        return self._gift_item

    def get_added_sus(self) -> int:
        return self._added_sus

    def get_options(self) -> List[Dialogue]:
        return self._options
