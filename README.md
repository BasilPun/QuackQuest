QuackQuest 🦆
🕹️ How to Play

W → Jump

Spacebar → Duck & Speed Up

Start with 3 lives

Goal: run as far as you can while avoiding obstacles

The further you run, the higher your score 🏆

🚧 To Be Added

Tutorial / Starting Instructions → Intro screen to explain controls before gameplay.

More Obstacle Types → Add variety for increased challenge.

Death Animation → On game over (all lives lost), duck explodes into particles.

Machine Learning Agent → Train an AI to play the game automatically once core gameplay is stable.

📚 What I Learned
🎮 Game Development Concepts
Terrain Generation Logic

Implemented procedural terrain with random variation (Minecraft-style).

Used a world offset system to simulate an endless runner.

Managed memory by pre-loading upcoming chunks and removing off-screen ones.

Sprites & Sprite Sheets

Extracted frames from a sprite sheet for characters and obstacles.

Used pygame.sprite.Sprite groups for easier management and collision detection.

Built smooth animations by cycling between frames.

Animation Techniques

Timed frame updates to control walking and jumping.

Synced sprite changes with in-game actions for responsive visuals.

Game Physics

Implemented gravity to simulate falling.

Designed jump mechanics with controlled height and responsiveness.

Added knockback/bounce effects on collisions.

Collision Detection

Used bounding boxes (rect) for efficient collision handling.

Fixed obstacle collision logic so the duck properly loses lives when hit.

Fixed obstacle alignment, ensuring obstacles spawn correctly on terrain instead of floating.

Game Loop & State Management

Built a main loop to update and render the game each frame.

Implemented states: menu, running, and game over.

Added UI for restarting and an interactive duck on the main menu.

🐍 Python Programming Skills
Core Python Syntax

Used loops, conditionals, and functions throughout gameplay logic.

Organized code into reusable utility functions.

Object-Oriented Programming (OOP)

Designed classes like Duck, TerrainBlock, and Obstacle.

Encapsulated behavior in clean, maintainable objects.

Code Organization

Structured the project into multiple files (game.py, terrain.py, obstacles.py, etc.).

Learned how to build and maintain a medium-sized Python project.

🌐 Development Tools
Git & GitHub

Set up version control for the project.

Created a .gitignore to hide unnecessary files (e.g., __pycache__).

Committed and pushed updates through GitHub.

🕸️ Pygbag (Web Export)

Learned how to export the game using Pygbag.

Successfully ran the game in a browser through WebAssembly.

Understood packaging and deployment steps for web builds.