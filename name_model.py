# name_model.py

class Person:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    def get_full_name(self):
        return f"{self.__first_name} {self.__last_name}"

    def matches(self, name):
        return name.lower() in self.get_full_name().lower()

    def __str__(self):
        return self.get_full_name()