from data_manager import *
#import keyboard
from typing import Any


def type_data(texts) -> None:
    i = 0
    for item in texts:
        i += 1
        print(f"{i}. {item}")


def chooce_table(database_manager: DataManager, text=None) -> Any:
    if text:
        print(f"{text}\n")
    tables = database_manager._select_table()
    type_data(tables)
    i = input_validation(request_text="Выберите таблицу:\n")-1
    if i <= len(tables)-1:
        selected_table = tables[i]
    else: selected_table = False
    return selected_table


def choose_columns(columns: list) -> list:
    selected_columns = []
    while True:
        selected_columns.append(columns[int(input())-1])
        print("Ещё?")
        check = input_validation(request_text="1. Да\n2. Нет\n")
        if check == 2:
            break
    return selected_columns


def choose_values(items: list) -> list:
    values = []
    for item in items:
        values.append(input(f"Введите значение для {item}: "))
    return values


# def on_escape_pressed(e) -> None:
#     if e.event_type == keyboard.KEY_DOWN and e.name == 'esc':
#         command("cls")
#         print("Пока пока")
#         input()
#         quit()


def input_validation(request_text=None) -> int:
    if request_text:
        print(request_text)
        while True:
            try:
                value = int(input())
                break
            except ValueError:
                print("Неправильный ввод данных")
    else:
        while True:
            try:
                value = int(input())
                break
            except ValueError:
                print("Неправильный ввод данных")

    return value