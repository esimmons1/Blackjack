Blackjack Game
==============

Made by: Ellis Simmons, Fall 2024    
Language: Python  

---

What this is:  
A command-line version of the classic casino game **Blackjack**. Play against the dealer, draw cards, and try to get as close to 21 as possible without going over.

---

How to play:  
- Run the script, and the game will deal 2 cards each to you and the dealer.  
- You can choose to:  
  - **Hit** (draw a card)  
  - **Stand** (end your turn)  
- The dealer reveals their cards after you stand or bust.  
- Dealer draws cards until they reach at least 17.  
- Closest to 21 wins without going over.

---

How it works:  
The game is made up of several classes:

- **`Card`**  
  Represents a single card. Handles rank and suit. Face cards (`J`, `Q`, `K`) are worth 10 points. Aces are 11 by default but drop to 1 if you would bust.

- **`Deck`**  
  Creates a standard 52 card deck. Shuffles and handles drawing.

- **`Hand`**  
  Keeps track of cards in a player's hand. Computes total value, adjusting for aces.

- **`printHand()`**  
  Prints the visible cards in either your hand or the dealer's. Hides one dealer card until your turn is over.

- **`playBlackjack()`**  
  Runs the actual game loop:  
  - Deals cards  
  - Handles player input  
  - Automates dealer decisions  
  - Declares winner

---

Notes:  
- Terminal-based, no GUI.  
- Dealer stands on 17.  
- Handles multiple aces properly.  
- Basic input validation included.

---

Running the game:  
Just run it in a Python interpreter:  

```bash
python blackjack.py
```

As per usual, if you're going to steal or use it at least credit me please. Thank you for reading and have a nice day.
