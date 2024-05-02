from Cursor import Cursor

class Card: 
    def __init__(self, symbol: str, value: str):
        self.symbol = symbol
        self.value  = value
        
    def draw_card(self, x, y):
        card = ["------------", f"|{self.symbol}         |", "|          |", f"|    {self.value}     |", "|          |", f"|         {self.symbol}|", "------------"]
        cursor = Cursor()
        for idx, cardPart in enumerate(card):
            cursor.print_at_position(x, y + idx, cardPart)
            