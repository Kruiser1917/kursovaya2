import requests
from .api_client import JobAPI


class HHClient(JobAPI):
    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}

    def get_vacancies(self, keyword: str):
        self.params['text'] = keyword
        vacancies = []
        for page in range(20):  # Example to limit to 20 pages
            self.params['page'] = page
            response = requests.get(self.url, headers=self.headers, params=self.params)
            response.raise_for_status()  # Check for request errors
            data = response.json()
            vacancies.extend(data.get('items', []))
        return vacancies
