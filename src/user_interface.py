import unicodedata

from src.db_manager import DBManager


def clean_keyword(text: str) -> str:
    """
    Удаляет управляющие (непечатные) символы, включая surrogate-пары.
    """
    return "".join(c for c in text if unicodedata.category(c)[0] != "C")


def run_user_interface() -> None:
    db = DBManager()
    while True:
        print("\nВыберите действие:")
        print("1. Компании и кол-во вакансий")
        print("2. Все вакансии")
        print("3. Средняя зарплата")
        print("4. Вакансии выше средней")
        print("5. Поиск по ключевому слову")
        print("0. Выход")
        choice = input("Ваш выбор: ")

        if choice == "1":
            for row in db.get_companies_and_vacancies_count():
                print(f"{row[0]} — {row[1]} вакансий")
        elif choice == "2":
            for row in db.get_all_vacancies():
                print(row)
        elif choice == "3":
            print(f"Средняя зарплата: {db.get_avg_salary():.2f}")
        elif choice == "4":
            for row in db.get_vacancies_with_higher_salary():
                print(row)
        elif choice == "5":
            kw = input("Введите ключевое слово: ").strip()
            kw_clean = clean_keyword(kw)
            try:
                for row in db.get_vacancies_with_keyword(kw_clean):
                    print(row)
            except Exception as e:
                print(f"❌ Ошибка при поиске: {e}")
        elif choice == "0":
            break
        else:
            print("Неверный ввод.")
