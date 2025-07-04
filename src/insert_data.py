from src.api_hh import get_employers_vacancies
from src.db_config import get_connection


def insert_companies_and_vacancies(employers: dict) -> None:
    conn = get_connection()
    cur = conn.cursor()

    for name, hh_id in employers.items():
        print(f"📡 Загружаем компанию: {name} (hh_id={hh_id})")
        cur.execute("INSERT INTO companies (name, hh_id) VALUES (%s, %s) RETURNING id", (name, hh_id))
        company_db_id = cur.fetchone()[0]

        print(f"📨 Получаем вакансии компании: {name}")
        vacancies = get_employers_vacancies([hh_id])

        print(f"🔽 Вставляем {len(vacancies)} вакансий в БД")
        for vacancy in vacancies:
            salary = vacancy.get("salary")
            salary_from = salary.get("from") if salary else None
            salary_to = salary.get("to") if salary else None

            cur.execute(
                """
                INSERT INTO vacancies (company_id, title, salary_from, salary_to, url)
                VALUES (%s, %s, %s, %s, %s)
            """,
                (company_db_id, vacancy["name"], salary_from, salary_to, vacancy["alternate_url"]),
            )

    conn.commit()
    cur.close()
    conn.close()
