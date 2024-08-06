name = input("What is your name? ")

match name:
    case "Ragnar" | "Floki" | "Rollo" | "Lagertha":
        print("Norway")
    case "Jon Snow":
        print("Winterfell")
    case _:
        print("Who?")