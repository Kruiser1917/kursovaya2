# tests/test_vacancy.py
import unittest
from src.vacancy import Vacancy


class TestVacancy(unittest.TestCase):
    def test_vacancy_creation(self):
        vacancy = Vacancy("Python Developer", "http://example.com", 100000, 150000, "Описание вакансии")
        self.assertEqual(vacancy.title, "Python Developer")
        self.assertEqual(vacancy.link, "http://example.com")
        self.assertEqual(vacancy.salary_from, 100000)
        self.assertEqual(vacancy.salary_to, 150000)
        self.assertEqual(vacancy.description, "Описание вакансии")

    def test_vacancy_comparison(self):
        vacancy1 = Vacancy("Python Developer", "http://example.com", 100000, 150000, "Описание вакансии")
        vacancy2 = Vacancy("Java Developer", "http://example.com", 120000, 180000, "Описание вакансии")
        self.assertTrue(vacancy1 < vacancy2)


if __name__ == "__main__":
    unittest.main()
