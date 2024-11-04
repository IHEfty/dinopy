# Dinopy

A simple clone of the classic Dino game built using Python and Pygame. This game features a light and dark mode, customizable through a configuration file. The player controls a dinosaur that jumps over obstacles, and the game speed increases as the score goes up.

## Features

- **Light and Dark Themes**: Choose your theme by setting it in the configuration file (`settings.ini`).
- **Dynamic Difficulty**: The game speed gradually increases as your score goes up.
- **Score Display**: Real-time score display to track progress.

## Requirements

- **Python 3.6+**
- **Pygame**: Install it via pip if you haven't already.
  ```bash
  pip install pygame
  ```

## Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/IHEfty/dinopy.git
   cd dinopy
   ```

2. **Add the Settings File**

   Create a file named `settings.ini` in the project directory with the following content:

   ```ini
   [Settings]
   theme = light
   ```

   Change `theme` to `dark` if you prefer a dark background.

3. **Add Images**

   Place the following images in the same directory as your script:
   - `dino.png`: Dinosaur image for the light theme.
   - `cactus.png`: Cactus image for the light theme.
   - `dino1.png`: Dinosaur image for the dark theme.
   - `cactus1.png`: Cactus image for the dark theme.

## Running the Game

To start the game, run:

```bash
python dino.py
```

Press the `Space` key to make the dinosaur jump and avoid obstacles.

## Gameplay Instructions

- **Objective**: Jump over the cactuses to avoid collisions and keep the game running as long as possible.
- **Controls**: Press `Space` to jump. The dinosaur cannot jump again until it has landed back on the ground.

## Code Highlights

- **Dynamic Obstacles**: The game randomly generates obstacles at varying distances to keep gameplay interesting.
- **Speed Scaling**: As the player’s score increases, the obstacles move faster, adding a level of challenge.

## License

This project is for educational and personal use. Feel free to modify it for your own projects.

