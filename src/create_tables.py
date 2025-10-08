
from src.db_config import get_connection


def create_tables() -> None:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        CREATE TABLE companies (
            id SERIAL PRIMARY KEY,
            name VARCHAR NOT NULL,
            hh_id INT UNIQUE
        );
    """
    )

    cur.execute(
        """
        CREATE TABLE vacancies (
            id SERIAL PRIMARY KEY,
            company_id INT REFERENCES companies(id),
            title VARCHAR NOT NULL,
            salary_from INT,
            salary_to INT,
            url TEXT
        );
    """
    )

    conn.commit()
    cur.close()
    conn.close()
