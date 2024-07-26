from abc import ABC, abstractmethod


class FileManager(ABC):
    @abstractmethod
    def save(self, vacancies: list):
        pass

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def delete(self, vacancy_id: str):
        pass
