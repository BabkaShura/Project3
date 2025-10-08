import os
from typing import Any

import psycopg2
from dotenv import load_dotenv

load_dotenv()


def get_connection() -> Any:
    return psycopg2.connect(
        dbname="hh_vacancies", user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"), host=os.getenv("DB_HOST")
    )
