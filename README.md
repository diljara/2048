# 2048
#### Video Demo:  <URL HERE>
#### Description:

# WHAT DOES THE GAME DO?

This is a Python implementation of the popular 2048 puzzle game with a graphical user interface built using pygame. The game features customizable board sizes, a dynamic color gradient system.
2048 is a sliding block puzzle game where the objective is to combine tiles with the same numbers to create larger numbers. The game starts with a few "2" tiles on the board. When you swipe tiles in any direction (up, down, left, right), all tiles slide as far as possible in that direction. If two tiles with the same number collide, they merge into one tile with double the value, and half this value is added to your score. After each move, new "2" tiles appear randomly on empty spaces. The game continues until the board is full and no more moves are possible.

# Features

* Customizable board size: Choose from 3x3 to 19x19 grid sizes  
* Dynamic color gradient: Colors automatically adjust based on board size  
* Score tracking: Real-time score display  
* Smooth animations: Built with pygame for responsive gameplay  

# Project Structure  

    2048/  
    ├── project.py              # Main entry point and game loop  
    ├── mechanics.py            # Game logic and board mechanics  
    ├── interface.py            # UI components (buttons, colors)  
    ├── game_epochs.py          # Game state management (menus, gameplay)  
    ├── test_mechanics.py       # Tests for game mechanics  
    ├── test_interface.py       # Tests for color functions  
    ├── requirements.txt        # Project dependencies  
    └── README.md               # This file  

# How to Play

## Starting the Game

`python project.py`  

## Game Controls

* Arrow Keys: Move tiles (↑ ↓ ← →)  
* ESC: Exit the current game  
* Mouse Click: Interact with menu buttons  

## Menu Navigation

1. **Start Menu**:

* Click "START" to begin with default 5x5 board  
* Click "Choose field size" to enter custom board dimensions  
* Type a number (3-19) and press Enter to start with custom size  

2. **Game Over Menu**:

* Displays your final score  
* Press any key to exit  

# HOW IS THE GAME BUILT?

## **mechanics.py**  

Contains the core game logic:  
* **Game class**: Manages board state, scoring, and game-over conditions  
* **Swipe methods**: Implements left, right, up, and down movements using a two-pointer algorithm to efficiently merge tiles  
* **Board management**: Handles tile generation and placement  
* **Input validation**: Ensures board size is valid (integer between 3 and 19)  

The swipe algorithm uses two pointers to:  

* Move all non-zero elements to one end  
* Preserve relative order of elements  
* Merge adjacent duplicates  
* Update score accordingly  

I decided to implement only the `left()` and `right()` functions and then use matrix transposition to handle `up()` and `down()` movements. This eliminates code duplication and makes the codebase more maintainable.  

The game logic is completely decoupled from the interface for several reasons:

* Testability: Can test game logic without pygame  
* Reusability: The same mechanics can be used for different interfaces  
* Possible future ML integration: hoping to implement reinforcement learning agent that will learn to play the game  
* Code clarity: Separation of concerns makes the codebase easier to maintain

## **interface.py**
Handles all UI components:

* **Button class**: Creates interactive buttons with position, size, color, and text

   `draw()`: Renders button on screen  
   `move()`: Adjusts button position by delta coordinates  


* **Color gradient system**: Uses matplotlib to generate smooth color gradients

   `get_nice_gradient(N)`: Creates N colors interpolated across a predefined color palette  
   `normalize()/denormalize()`: Converts between 0-255 and 0-1 color (r, g, b) ranges    
   The gradient adjusts to board size (3×size+1 colors) ensuring visual consistency  

## **project.py**

Manages game states and event handling:

* `start_menu()`: Initial screen with board size selection  
* `play()`: Main game loop with keyboard input handling  
* `over_menu()`: End screen displaying final score  

Each function uses pygame's event system to handle user input and updates the display at 60 FPS.  
Event handling is done using pygame library.  
Why pygame?  

* Easy to learn: Simple with excellent documentation  
* Active community: A lot of tutorials and examples  
* Cross-platform: Works on Windows, macOS, and Linux  
* Lightweight: Minimal dependencies compared to alternatives  

# Testing
The project includes comprehensive test coverage using pytest framework.
## Test Coverage

**mechanics.py**: Fully tested  

* Board initialization and validation  
* All swipe directions (left, right, up, down)  
* Tile merging logic  (sometimes double merging bug occurs, it makes game easier)
* Score calculation  
* Random tile generation  
* Game-over detection  

**interface.py**: Partially tested  

* Color normalization and denormalization  
* Gradient generation with various sizes  
* Color value validation and edge cases  
Note: Button class and pygame-dependent features are tested manually  

**project.py**: Tested manually

* Menu navigation and user interactions tested through gameplay
* Event handling verified during development

The core game logic in `mechanics.py` is thoroughly tested with unit tests to ensure correctness of the game rules and board operations. The `interface.py` module's non-pygame components (color functions) are also unit tested. Components requiring pygame initialization (Button class, menu systems, event handlers) are verified through manual testing to ensure they work correctly in the actual game environment.

# Future Enhancements

* Reinforcement Learning: Train AI agent to play the game optimally
* High score persistence: Save best scores to disk
* Full testing: Test with mock pygame inits
* Fix bugs: double merging in certain situations
