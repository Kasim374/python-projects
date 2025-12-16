while True:
    print("==========================================================================")
    print("             Welcome to Personal Journal Manager             ")
    print("==========================================================================")
    print(" * Please select an Option ")
    print("1. Add a New Entry:")
    print("2. View All Entries:")
    print("3. Search for an Entry:")
    print("4. Delete an Entry:")
    print("5. Exit")

    choice = int(input("Select an option from (1-5): "))

    if choice == 1:
        with open("journal.txt", "a") as file:
            entry = input("Write your journal entry:\n")
            file.write(entry + "\n")
        print("Entry added successfully!")

    elif choice == 2:
        try:
            with open("journal.txt", "r") as file:
                print("Your Journal Entries:")
                print(file.read())
        except FileNotFoundError:
            print("No journal entries found.")

    elif choice == 3:
        keyword = input("Enter a keyword to search for: ")
        try:
            with open("journal.txt", "r") as file:
                entries = file.readlines()

            found = False
            print("Search Results:")
            for entry in entries:
                if keyword.lower() in entry.lower():
                    print(entry.strip())
                    found = True

            if not found:
                print("No entries found with the given keyword.")
        except FileNotFoundError:
            print("Journal file not found.")

    elif choice == 4:
        keyword = input("Enter a keyword to delete entries: ")
        try:
            with open("journal.txt", "r") as file:
                entries = file.readlines()

            with open("journal.txt", "w") as file:
                deleted = False
                for entry in entries:
                    if keyword.lower() not in entry.lower():
                        file.write(entry)
                    else:
                        deleted = True

            if deleted:
                print("Entries containing the keyword have been deleted.")
            else:
                print("No entries found with the given keyword.")
        except FileNotFoundError:
            print("Journal file not found.")

    elif choice == 5:
        print("Exiting the Journal Manager. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option (1-5).")
