# Asteroids Game (Python)

A fully functional Asteroids game written in Python, featuring ship movement, asteroid collisions, torpedo firing, and score tracking. The game follows the classic arcade mechanics, using object-oriented programming principles to manage entities like ships, asteroids, and torpedoes.

## Features

- Classic Asteroids gameplay where the player navigates a spaceship, shoots asteroids, and survives as long as possible.
- Ship controls that allow the player to rotate, accelerate, and fire torpedoes to destroy asteroids.
- Asteroids split into smaller ones upon impact.
- A scoring system where points are awarded based on asteroid size.
- A dynamic game loop using a custom `Screen` class for rendering and event handling.
- A life system where the player loses a life upon collision, and the game ends when all lives are lost.
- Game over and victory messages are displayed based on the player's performance.

## Code Structure

- Object-oriented design with separate classes for `Ship`, `Asteroid`, `Torpedo`, and `GameRunner`.
- Custom `Screen` class that manages rendering, user input, and updates.
- Event handling for user inputs, including arrow keys for movement and the spacebar for shooting.
- Screen wrapping that allows objects to move beyond one edge and reappear on the opposite side.
- Collision detection for interactions between the ship, asteroids, and torpedoes.
- Randomized asteroid generation to ensure a different game experience each time.

## Controls

| Key | Action |
|-----|--------|
| Left Arrow | Rotate ship left |
| Right Arrow | Rotate ship right |
| Up Arrow | Accelerate forward |
| Space | Fire torpedo |

## How to Run

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd Asteroids-Python
