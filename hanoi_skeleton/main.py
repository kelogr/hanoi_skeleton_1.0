from hanoi.hanoi import HanoiGame
from hanoi.hanoi_exception import HanoiException


def get_int_value(message, range_start, range_end):
    """
    Sends the user the input message and checks that the input data is an integer between range_start and range_end.
    Returns the value if is correct, None otherwise.

    :param message: Message for the user asking for some integer input
    :param range_start: First value into the valid range.
    :param range_end: First value out of the valid range
    :return:
    """

    value = None
    while value is None:
        value = input(message)
        try:
            value = int(value)
            if value < range_start or value > range_end:
                print("The value should be between %d and %d! Try again." % (range_start, range_end))
                value = None
        except ValueError:
            print("This is not a valid input value! Try again.")
            value = None

    return value


def do_move(hanoi_game):
    """
    Asks the user for a move and returns True if the move lead to a finishing state.

    :param hanoi_game: The game instance the program is using.
    :return: True if the move reached a finishing state, False otherwise.
    """

    done = False
    while not done:

        try:
            source_tower = get_int_value("Move from? (tower 1, 2 or 3, 0 to cancel)\n", 0, 3)
            if source_tower:
                target_tower = get_int_value("Move to? (tower 1, 2 or 3, 0 to cancel)\n", 0, 3)

                if target_tower:
                    #hanoi_game.move(hanoi_game.towers[source_tower-1], hanoi_game.towers[target_tower-1])
                    hanoi_game.move(source_tower-1, target_tower-1)
                else:
                    print("Move canceled!")
            else:
                print("Move canceled!")
            done = True

        except HanoiException as exc:
            print(exc)
            print()

    return hanoi_game.is_finished()


game_options = """
What do you want to do?
    1.- Do a move
    2.- Show current state
    3.- Show optimal solution
    0.- Quit"""


def play_game():
    """
    Main loop for interactive play.
    """

    n_discs = get_int_value("How many discs do you want?\n", 1, 10)
    hanoi_game = HanoiGame(n_discs)

    #print(hanoi_game.states)

    quit_game = False

    while quit_game is False:
        print(game_options)

        selected_option = input()
        if selected_option == "0":
            quit_game = True

        elif selected_option == "1":
            do_move(hanoi_game)
            print("\nCurrent state:")
            try:
                print(hanoi_game)
            except HanoiException as msg:
                print(msg)
            quit_game = hanoi_game.is_finished()

        elif selected_option == "2":
            print("\nCurrent state:")
            try:
                print(hanoi_game)
            except HanoiException as msg:
                print(msg)
        elif selected_option == "3":
            hanoi_game.print_optimal_solution()

        else:
            print("This is not a valid option! Let's try again...")

    if hanoi_game.is_finished():
        print("CONGRATS")


header = """
    ################################
    ####### TOWERS OF HANOI ########
    ################################"""

main_options = """
What do you want to do?
    1.- Play hanoi towers!
    2.- Show help
    0.- Exit"""

main_help = """
HOW TO PLAY:

The objective of the game is to move the entire stack of discs from Tower 1 to Tower 3!
But there are two restrictions:
    1) You can move only one disk at a time.
    2) No disk can be placed on top of a smaller disc."""


def show_menu():
    """
    Main loop for the main menu
    """

    print(header)

    exit_game = False
    while not exit_game:
        print(main_options)

        selected_option = input()
        if selected_option == "0":
            exit_game = True

        elif selected_option == "1":
            play_game()

        elif selected_option == "2":
            print(main_help)

        else:
            print("This is not a valid option! Let's try again...")


if __name__ == '__main__':
    show_menu()

#       TEST NUMBER 6
#Initial state plus 2^n - 1 states with moves
hanoi_game = HanoiGame(10)
assert(hanoi_game.get_n_states() == 1024)

#       TEST NUMBER 7
#You need to be able to retrieve the state of a tower in a state, to see the number of elements that are there
hanoi_game = HanoiGame(3)
state = hanoi_game.get_state(5)

assert(sum(1 for element in state.get_tower(0) if element != 0) == 1)
assert(sum(1 for element in state.get_tower(1) if element != 0) == 1)
assert(sum(1 for element in state.get_tower(2) if element != 0) == 1)

#       TEST NUMBER 10

#Note that we are accessing the first state. No moves have been done yet, So no header or last move line needs to be present
expected = """
....#|#.... .....|..... .....|..... 
...##|##... .....|..... .....|..... 
..###|###.. .....|..... .....|..... 
.####|####. .....|..... .....|..... 
#####|##### .....|..... .....|..... 
  Tower 1     Tower 2     Tower 3   
"""

hanoi_game = HanoiGame(5)
state = hanoi_game.get_state(0)
print(state)
assert(expected == str(state))

#       TEST NUMBER 12

#Show the current state, when playing manually
hanoi_game = HanoiGame(3)
hanoi_game.move(0, 2)
hanoi_game.move(0, 1)

state = hanoi_game.get_current_state()

expected = """
...|... ...|... ...|... 
...|... ...|... ...|... 
###|### .##|##. ..#|#.. 
Tower 1 Tower 2 Tower 3 
"""
print(state + " " + expected)
assert(expected == str(state))
