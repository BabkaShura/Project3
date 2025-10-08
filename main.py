from src.create_database import create_database
from src.create_tables import create_tables
from src.insert_data import insert_companies_and_vacancies
from src.user_interface import run_user_interface

companies = {
    "Яндекс": 1740,
    "Сбер": 3529,
    "VK": 15478,
    "Тинькофф": 78638,
    "OZON": 2180,
    "Газпромбанк": 39305,
    "Альфа-Банк": 80,
    "Ростелеком": 2748,
    "Skyeng": 1122462,
}

print("✅ Шаг 1: Создание базы данных...")
create_database()

print("✅ Шаг 2: Создание таблиц...")
create_tables()

print("✅ Шаг 3: Загрузка вакансий и компаний...")
insert_companies_and_vacancies(companies)

print("✅ Шаг 4: Запуск интерфейса...")
run_user_interface()
