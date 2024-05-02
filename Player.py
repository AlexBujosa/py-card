from Card import Card
from enum import Enum
from Cursor import Cursor

class Player: 
    def __init__(self):
        self.deck : list[Card] = []
    
    def pickUp(self):
        print("Picking up a card!!!")
        
    def throwingUp(self): 
        print("Throwing up a card!")
        
    def append_Card(self, card: Card):
        if len(self.deck) < 6: 
            self.deck.append(card)
            return
        
        print("Out of range, can not be above 6!!!")
        
    
    def getDeck(self) -> list[Card]: 
        return self.deck
    
    def showDeck(self): 
        for idx, card in enumerate(self.deck):
            card.draw_card(5 + 14 * idx, 15)
        

class PlayerE(Enum):
    P1 = 1
    P2 = 2