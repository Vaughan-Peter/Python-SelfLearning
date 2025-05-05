# manager.py

from name_model import Person
import file_handler

class NameManager:
    def __init__(self, data_file='names.dat'):
        self.data_file = data_file
        self.people = file_handler.load_data(self.data_file)

    def add_person(self, first_name, last_name):
        person = Person(first_name, last_name)
        self.people.append(person)
        self._save()

    def list_people(self):
        return self.people

    def search_person(self, query):
        return [p for p in self.people if p.matches(query)]

    def delete_person(self, query):
        before = len(self.people)
        self.people = [p for p in self.people if not p.matches(query)]
        self._save()
        return before - len(self.people)

    def _save(self):
        file_handler.save_data(self.people, self.data_file)