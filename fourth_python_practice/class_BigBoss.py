from class_admin import *
import json


class BigBoss(Admin):
    def show_accounts(self, file_name: str) -> None:
        data = self.open_json(file_name)
        for i, (key, value) in enumerate(data.items()):
            print(f"{i+1}. Логин: {key}, пароль: {value}")


    def open_json(self, file_name: str) -> dict:
        with open(file_name, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data


    def edit_file(self, file_name: str) -> None:
        command("cls")
        while True:
            data = self.open_json(file_name)
            login_list = list(data.keys())
            password_list = list(data.values())
            menu = int(input("""Выберите действие:
        1. Изменть существующие данные
        2. Добавить нового админа
        3. Удалить логин
        4. Выход\n"""))
            command("cls")
            match menu:
                case 1:
                    while True:
                        self.show_accounts(file_name)
                        choose_action = int(input("""Выберите действие:
        1. Изменть логин
        2. Изменить пароль
        3. Сохранить
        4. Выход из \"Изменть существующие данные\"\n"""))
                        match choose_action:
                            case 1:
                                command("cls")
                                working_login_num = int(
                                    input("Выберите логин который хотите отредактировать:\n")) - 1
                                login_list[working_login_num] = input("Введите изменённый логин:\n")
                                print("Логин изменён!")
                            case 2:
                                command("cls")
                                working_password_num = int(
                                    input("Выберите пароль который хотите отредактировать:\n")) - 1
                                password_list[working_password_num] = input("Введите изменённый пароль:\n")
                                print("Пароль изменён!")
                            case 3:
                                command("cls")
                                accounts_dict = dict(zip(login_list, password_list))
                                with open(file_name, 'w', encoding="utf-8") as file:
                                    json.dump(accounts_dict, file, indent=4)
                                print("Данные успешно сохранены!")
                            case 4:
                                command("cls")
                                break
                case 2:
                    command("cls")
                    admin_dict = self.open_json(file_name)
                    new_admin_login = input("Введите логин нового админа: ")
                    new_admin_password = input("Введите пароль нового админа: ")
                    admin_dict[new_admin_login] = new_admin_password

                    with open(file_name, 'w', encoding="utf-8") as file:
                        json.dump(admin_dict, file, indent=4)
                case 3:
                    command("cls")
                    admin_dict = self.open_json(file_name)
                    print("Список аккаунтов: ")
                    self.show_accounts(file_name)
                    item_for_delete = input_validation(request_text="Выберите логин для удаления: ") - 1
                    keys_list = list(admin_dict.keys())
                    key_for_delete = keys_list[item_for_delete]
                    admin_dict.pop(key_for_delete)

                    with open(file_name, 'w', encoding="utf-8") as file:
                        json.dump(admin_dict, file, indent=4)

                    print("Аккаунт удалён)")
                case 4:
                    command("cls")
                    break


    def edit_accounts(self) -> None:
        admins_file = "admins_list.json"
        bosses_file = "bosses_list.json"
        print("Выберите файл для редактирования")
        print("1. admins_list.json")
        print("2. bosses_list.json")
        current_file = input_validation()
        match current_file:
            case 1:
                self.edit_file(admins_file)
            case 2:
                self.edit_file(bosses_file)


    def run_actions(self) -> int:
        try:
            while True:
                command("cls")
                actions = input_validation(request_text="""Вам доступны слудеющие действия:
1. Вывести данные в бухгалтерии
2. Добавить данные в бухгалетрию
3. Обновить данные из бухгалтерии
4. Удалить данные в бухгалтерии
5. Обновить списки доступа
6. Выход
""")
                command("cls")

                match actions:
                    case 1:
                        self.select_table()
                    case 2:
                        self.insert_data()
                    case 3:
                        self.update_data()
                    case 4:
                        self.delete_data()
                    case 5:
                        self.edit_accounts()
                    case 6:
                        print("Пока пока)")
                        return 15
        finally:
            self.database_manager.close_connection()