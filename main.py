import sys

def show_menu():
    print("\nWelcome to OpenCyb3r")
    print("=====================")
    print("1. Hash Generator")
    print("2. Exit")
    return input("Choose an option: ")

def hash_generator_tool():
    import hash_generator
    hash_generator.main()

def main():
    while True:
        choice = show_menu()
        if choice == "1":
            hash_generator_tool()
        elif choice == "2":
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()