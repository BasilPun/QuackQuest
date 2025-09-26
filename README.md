# QuackQuest 🦆

## 🕹️ How to Play

- **W** → Jump
- **Spacebar** → Duck & Speed Up
- Start with **3 lives**
- Goal: **run as far as you can** while avoiding obstacles
- The further you run, the higher your score 🏆

---

## 🚧 To Be Added

- **Obstacle Interactions** → Collisions should correctly remove a life.
- **Tutorial / Starting Instructions** → Intro screen to explain controls before gameplay.
- **Obstacle Sprite Fix** → Sometimes sprites tend to spawn on air due to spawning and the edge of blocks.
- **More Obstacle Types** → Add variety for increased challenge.
- **Death Animation** → On game over (all lives lost), duck explodes into particles.
- **Machine Learning Agent** → Train an AI to play the game automatically once core gameplay is stable.

---

## 📚 What I Learned

### 🎮 Game Development Concepts

- **Terrain Generation Logic**

  - Implemented procedural terrain with random variation (Minecraft-style).
  - Used a world offset system to simulate an endless runner.
  - Managed memory by pre-loading upcoming chunks and deleting off-screen ones.

- **Sprites & Sprite Sheets**

  - Extracted frames from a sprite sheet for characters and obstacles.
  - Used `pygame.sprite.Sprite` groups for easier management and collision detection.
  - Built smooth animations by cycling frames in code.

- **Animation Techniques**

  - Timed frame updates to control walking and jumping.
  - Synced sprite changes with in-game actions for responsive visuals.

- **Game Physics**

  - Implemented **gravity** to simulate falling.
  - Designed **jump mechanics** with controlled height and responsiveness.
  - Added **knockback/bounce back** effects when hitting obstacles.

- **Collision Detection**

  - Used bounding boxes (`rect`) for efficient collision handling.
  - Responded to collisions by stopping, sliding, or bouncing.

- **Game Loop & State Management**
  - Built a main loop to update and render the game each frame.
  - Managed states: _menu_, _running_, and _game over_.
  - Added UI for restart prompts and an interactive duck on the main menu.

---

### 🐍 Python Programming Skills

- **Core Python Syntax**

  - Practiced loops, conditionals, and functions in a real project.
  - Organized code into reusable modules.

- **Object-Oriented Programming (OOP)**

  - Designed classes for entities like `Duck`, `TerrainBlock`, and `Obstacle`.
  - Encapsulated logic inside objects for cleaner, maintainable code.

- **Code Organization**
  - Split the project into multiple files (`game.py`, `terrain.py`, `obstacles.py`, etc.).
  - Learned how to structure a medium-sized Python project.

---

### 🌐 Development Tools

- **Git & GitHub**
  - Set up version control with Git.
  - Created a `.gitignore` to keep unnecessary files (like `__pycache__`) out of the repo.
  - Learned to commit, push, and manage code changes on GitHub.
