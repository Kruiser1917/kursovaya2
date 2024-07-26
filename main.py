from src.hh_client import HHClient
from src.json_file_manager import JSONFileManager
from src.vacancy import Vacancy


def filter_vacancies_by_salary(vacancies, min_salary, max_salary):
    return [vacancy for vacancy in vacancies if
            (vacancy['salary']['from'] or 0) >= min_salary and (vacancy['salary']['to'] or float('inf')) <= max_salary]


def user_interaction():
    hh_client = HHClient()
    file_manager = JSONFileManager('data/vacancies.json')

    while True:
        print("\n1. Поиск вакансий")
        print("2. Показать топ N вакансий по зарплате")
        print("3. Показать вакансии с ключевым словом")
        print("4. Удалить вакансию по ID")
        print("5. Показать вакансии по диапазону зарплат")
        print("6. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            keyword = input("Введите ключевое слово для поиска вакансий: ")
            vacancies = hh_client.get_vacancies(keyword)
            file_manager.save(vacancies)
            print("Вакансии сохранены.")

        elif choice == '2':
            n = int(input("Введите количество вакансий для вывода: "))
            vacancies = file_manager.load()
            vacancies = sorted(vacancies, key=lambda x: x['salary']['from'], reverse=True)[:n]
            for vacancy in vacancies:
                print(vacancy)

        elif choice == '3':
            keyword = input("Введите ключевое слово для фильтрации вакансий: ")
            vacancies = file_manager.load()
            filtered_vacancies = [v for v in vacancies if keyword.lower() in v['snippet']['requirement'].lower()]
            for vacancy in filtered_vacancies:
                print(vacancy)

        elif choice == '4':
            vacancy_id = input("Введите ID вакансии для удаления: ")
            file_manager.delete(vacancy_id)
            print("Вакансия удалена.")

        elif choice == '5':
            min_salary = int(input("Введите минимальную зарплату: "))
            max_salary = int(input("Введите максимальную зарплату: "))
            vacancies = file_manager.load()
            filtered_vacancies = filter_vacancies_by_salary(vacancies, min_salary, max_salary)
            for vacancy in filtered_vacancies:
                print(vacancy)

        elif choice == '6':
            break


if __name__ == "__main__":
    user_interaction()
