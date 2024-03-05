from dataclasses import dataclass
from msvcrt import kbhit, getch
from os import system as command
from time import sleep


@dataclass(slots=True, frozen=False)
class Character:
    name: str
    surname: str
    middle_name: str
    inventory: list[str]
    username: str
    action: str


def add_to_inventory(character: Character, item: str) -> None:
    character.inventory.append(item)

    show_message(f"Добавлен предмет \"{item}\" в Ваш инвентарь.", clear=False, spacing=True, tooltip=False,
                 wait_for_key=False)


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
                print(f"Неправильный выбор. Выберите пожалуйста между 1 и {len(options)}\n")
        except ValueError:
            print("Неправильный ввод. Введите пожалуйста число.")


def type(text: str, name: str = None) -> None:
    for letter in text:
        if kbhit():
            key = getch()

            if key == b'\r':
                command("cls")

                if name:
                    show_name(name)

                print(text)
            if key == b'\x1b':
                command("cls")
                print("Вы вышли из игры, сохранение было сделано автоматически")
                quit(0)

            break

        print(letter, end="", flush=True)
        sleep(0.025)


def show_name(name: str) -> None:
    print(f"[{name}]: ", end="")


def show_tooltip() -> None:
    print("Для того чтобы пропустить анимацию нажмите ENTER")
    print("Для того чтобы выйти из игры нажмите ESCAPE")
    print()


def wait_for_any_key() -> None:
    print()
    print()
    print('Нажмите любую клавишу, чтобы продолжить', end='', flush=True)
    getch()


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