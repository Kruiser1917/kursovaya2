# src/json_file_manager.py
import json
from .file_manager import FileManager

class JSONFileManager(FileManager):
    def __init__(self, filename: str):
        self.filename = filename

    def save(self, vacancies: list):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=4)

    def load(self):
        with open(self.filename, 'r', encoding='utf-8') as f:
            return json.load(f)

    def delete(self, vacancy_id: str):
        vacancies = self.load()
        vacancies = [vacancy for vacancy in vacancies if vacancy['id'] != vacancy_id]
        self.save(vacancies)
