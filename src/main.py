"""Entry file to the program escape from torkiv. See readme for details!"""


def main():
    print(
        'You wake up in an unknown house. You appear to be in a '
        'bedroom. '
        'The air is frigid; there is an icy window that you might '
        'be able to break through and a door to the bedroom.\n'
        '  1. Try to break through the window\n'
        '  2. Go through the door\n'
        '  3. Hide under the comforter\n'
    )
    choice = input()

    if choice == '1':
        break_through_window_1()
    elif choice == '2':
        go_through_door_1()
    elif choice == '3':
        hide_under_comforter_1()
    else:
        main()


def break_through_window_1():
    print(
        'Some death text here.\n\n'
        'GAME OVER'
    )


def go_through_door_1():
    print('TODO')


def hide_under_comforter_1():
    print('TODO')


if __name__ == "__main__":
    main()
