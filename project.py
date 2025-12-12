# the main file to run the game
# here are written the game parts: start menu, main game loop, over menu
# and their event handlers
import pygame
import sys
from interface import Button, get_nice_gradient
from mechanics import Game

def start_menu(screen, clock, screen_width, screen_height, size, screen_color=(248, 239, 206)):
    """
    start menu before the game starts
    args:
        screen - pygame display surface
        clock - pygame time clock
        screen_width - width of the screen
        screen_height - height of the screen
        size - initial size of the game field
    returns:
        size - size of the game field chosen by the user
    """

    PINK = (228, 166, 157)

    # start menu loop
    menu = True
    pygame.display.set_caption("2048 menu")
    menu_button = Button((screen_width//2, screen_width//8), (screen_width//4, screen_height//4), PINK, f'START ({size}x{size})')

    # text input button
    message = 'Choose field size (e.g. 3): '
    text_button = Button((screen_width//2, screen_width//8), (screen_width//4, screen_height//2), PINK, message)
    text = ''
    input_active = False

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # if press on a menu button, the game starts
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if menu_button.x <= x <= menu_button.x + menu_button.w and menu_button.y <= y <= menu_button.y + menu_button.h:
                    menu = False
                # if press on the text button, activate text input
                elif text_button.x <= x <= text_button.x + text_button.w and text_button.y <= y <= text_button.y + text_button.h:
                    input_active = True

            # keyboard event handler for text input
            if event.type == pygame.KEYDOWN and input_active:

                # if backspace is pressed, remove last character
                if event.key == pygame.K_BACKSPACE:
                    text =  text[:-1]

                # if enter is pressed, try to start the game with the given size
                elif event.key == pygame.K_RETURN:
                    if text:
                        try:
                            Game(int(text))
                        except ValueError:
                            # invalid size, change the message
                            message = 'Invalid board size. Try again: '
                        else:
                            # valid size, exit the menu
                            size = int(text)
                            menu = False
                else:
                    text += event.unicode
        # Get the current time in milliseconds
        current_time_ms = pygame.time.get_ticks()

        # Determine if the current second is even or odd
        even_second = (current_time_ms // 1000) % 2

        # Update the text button to show a blinking cursor
        text_button.text = message + text + '|'*input_active if even_second else message + text + ' '*input_active

        # Fill the screen with the color (cream colour is the default color)
        screen.fill(screen_color)

        menu_button.draw(screen)
        text_button.draw(screen)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate at 60 frames per second
        clock.tick(60)
    return size



def play(screen, clock, size, screen_width, screen_height, screen_color=(248, 239, 206)):
    """
    main game loop
    args:
        screen - pygame display surface
        clock - pygame time clock
        size - size of the game field
        screen_width - width of the screen
        screen_height - height of the screen
    returns:
        score - final score of the game
    """

    # Change the caption of the window
    pygame.display.set_caption("2048 game")

    # list for 0, 2, 4, 8 and so on
    # that is then used to create a dictionary for colors
    numbers = [2**x for x in range(0, 3*size + 1)]
    numbers[0] = 0
    colors = dict(zip(numbers, get_nice_gradient(3*size+1)))
    WHITE = (255, 255, 255)

    # h - height
    # 1.5 coefficient is needed for space between buttons
    # 4 is margins
    button_h = screen_height // (size * 1.5 + 4)
    # w - width
    button_w = button_h
    # s - starting coordinates for buttons
    s_x, s_y = (screen_width-1.5*size*button_w)//2,  2 * button_h

    # initialize a game session
    game = Game(size)

    # create number buttons for the game
    score_button = Button((3*button_w, button_h), (button_w, 0.5 * button_h), screen_color, f'Score : {game.score}')
    board_buttons = [
        [
            Button((button_w, button_h),
                (s_x + 1.5 * button_w * i, s_y + 1.5 * button_h * j),
                colors[game.board[j][i]],
                str(game.board[j][i]) if game.board[j][i] != 0 else '')
            for j in range(size)
        ]
        for i in range(size)
    ]

    while not game.over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # keyboard event handler for swipes
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_RIGHT:
                        game.right()
                        game.add_number()
                    case pygame.K_LEFT:
                        game.left()
                        game.add_number()
                    case pygame.K_UP:
                        game.up()
                        game.add_number()
                    case pygame.K_DOWN:
                        game.down()
                        game.add_number()
                    case pygame.K_ESCAPE:
                        game.over = True
                score_button.text = f'Score : {game.score}'
                for i in range(size):
                    for j in range(size):
                        board_buttons[i][j].color = colors[game.board[j][i]]
                        board_buttons[i][j].text = str(game.board[j][i]) if game.board[j][i] != 0 else ''

        # Fill the screen with the color (cream colour is the default color)
        screen.fill(screen_color)

        # Draw the score and the game board
        score_button.draw(screen)
        for row in board_buttons:
            for button in row:
                button.draw(screen, WHITE)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate at 60 frames per second
        clock.tick(60)

    return game.score


def over_menu(screen, clock, score, screen_width, screen_height, screen_color=(248, 239, 206)):
    """
    final menu with the score
    args:
        screen - pygame display surface
        clock - pygame time clock
        score - final score of the game
        screen_width - width of the screen
        screen_height - height of the screen
    no return
    """
    AQUA = (148, 196, 193)

    # button showing the score
    over_menu_button = Button((screen_width//2, screen_width//8), (screen_width//4, screen_height//3), AQUA, f'Your score is {score}')
    over_menu = True

    # over menu loop
    while over_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                over_menu = False


        # Fill the screen with the color (cream colour is the default color)
        screen.fill(screen_color)

        over_menu_button.draw(screen)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate at 60 frames per second
        clock.tick(60)



def main():
    # Initialize PyGame
    pygame.init()

    # Set up the game window
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Set the frame rate
    clock = pygame.time.Clock()

    # Set the game field size
    size = 5

    pygame.display.set_caption("2048 menu")
    size = start_menu(screen, clock, screen_width, screen_height, size)

    pygame.display.set_caption("2048 game")
    score = play(screen, clock, size, screen_width, screen_height)

    pygame.display.set_caption("Press any key to exit...")
    over_menu(screen, clock, score, screen_width, screen_height)

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
