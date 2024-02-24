def become_warrior(first_name, last_name, power):
    name = f"{first_name} {last_name} the warrior"
    power = power + 1
    return name, power


# Don't edit below this line


def main():
    test("Frodo", "Baggins", 5)
    test("Bilbo", "Baggins", 10)
    test("Gandalf", "The Grey", 9000)


def test(first_name, last_name, power):
    title_string, power = become_warrior(first_name, last_name, power)
    print(title_string, "has a power level of:", power)


main()
