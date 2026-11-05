import json
import os

DB_FILE = "database.json"

def load_persons() -> list:
    if not os.path.exists(DB_FILE):
        return []
    try:
        with open(DB_FILE, "r", encoding="utf-8") as file:
            return json.load(file);
    except json.JSONDecodeError:
        return []

def save_persons(persons: list) -> None:
    with open(DB_FILE, "w", encoding="utf-8") as file:
        json.dump(persons, file, indent=4, ensure_ascii=False)

def is_age(age: str) -> bool:
    return age.isdigit() and int(age) > 0

def main():
    persons = load_persons()
    while True:
        person = {}
        print("Firstname?")
        person["firstname"] = input().strip()
        print("Lastname?")
        person["lastname"] = input().strip()
        while True:
            print("Age?")
            age_input = input().strip()
            if is_age(age_input):
                person["age"] = int(age_input)
                break
        persons.append(person)
        save_persons(persons)
        
if __name__ == "__main__":
    main()
    assert(is_age("19") == True)
    assert(is_age("0") == False)
