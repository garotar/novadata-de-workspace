class Human:
    def __init__(
        self,
        name: str,
        surname: str,
        age: int,
        job: str,
        company: str,
    ) -> None:
        self.name = name
        self.surname = surname
        self.age = age
        self.job = job
        self.company = company


    def greeting(self) -> str:
        print(f"Hi! My name is {self.name} {self.surname}, I'm {self.age} years old. "
              f"I work as {self.job} for {self.company}. And I totally forgot object oriented programming.")


if __name__ == "__main__":
    human = Human("Vasya", "Bulkin", 18, "programmer", "Deep Sick")
    human.greeting()
