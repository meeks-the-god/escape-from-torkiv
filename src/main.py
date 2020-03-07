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
        'You ram into the window with all the force you can muster, but you '
        ' break your shoulder and sit there wimpering.\n\n'
        'GAME OVER'
    )


def go_through_door_1():
    print(
        'You go through the door and a large dog growls at you. You go '
        'down a set of stairs and find 4 more rooms.\n'
        '  1. Leap over the railing\n'
        '  2. Climb down the stairs\n'
        '  3. Enter the room with a check on it\n'
        '  4. Enter the room with an A on it\n'
    )
    choice = input()

    if choice == '1':
        leap_over_railing()
    elif choice == '2':
        climb_down_stairs()
    elif choice == '3':
        enter_checkmark_room()
    elif choice == '4':
        enter_room_a()
    else:
        go_through_door_1()


def hide_under_comforter_1():
    print(
        'You fall asleep under the comforter, and you never wake up.\n\n'
        'GAME OVER'
    )


def leap_over_railing():
    print(
        'You jump over the railing and you land on your knees. You look down '
        ' and your knee bone is sticking out.\n\n'
        'GAME OVER'
    )


def climb_down_stairs():
    print(
        'You try to climb down the stairs, but you fall through a missing'
        ' stair.\n\n'
        'GAME OVER'
    )


def enter_checkmark_room():
    print(
        'You enter a room and there are 2 different levers, all pointed up. '
        '\n'
        '1. Pull the lever with blood on it.'
        '2. Pull the lever with an ant colony on it.'
    )


def enter_room_a():
    print(
        'You go inside the room with an A on it. A mysterious voice says'
        ' "Annihilation or Apples". You yell back "Apples". That'
        ' doesn\'t seem so bad. You spend the next 30 hours picking apples,'
        ' until you die of dehydration.\n\n'
        'GAME OVER'
    )


if __name__ == "__main__":
    main()
