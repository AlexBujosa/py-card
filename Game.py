import os

import random 
import math
import time

from Card import Card
from Player import Player, PlayerE
from typing import Dict

class Game:
    
    def __init__(self):
        self.symbol = ['♠', '♥', '♦', '♣']
        self.values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.deck = []
        self.shuffled_deck = []
        self.dead_deck = []
        self.current_player: Player = None
        
    def start_game(self):
        alternatePlayer: bool = True
        P1, P2= PlayerE
        players: Dict[PlayerE, Player] = {
            P1: Player(),
            P2: Player()
        }
        def getPlayer():
            return players[P1] if alternatePlayer  else players[P2]
        
        self.generate_card()
        self.shuffle_deck()
        self.distribute_cards(players)
    
        while True:
            self.current_player = getPlayer()
            self.GeneralOptions()
    
    def generate_card(self):
        for x in self.symbol:
            for y in self.values:
                self.deck.append(Card(x, y))
    
    def shuffle_deck(self):
        while len(self.deck) > 0:
            idx_card = math.floor(len(self.deck) * random.random())
            selected_card = self.deck.pop(idx_card)
            self.shuffled_deck.append(selected_card)
    
    def print_allCard(self):
        for card in self.shuffled_deck:
            card.draw_card()
    
    def distribute_cards(self, players: Dict[PlayerE, Player]):
        P1, P2= PlayerE
        
        for x in range(0, 10):
            if x % 2 == 0: 
                players[P1].append_Card(self.shuffled_deck.pop())
            else:
                players[P2].append_Card(self.shuffled_deck.pop())
                
    def GeneralOptions(self):
        isThrowedCard : bool = False
        option: int = 0
        
        def printOptions():
            self.clearScreen()
            print("Opciones: \n\n")
            print("1. Seleccionar Carta\n")
            print("2. Mostrar mis Cartas\n")
            print("3. Votar carta de tu mano\n\n")
        
        def takeAction():
            if(option == 1):
                self.SelectCardOptions()
            elif(option == 2):  
                self.current_player.showDeck() 
            elif(option == 3 and len(self.current_player.getDeck()) == 6):
                self.current_player.throwingUp()   
                         
            input("\nPress to continue... ")    
        while(isThrowedCard == False):
            printOptions()
            option_input = input("Elige una opcion putito ummmmm: ")
            try:
                option = int(option_input)
                if(option not in [1,2,3]):
                    print("El input no se encuentra en el rango de [1,2,3]")
                else:
                    takeAction()
            except ValueError:
                print("El input debe ser un numero entero")
                
    def SelectCardOptions(self):
        option: int = 0
        
        def printOptions():
            self.clearScreen()
            print("Opciones de Seleccion: \n\n")
            print("1. Seleccionar el mazo\n")
            print("2. Seleccionar del cementerio\n")
            print("3. Volver\n\n")
        
        def takeAction():
            if(option == 1):
                self.getCardFromShuffledDeck()
            elif(option == 2):  
                self.getCardFromDeadDeck()
            input("\nPress to continue... ")   
                             
        while(option not in [1,2,3]):
            printOptions()
            option_input = input("Elige una opcion putito ummmmm: ")
            try:
                option = int(option_input)
                takeAction()
            except ValueError:
                print("El input debe ser un numero entero")
                
    def clearScreen(self):
        _ = os.system('cls')
        
    def getCardFromShuffledDeck(self) -> None:
        if(len(self.current_player.getDeck()) > 5):
            print("No puedes seleccionar mas del mazo, tienes que votar :V ")
            return
        card = self.shuffled_deck.pop()
        self.current_player.append_Card(card)
        
    def getCardFromDeadDeck(self) -> None:
        if(len(self.current_player.getDeck()) > 5):
            print("No puedes seleccionar carta, tienes que votar :V ")
            return
        elif(len(self.dead_deck) == 0):
            print("No hay cartas en el dead deck:V ")
            return
        
        card = self.dead_deck.pop()
        self.current_player.append_Card(card)