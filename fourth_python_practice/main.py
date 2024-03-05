from class_client import *
from class_BigBoss import *


def authorization(user: Human, users: dict) -> None:
    i = 0
    while i != 15:
        command("cls")
        login = input("Введите логин:\n")
        password = input("Введите пароль:\n")
        if login in users and users[login] == password:
            i = user.run_actions()
        else:
            i += 1
            print("Неверен логин или пароль")
            print(f"У вас осталось {15 - i} попыток")
            input()

while True:
    try:
        command("cls")


        with open("admins_list.json", "r", encoding="utf-8") as file:
            users = json.load(file)
        with open("bosses_list.json", "r", encoding="utf-8") as file:
            users_bosses = json.load(file)

        print("Войти как:")
        print("1. Клиент")
        print("2. Админ")
        print("3. Биг босс")
        print("4. Выход")
        menu = input_validation()

        match menu:
            case 1:
                client = Client()
                client.run_actions()
            case 2:
                admin = Admin()
                authorization(admin, users)
            case 3:
                boss = BigBoss()
                authorization(boss, users_bosses)
            case 4:
                print("Пока пока")
                quit()
    except Exception as e: print(f"Произошла ошибка {e}, попробуйте войти снова")