print("WELCOME TO PATTERN & NUMBER ANALYZER")
print("1. Pattern Generator")
print("2. Number Analyzer")
print("3. Exit")

choice = ""

while choice != "3":
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        rows = int(input("Enter number of rows: "))
        print("\nTriangle Pattern:\n")
        line = 1
        while line <= rows:
            print("*" * line)
            line += 1

    elif choice == "2":
        start = int(input("Enter starting number: "))
        end = int(input("Enter ending number: "))

        num = start
        total = 0

        while num <= end:
            if num % 2 == 0:
                print(num, "→ even")
            else:
                print(num, "→ odd")

            total += num
            num += 1

        print("Total sum from", start, "to", end, "is:", total)

     elif choice == "3":
        print("Thank you for using the tool. Goodbye!")

    else:
        print("Invalid choice! Please select 1, 2, or 3.")