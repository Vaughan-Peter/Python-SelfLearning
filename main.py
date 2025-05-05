# main.py

from manager import NameManager

def display_menu():
    print("\nName Manager")
    print("1. Add Name")
    print("2. View All Names")
    print("3. Search for a Name")
    print("4. Delete a Name")
    print("5. Exit")

def main():
    nm = NameManager()

    while True:
        display_menu()
        choice = input("Enter choice: ").strip()

        if choice == '1':
            first = input("First name: ").strip()
            last = input("Last name: ").strip()
            nm.add_person(first, last)
            print("Name added.")
        elif choice == '2':
            for p in nm.list_people():
                print(f"- {p}")
        elif choice == '3':
            q = input("Search query: ").strip()
            results = nm.search_person(q)
            if results:
                print("Matches found:")
                for p in results:
                    print(f"- {p}")
            else:
                print("No matches found.")
        elif choice == '4':
            q = input("Name to delete: ").strip()
            count = nm.delete_person(q)
            print(f"{count} name(s) deleted.")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()