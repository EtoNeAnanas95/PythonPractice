from dataclasses import dataclass
from time import sleep
from os import system as command

from messages import *

from msvcrt import kbhit, getch

def wait_for_any_key() -> None:
    print()
    print()
    print('Нажмите любую клавишу, чтобы продолжить', end='', flush=True)
    getch()

def show_tooltip() -> None:
    print("Для того чтобы пропустить анимацию нажмите ENTER")
    print()

def show_name(name: str) -> None:
    print(f"[{name}]: ", end="")

def type(text: str, name: str = None) -> None:
    for letter in text:
        if kbhit():
            key = getch()
            
            if key == b'\r':
                command("cls")

                if name:
                    show_name(name)

                print(text)
            
            break

        print(letter, end="", flush=True)
        sleep(0.025) 
      
def show_message(
    text: str,
    name: str = None,
    clear: bool = True,
    spacing: bool = False,
    tooltip: bool = True,
    wait_for_key: bool = False 
) -> None:
    if clear is True:
        command("cls")

    if name:
        show_name(name)

    if tooltip is True:
        show_tooltip()

    type(text)

    if wait_for_key is True:
        wait_for_any_key()

    if spacing is True:
        print()
    
    if clear is True:
        sleep(0.3)
        command("cls")

def choose_option(
    label: str,
    options: list,
    clear: bool = True,
    is_string: bool = True
) -> int:
    if clear is True:
        command("cls")

    print()
    print()
    print(label)
    
    for index, option in enumerate(options):
        print(f"{index + 1}. {option}")

    while True:
        try:
            print()
            choice = int(input(f"Выберите от 1 - {len(options)}: ")) 
            if 1 <= choice <= len(options):
                if is_string is True:
                    return options[choice - 1] 
                else: 
                    return choice - 1
            else:
                print(f"Неправильный выбор. Выберите пожалуйста между 1 и {len(options)}")
        except ValueError:
            print("Неправильный ввод. Введите пожалуйста число.")

def add_to_inventory(inventory: set, item: str) -> None:
    inventory.update(item)

    show_message(f"Добавлен предмет \"{item}\" в Ваш инвентарь.", clear=False, spacing=True, tooltip=False, wait_for_key=False)

@dataclass(slots=True, frozen=True)
class Character:
    name: str
    surname: str
    middle_name: str

character = Character(
    name=choose_option("Выберите имя:", names),
    surname=choose_option("Выберите фамилию:", surnames),
    middle_name=choose_option("Выберите отчество:", middle_names)
)
inventory = set()

show_message(text = f"""
Ваше имя: {character.name}
Ваше фамилия: {character.surname}
Ваше отчество: {character.middle_name}
      """, spacing=True, wait_for_key=True)

show_message(introduction, wait_for_key=True)
show_message(beginning.format(name=character.name), wait_for_key=True)

show_message(action_one, clear=False, tooltip=False, wait_for_key=False)

index = choose_option("Выберите действие:", action_one_options, clear=False, is_string=False)
choice = action_one_options[index]

show_message(f"Вы выбрали: {choice}", clear = True, spacing=True, tooltip=False)

match index:
    case 0:
        show_message(action_two, clear=False, tooltip=False)

        index = choose_option("Выберите действие:", action_two_options, clear=False, is_string=False)
        choice = action_two_options[index]

        show_message(f"Вы выбрали: {choice}", clear = True, spacing=True, tooltip=False, wait_for_key=False)

        match index:
            case 0:
                show_message(name="Отец", text=action_teatime_dad_phrase, clear=False, spacing=True, tooltip=False, wait_for_key=False)
                show_message(action_teatime, clear=False, tooltip = False, wait_for_key=True)
                show_message(good_ending_message, clear=True, tooltip = True, wait_for_key=True)
            case 1:
                show_message(action_homicide, clear=False, tooltip = False, wait_for_key=True)
                show_message(bad_ending_message, clear=True, tooltip = True, wait_for_key=True)

    case 1:
        show_message(action_three, clear=False, tooltip=False)

        index = choose_option("Выберите действие:", action_three_options, clear=False, is_string=False,)
        choice = action_three_options[index]

        show_message(f"Вы выбрали: {choice}", clear = True, spacing=True, tooltip=False, wait_for_key=False)

        match index:
            case 0:
                show_message(name="Колян", text=action_friend_phrase_one, clear=False, spacing=True, tooltip=False, wait_for_key= False)
                show_message(name=character.name, text=action_friend_phrase_character, clear=False, spacing=True, tooltip=False, wait_for_key= False)
                show_message(name="Колян", text=action_friend_phrase_two, clear=False, spacing=True, tooltip=False, wait_for_key= False)

                show_message(action_five, clear=False, spacing=True, tooltip = False, wait_for_key=False)

                index = choose_option("Выберите действие:", action_five_options, clear=False, is_string=False)
                choice = action_five_options[index]

                show_message(f"Вы выбрали: {choice}", clear = True, spacing=True, tooltip=False)

                match index:
                    case 0:
                        add_to_inventory(inventory, item = "Ключ")
                        add_to_inventory(inventory, item = "Записка")

                        show_message(action_six, clear=False, tooltip = False, wait_for_key=True) 

                        show_message(good_ending_message, clear=True, tooltip = True, wait_for_key=True)
                    case 1:
                        add_to_inventory(inventory, item = "Травушка муравушка")

                        show_message(action_five_alt, clear=False, tooltip = False, wait_for_key=True) 
                        show_message(bad_ending_message, clear=True, tooltip = True, wait_for_key=True)


            case 1:
                show_message(text=action_three_alt, clear=False, spacing=True, tooltip=False, wait_for_key = True)
                show_message(bad_ending_message, clear=True, tooltip = True, wait_for_key=True)