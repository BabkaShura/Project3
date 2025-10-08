import unicodedata
from typing import Any

from src.db_config import get_connection


class DBManager:
    def __init__(self) -> None:
        self.conn = get_connection()
        self.cur = self.conn.cursor()

    def get_companies_and_vacancies_count(self) -> Any:
        self.cur.execute(
            """
            SELECT c.name, COUNT(v.id)
            FROM companies c
            JOIN vacancies v ON c.id = v.company_id
            GROUP BY c.name
        """
        )
        return self.cur.fetchall()

    def get_all_vacancies(self) -> Any:
        self.cur.execute(
            """
            SELECT c.name, v.title, v.salary_from, v.salary_to, v.url
            FROM vacancies v
            JOIN companies c ON c.id = v.company_id
        """
        )
        return self.cur.fetchall()

    def get_avg_salary(self) -> Any:
        self.cur.execute(
            """
            SELECT AVG((COALESCE(salary_from, 0) + COALESCE(salary_to, 0)) / 2)
            FROM vacancies
            WHERE salary_from IS NOT NULL AND salary_to IS NOT NULL
        """
        )
        return self.cur.fetchone()[0]

    def get_vacancies_with_higher_salary(self) -> Any:
        avg = self.get_avg_salary()
        self.cur.execute(
            """
            SELECT c.name, v.title, v.salary_from, v.salary_to, v.url
            FROM vacancies v
            JOIN companies c ON v.company_id = c.id
            WHERE ((COALESCE(salary_from, 0) + COALESCE(salary_to, 0)) / 2) > %s
        """,
            (avg,),
        )
        return self.cur.fetchall()

    def get_vacancies_with_keyword(self, keyword: str) -> Any:
        # Очистка ключевого слова от управляющих символов
        cleaned_keyword = "".join(c for c in keyword if unicodedata.category(c)[0] != "C")

        self.cur.execute(
            """
            SELECT c.name, v.title, v.salary_from, v.salary_to, v.url
            FROM vacancies v
            JOIN companies c ON v.company_id = c.id
            WHERE v.title ILIKE %s
        """,
            (f"%{cleaned_keyword}%",),
        )
        return self.cur.fetchall()
