import os

from actions import *
from saves import choose_save, save_inventory, save_character, Save, load_inventory, delete_save


def new_character() -> Character:
    command("cls")

    character = Character(
        name=choose_option("Выберите имя:", names),
        surname=choose_option("Выберите фамилию:", surnames),
        middle_name=choose_option("Выберите отчество:", middle_names),
        username=input("Введите имя своего пользователя: ").strip(),
        inventory=[],
        action="introduction"
    )

    return character

def new_game(character: Character) -> None:
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


def game_from_save(save: Save, character: Character) -> None:
    command("cls")
    action = save.action

    actions = {
        "introduction": start_from_action_one,
        "beginning": start_from_action_one,
        "action_one": start_from_action_one,
        "action_two": start_from_action_two,
        "action_three": start_from_action_three,
        "action_teatime": Action_teaTime,
        "action_homicide": Action_homicide,
        "action_six": Action_six,
        "action_five": Action_five,
        "action_three_alt": Action_three_alt,
        "action_friend": start_from_action_friend,
    }

    actions[action](character)


def game():
    try:
        character = None

        while True:
            chosen = choose_option("Выберите действие: ", ["Новая игра", "Сохранения", "Удалить сохранение"], clear=True,
                                   is_string=False)

            match chosen:
                case 0:
                    character = new_character()

                    new_game(character)

                    break

                case 1:
                    if os.path.exists("saves.csv"):
                        user, save = choose_save()

                        if user == None:
                            continue

                        if save == None:
                            continue

                        inventory = load_inventory(user.username, [save.surname, save.name, save.middle_name])

                        character = Character(
                            name=save.name,
                            surname=save.surname,
                            middle_name=save.middle_name,
                            inventory=inventory,
                            username=user.username,
                            action=save.action
                        )

                        game_from_save(save, character)

                    else:
                        character = new_character()

                        new_game(character)
                    break
                case 2:
                    if os.path.exists("saves.csv"):
                        delete_save()
                    else:
                        print("Нет доступных сохранений для удаления.")
    except:
        pass
    finally:
        if character != None:
            save_character(character)
            save_inventory(character)
