class Vacancy:
    def __init__(self, title: str, link: str, salary_from: int,
                 salary_to: int, description: str):
        self.title = title
        self.link = link
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.description = description

    def __str__(self):
        return (f"Vacancy(title={self.title}, salary_from={self.salary_from}, "
                f"salary_to={self.salary_to})")

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.salary_from == other.salary_from and self.salary_to == other.salary_to

    def __lt__(self, other):
        return (self.salary_from or 0) < (other.salary_from or 0)
