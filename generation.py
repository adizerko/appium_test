from faker import Faker

faker = Faker()

class Generation:

    @staticmethod
    def text(max_nb_chars: int = 10) -> str:
        return faker.text(max_nb_chars)

    @staticmethod
    def username() -> str:
        return faker.user_name()

    @staticmethod
    def password() -> str:
        return faker.password()
