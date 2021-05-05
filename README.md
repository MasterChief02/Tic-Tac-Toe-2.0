# Tic-Tac-Toe-2.0


## Introduction
As the name suggests, the game mainly provides an interface for users to play Tic-Tac-Toe. It allows users to play over the internet with players across the globe in real-time. It also allows users to play over the local network. And at its core, the user can also play against the computer, that **doesn't simply use** `random()`. Play against option is supported by the use of **Reinforcement Learning**, where the computer itself identifies all possible outcomes and depending on that, makes its move. So it is somewhat extremely difficult to win against the computer, but still, it is not a very perfect artificial intelligent system, as up to now there is one geometrically unique way to win against the computer has been identified.


## Play Online
This option allows users, present across the globe, to play against each other. As a standard multiplayer game, a user is given a time of 30 seconds to make his move, and the cycle goes on until either of them wins or there are no more possible moves. To have such functionality, **Google Firebase Real-Time Database** is used. Currently, due to the limitations of the free account on firebase, only maximum of 50 games can be played at any interval of time, and the code is also created for only 50 games, although it can be easily modified to support any given maximum number of games.


## Play Locally
This option allows the user to play with another user present on the same local network. We assume that the two players can communicate with each other, and thus there is no time limit for moves in this mode. If needed, a time limit can be easily added to this mode as well in a similar manner, as used play online mode. To have such functionality, the `socket` library is used. One computer hosts the game on the local network, while the second computer joins the game using the number provided by the host system. The data transfer across the network takes place only when a move is made.


## Play Against AI
This is the most auspicious option present in the game, as per the point of view of a developer. It is not a simple illustration of the `random` module, instead, it is a basic and yet effective example of **Reinforcement Learning**. The option itself has two more options- user first and AI-first. If the AI-first option is selected, then the computer makes its first move using the `random()` function. But in all other cases, it first detects all the available options to make a move. Then for each option, it simulates all the possible games and determines their outcomes. Depending on this data, it assigns a score to each available option, and then the system makes its move for the option with maximum score. This method is used mainly for the hard mode. For ease of users, two other modes- easy and medium, are also provided which also follows the same principle, but differs only in the selection method of the move. To make the game interactive, the character of AI also makes some comments sometimes.


## Testing The Game
As a developer, one can test the game by running the `Tic-Tac-Toe.py` script. The end-user can directly extract the 'Tic-Tac-Toe 2.0.zip' file, which includes the 'assets' folder and the executable file, and can directly run the executable.

## Resources
The game assets are not developed by me, instead I have taken them from internet. You can find all the original files of resources from the given links:
- Characters:
  - Kiara: https://infinitestars.itch.io/infinite-stars-asset-kiaria
  - Lochem: https://infinitestars.itch.io/infinite-stars-asset-lochem
  - Mayvheen: https://infinitestars.itch.io/infinite-stars-asset-mayvheen
  - Raymond: https://infinitestars.itch.io/infinite-stars-asset-raymond
  - Veera: https://infinitestars.itch.io/infinite-stars-asset-veera-armored
 - GUI: https://craftpix.net/freebies/free-space-shooter-game-gui/
 - Font: https://www.dafont.com/origin-tech.font
