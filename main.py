persons = []


def print_person():
    for person in persons:
        print(f"Firstname: {person['firstname']}")
        print(f"Lastname: {person['lastname']}")
        print(f"Age: {person['age']}")

def main():
    while True:
        person = {}
        print("Firstname?")
        person["firstname"] = input()
        print("Lastname?")
        person["lastname"] = input()
        while True:
            print("Age?")
            age_input = input().strip()
            if age_input.isdigit() and 0 < int(age_input):
                person["age"] = age_input
                break
        persons.append(person)
        break
    print_person()

if __name__ == "__main__":
    main()