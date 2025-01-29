from src import parse_input


def main():
    print("Final progect")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        print(command)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "task1":
            pass
        elif command == "task2":
            pass
        elif command == "task3":
            pass
        elif command == "task4":
            pass
        elif command == "task5":
            pass
        elif command == "task6":
            pass
        elif command == "task7":
            pass
        else:
            print("Unknown command")


if __name__ == "__main__":
    main()
