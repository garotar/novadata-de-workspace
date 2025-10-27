class Human:
    def __init__(
        self,
        name: str,
        age: int,
        job: str
    ) -> None:
        self.name = name
        self.age = age
        self.job = job

    def greeting(self) -> str:
        print(f"Hi! My name is {self.name}, I'm {self.age} years old. I work as {self.job} for OpenAI.")
        print(f"HAHAHHA Staryi Kon' borozdy ne isportit!")
        print(f"if we knew what it is...")


if __name__ == "__main__":
    human = Human("Roman", 150, "data engineer")
    human.greeting()
