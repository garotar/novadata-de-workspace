class Human:
    def __init__(
        self,
        name: str,
        age: int,
        job: str,
        experience: int
    ) -> None:
        self.name = name
        self.age = age
        self.job = job
        self.experience=experience

    def greeting(self) -> str:
        print(f"Hi! My name is {self.name}, I'm {self.age} years old. I work as {self.job} for OpenAI {self.experience} years of experience.")
        print(f"HAHAHHA Staryi Kon' borozdy ne isportit!")
        print(f"if we knew what it is...")


if __name__ == "__main__":
    human = Human("Roman", 150, "data engineer", experience=55)
    human.greeting()
