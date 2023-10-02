# The Game of Wheels

Inspired by the mini-game ['Wheels' from Sea of Stars](https://seaofstars.fandom.com/wiki/Wheels), this is a recreation by Donovan Townes a.k.a Z8phyR. The primary objective is to destroy the enemy's crown before they get to yours.

## How to Play

1. Players will first select two heroes each. These heroes have unique abilities that influence the game.
2. Once the heroes are selected, players will spin a wheel to gain resources.
3. Depending on the spin result, heroes gain energy, experience, and there's a possibility to damage the enemy's defenses.
4. The game continues until one of the players' crowns is destroyed.

5. In depth gameplay mechanics can be found in the gameplay.md file.

## Technical Details

The game is built using Python with a strong emphasis on Object-Oriented Programming (OOP). The game consists of multiple classes such as `Player`, `Hero`, `Wheel`, and `Game` to modularize different functionalities.

### Key Challenges

- **Dynamic Hero Selection**: Implementing a system where players can choose from various heroes, each with its unique abilities, posed a design challenge.
- **Spin Logic**: Given the randomness of a spin, calculating the results and their impacts on the player's resources (XP, energy) required meticulous logic.
- **Scaling**: As heroes gain XP and level up, managing their state, especially when they reach the maximum level, was challenging.
- **NPC Logic**: Simulating an NPC turn, making it appear as if the computer player is making decisions, was an interesting challenge.

## Installation & Usage

1. Ensure you have Python installed.
2. Clone this repository: `git clone https://github.com/Z8phyR/GameOfWheels.git`
3. Navigate to the directory: `cd GameOfWheels`
4. Run the game: `python main.py`

## Contribution

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
