from Defs import *
from messages import *


def Action_one(character: Character) -> int:
    character.action = "action_one"

    show_message(text=f"""
    Ваше имя: {character.name}
    Ваше фамилия: {character.surname}
    Ваше отчество: {character.middle_name}
          """, spacing=True, wait_for_key=True)

    show_message(introduction, wait_for_key=True)
    show_message(beginning.format(name=character.name), wait_for_key=True)

    show_message(action_one, clear=False, tooltip=False, wait_for_key=False)

    index = choose_option("Выберите действие:", action_one_options, clear=False, is_string=False)
    choice = action_one_options[index]

    show_message(f"Вы выбрали: {choice}", clear=True, spacing=True, tooltip=False)
    return index


def Action_two(character: Character) -> int:
    character.action = "action_two"
    show_message(action_two, clear=False, tooltip=False)

    index = choose_option("Выберите действие:", action_two_options, clear=False, is_string=False)
    choice = action_two_options[index]

    show_message(f"Вы выбрали: {choice}", clear=True, spacing=True, tooltip=False, wait_for_key=False)
    return index


def Action_teaTime(character: Character) -> None:
    character.action = "action_teatime"
    show_message(name="Отец", text=action_teatime_dad_phrase, clear=False, spacing=True, tooltip=False,
                 wait_for_key=False)
    show_message(action_teatime, clear=False, tooltip=False, wait_for_key=True)
    show_message(good_ending_message, clear=True, tooltip=True, wait_for_key=True)


def Action_homicide(character: Character) -> None:
    character.action = "action_homicide"
    show_message(action_homicide, clear=False, tooltip=False, wait_for_key=True)
    show_message(bad_ending_message, clear=True, tooltip=True, wait_for_key=True)


def Action_three(character: Character) -> int:
    character.action = "action_three"

    show_message(action_three, clear=False, tooltip=False)

    index = choose_option("Выберите действие:", action_three_options, clear=False, is_string=False, )
    choice = action_three_options[index]

    show_message(f"Вы выбрали: {choice}", clear=True, spacing=True, tooltip=False, wait_for_key=False)
    return index


def Action_friend(character: Character) -> int:
    character.action = "action_friend"

    show_message(name="Колян", text=action_friend_phrase_one, clear=False, spacing=True, tooltip=False,
                 wait_for_key=False)
    show_message(name=character.name, text=action_friend_phrase_character, clear=False, spacing=True, tooltip=False,
                 wait_for_key=False)
    show_message(name="Колян", text=action_friend_phrase_two, clear=False, spacing=True, tooltip=False,
                 wait_for_key=False)

    show_message(action_five, clear=False, spacing=True, tooltip=False, wait_for_key=False)

    index = choose_option("Выберите действие:", action_five_options, clear=False, is_string=False)
    choice = action_five_options[index]

    show_message(f"Вы выбрали: {choice}", clear=True, spacing=True, tooltip=False)
    return index


def Action_six(character: Character) -> None:
    character.action = "action_six"

    add_to_inventory(character, item="Ключ")
    add_to_inventory(character, item="Записка")

    show_message(action_six, clear=False, tooltip=False, wait_for_key=True)

    show_message(good_ending_message, clear=True, tooltip=True, wait_for_key=True)


def Action_five(character: Character) -> None:
    character.action = "action_five"
    add_to_inventory(character, item="Травушка муравушка")

    show_message(action_five_alt, clear=False, tooltip=False, wait_for_key=True)
    show_message(bad_ending_message, clear=True, tooltip=True, wait_for_key=True)


def Action_three_alt(character: Character) -> None:
    character.action = "action_three_alt"
    show_message(text=action_three_alt, clear=False, spacing=True, tooltip=False, wait_for_key=True)
    show_message(bad_ending_message, clear=True, tooltip=True, wait_for_key=True)


def start_from_action_one(character: Character) -> None:
    match Action_one(character):
        case 0:
            match Action_two(character):
                case 0:
                    Action_teaTime(character)
                case 1:
                    Action_homicide(character)
        case 1:
            match Action_three(character):
                case 0:
                    match Action_friend(character):
                        case 0:
                            Action_six(character)
                        case 1:
                            Action_five(character)
                case 1:
                    Action_three_alt(character)


def start_from_action_two(character: Character) -> None:
    match Action_two(character):
        case 0:
            Action_teaTime(character)
        case 1:
            Action_homicide(character)


def start_from_action_three(character: Character) -> None:
    match Action_three(character):
        case 0:
            match Action_friend(character):
                case 0:
                    Action_six(character)
                case 1:
                    Action_five(character)
        case 1:
            Action_three_alt(character)


def start_from_action_friend(character: Character) -> None:
    match Action_friend(character):
        case 0:
            Action_six(character)
        case 1:
            Action_five(character)
