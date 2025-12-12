    # 2048
    #### Video Demo:  <URL HERE>
    #### Description:

    WHAT DOES THE GAME DO?

    This is a Python implementation of the popular 2048 puzzle game with a graphical user interface built using pygame. The game features customizable board sizes, a dynamic color gradient system.
    2048 is a sliding block puzzle game where the objective is to combine tiles with the same numbers to create larger numbers. The game starts with a few "2" tiles on the board. When you swipe tiles in any direction (up, down, left, right), all tiles slide as far as possible in that direction. If two tiles with the same number collide, they merge into one tile with double the value, and half this value is added to your score. After each move, new "2" tiles appear randomly on empty spaces. The game continues until the board is full and no more moves are possible.

    Features

        Customizable board size: Choose from 3x3 to 19x19 grid sizes
        Dynamic color gradient: Colors automatically adjust based on board size
        Score tracking: Real-time score display
        Smooth animations: Built with pygame for responsive gameplay

    Project Structure
        project_2048_graphic/
        ├── project.py              # Main entry point, game state management (menus, gameplay)
        ├── mechanics.py            # Game logic and board mechanics
        ├── interface.py            # UI components (buttons, colors)
        ├── test_mechanics.py       # Tests for game mechanics
        ├── test_interface.py      # Tests for interface (colors)
        ├── requirements.txt        # Project dependencies
        └── README.md              # This file

    How to Play

    Starting the Game

    ->python project.py

    Game Controls

    Arrow Keys: Move tiles (↑ ↓ ← →)
    ESC: Exit the current game
    Mouse Click: Interact with menu buttons

    Menu Navigation

    Start Menu:

    Click "START" to begin with default 5x5 board
    Click "Choose field size" to enter custom board dimensions
    Type a number (3-19) and press Enter to start with custom size

    Game Over Menu:

    Displays your final score
    Press any key to exit

    HOW IS THE GAME BUILT?

    the game has mechanics.py file where all the actions with the board and all game logic are written.
    also there are described possible exceptions such as trying to create a board of not int size or too big size.
    in order to effectively swipe the board meaning sort the board array i learned how to sort an array with 2 pointers
    so that the zeros go to beginning of an array and the relative order of other elements is conserved
    unless there are two duplicates that need to be summed up. in case of duplicates the value of one duplicate is added to the score.

    so that i don't need to write 4 almost identical functions i decided to have arg 'transpose'
    that transposes board array and calls "transposes" function.
    for example, to swipe an array down the array is transposed and then game.right(transpose=True) is called.
    the score adds after each move.

    mechanics.py file is tested with test_mechanics.py that tests swiping functions, creating the game function
    and function that adds extra "2"'s after each swipe on the board.
    the separate file for game mechanics is needed not only due to OOP, code clarity, but also for my hopefully
    next project idea. i'd like to try RL method on this 2048 game and for that i want to be able to create a game session
    without graphic interface, just arrays and numbers that will be passed on to to RL network.
    but I understand that there's not enough complexity without proper graphic interface.
    for that reason, the game has graphic interface using pygame library (library version is in requirements.txt).
    I chose pygame because it's an easy to learn library + it's an active library and it has a lot of materials and tutorials on the internet.
    using pygame means that I'll have to rewrite my event handler (used to use the curses library) which is fine.
    it also means that I'll have to write and test code on my own computer, not cs50.dev.

    the next part of the project is interface.py. this file has buttons class, during init method button object gets location, size, color parameters as well as text of the button and pygame rectangle. the button object can be drawn if provided with screen argument and moved if provided with a coordinate shift.
    another part of interface.py is function for creating needed number of colors according to defined gradient. it uses matplotlib library (needed version of library is in requirements.txt).
    this function also uses normalize and denormalize function that does the transition (r, g, b) 0-255 <-> (r, g, b) 0-1.
    gradient function and its helping functions are tested in test_interface.py.
    unfortunately, to test class Button I need to create mock pygame inits in pytest that I'd like to know how to do in the future but for now I've decided that the project can be complex enough without it.

    an important part of the game is event handler that is written in project.py file.
    it has 3 parts - the player is greeted with starting menu. here he can start game of 5x5 size or press with mouse on button "Choose field size:".
    When he presses on it, blinking cursor appears, it's possible to print need size (int number between 3 and 19). You may also print backspace to erase last symbol.
    Then you need to press Enter. if size is correct, the game session will start. if not, you'll see message "Invalid board size. Try again: ". You'll need to input size again.
    Depending on the size of the board, the player will see a little bit different colors because the size parameter is passed on to gradient function that creates list of 3*size+1 colors.
    The game starts, you control it with arrow keys. if an arrow is pressed the corresponding swiping function is called.
    if an 'Escape' key is pressed then the game is over and you see a menu with final scores.
    also the game will be over if you don't have any spare room on the board and swiping is impossible.
    you press any key and the game is closed.
    unfortunately, project.py was tested only manually without unit tests for the reason mentioned earlier.
