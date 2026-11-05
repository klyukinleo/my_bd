persons = []


def print_person():
    for person in persons:
        print(f"Firstname: {person['firstname']}")
        print(f"Lastname: {person['lastname']}")
        print(f"Age: {person['age']}")

def is_age(age):
    return age.isdigit() and int(age) > 0

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
            if is_age(age_input):
                person["age"] = age_input
                break
        persons.append(person)
        break
    print_person()

if __name__ == "__main__":
    main()
    assert(is_age("19") == True)
    assert(is_age("0") == False)