from __future__ import annotations


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    people: dict[str, Person] = {}


def create_person_list(people: list[dict]) -> list[Person]:
    instances = [Person(p["name"], p["age"]) for p in people]

    for person_dict in people:
        name = person_dict["name"]
        instance = Person.people[name]

        if person_dict.get("wife") is not None:
            instance.wife = Person.people[person_dict["wife"]]
        elif person_dict.get("husband") is not None:
            instance.husband = Person.people[person_dict["husband"]]

    return instances
