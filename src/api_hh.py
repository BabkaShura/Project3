from typing import Dict
from typing import List

import requests


def get_employers_vacancies(employer_ids: List[int], per_page: int = 100) -> List[Dict]:
    all_vacancies = []
    for employer_id in employer_ids:
        page = 0
        while True:
            response = requests.get(
                "https://api.hh.ru/vacancies", params={"employer_id": employer_id, "per_page": per_page, "page": page}
            )
            data = response.json()
            all_vacancies.extend(data["items"])
            if data["pages"] - 1 <= page:
                break
            page += 1
    return all_vacancies
