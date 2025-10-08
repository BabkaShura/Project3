import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()


def create_database() -> None:
    conn = psycopg2.connect(
        dbname="postgres", user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"), host=os.getenv("DB_HOST")
    )
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("DROP DATABASE IF EXISTS hh_vacancies")
    cur.execute("CREATE DATABASE hh_vacancies")
    cur.close()
    conn.close()
