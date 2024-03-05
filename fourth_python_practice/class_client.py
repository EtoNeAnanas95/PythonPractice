from class_human import *


class Client(Human):
    def run_actions(self):
        try:
            while True:
                command("cls")
                actions = input_validation(request_text="""Вам доступны слудеющие действия:
1. Вывести данные из бухгалтерии
2. Выход
""")
                command("cls")

                match actions:
                    case 1:
                        self.select_table()
                    case 2:
                        print("Пока пока)")
        finally:
            self.database_manager.close_connection()