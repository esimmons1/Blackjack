# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 22:04:43 2023

@author: simmo
"""

import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def value(self):
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 11
        else:
            return int(self.rank)

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
                self.cards.append(Card(rank, suit))
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []

    def addCard(self, card):
        self.cards.append(card)

    def value(self):
        value = sum(card.value() for card in self.cards)
        numAces = sum(1 for card in self.cards if card.rank == 'A')
        while value > 21 and numAces:
            value -= 10
            numAces -= 1
        return value

def printHand(hand, dealer=False, revealDealer=False):
    if dealer:
        print("Dealer's hand:")
        if not revealDealer:
            print(" <hidden card>")
            for card in hand.cards[1:]:
                print(f" {card.rank} of {card.suit}")
        else:
            for card in hand.cards:
                print(f" {card.rank} of {card.suit}")
            print(f"Total value: {hand.value()}")
        print()
    else:
        print("Your hand:")
        for card in hand.cards:
            print(f" {card.rank} of {card.suit}")
        print(f"Total value: {hand.value()}\n")

def playBlackjack():
    deck = Deck()
    playerHand = Hand()
    dealerHand = Hand()

    # Initial deal
    playerHand.addCard(deck.draw())
    dealerHand.addCard(deck.draw())
    playerHand.addCard(deck.draw())
    dealerHand.addCard(deck.draw())

    printHand(dealerHand, dealer=True, revealDealer=False)
    printHand(playerHand)

    # Player's turn
    while playerHand.value() < 21:
        action = input("Do you want to hit or stand? (h/s): ").strip().lower()
        if action == 'h':
            card = deck.draw()
            playerHand.addCard(card)
            print(f"You got a: {card.rank} of {card.suit}\n")
            printHand(playerHand)
        elif action == 's':
            break
        else:
            print("Invalid input. Please enter 'h' or 's'.")

    if playerHand.value() > 21:
        print("You bust! Dealer wins.")
        return

    # Dealer's turn
    print("\nDealer's turn:")
    printHand(dealerHand, dealer=True, revealDealer=True)

    while dealerHand.value() < 17:
        card = deck.draw()
        dealerHand.addCard(card)
        print(f"Dealer draws: {card.rank} of {card.suit}")
        printHand(dealerHand, dealer=True, revealDealer=True)

    # Final outcome
    playerTotal = playerHand.value()
    dealerTotal = dealerHand.value()

    print(f"\nYour total: {playerTotal}")
    print(f"Dealer's total: {dealerTotal}")

    if dealerTotal > 21 or dealerTotal < playerTotal:
        print("You win!")
    elif dealerTotal > playerTotal:
        print("Dealer wins!")
    else:
        print("It's a tie!")

playBlackjack()
