import numpy as np

run = True

while run:
    print("\n================ NUMPY MENU ================")
    print("1. Create Array")
    print("2. Scalar Operations")
    print("3. Combine or Split Arrays")
    print("4. Search / Sort / Filter")
    print("5. Statistics")
    print("6. Exit")
    print("============================================")

    choice = input("Enter option (1-6): ")

    # --------------------  CREATE ARRAY --------------------
    if choice == "1":
        print("\n--- ARRAY CREATION ---")
        arr_type = input("Press 1 for 1D or 2 for 2D: ")

        if arr_type == "1":
            data = input("Enter numbers separated by space: ")
            data = data.split()
            arr_list = []
            for x in data:
                arr_list.append(int(x))
            arr = np.array(arr_list)
            print("1D Array:", arr)

        elif arr_type == "2":
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            print("Enter values row-wise:")

            matrix = []
            for i in range(rows):
                row_input = input()
                row_input = row_input.split()
                row_list = []
                for r in row_input:
                    row_list.append(int(r))
                matrix.append(row_list)

            arr = np.array(matrix)
            print("2D Array:\n", arr)

        else:
            print("Invalid array type!")
# --------------------  SCALAR OPERATIONS --------------------
    elif choice == "2":
        print("\n--- SCALAR OPERATIONS ---")
        nums = input("Enter array values separated by space: ")
        nums = nums.split()
        arr_list = []
        for x in nums:
            arr_list.append(int(x))
        arr = np.array(arr_list)

        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        op = input("Choose operation: ")
        s = int(input("Enter scalar value: "))

        if op == "1":
            print("Result:", arr + s)
        elif op == "2":
            print("Result:", arr - s)
        elif op == "3":
            print("Result:", arr * s)
        elif op == "4":
            print("Result:", arr / s)
        else:
            print("Invalid operation!")
# --------------------  COMBINE / SPLIT --------------------
    elif choice == "3":
        print("\n--- COMBINE / SPLIT ---")

        print("Enter first array:")
        a1_input = input().split()
        a1_list = []
        for x in a1_input:
            a1_list.append(int(x))
        arr1 = np.array(a1_list)

        print("Enter second array:")
        a2_input = input().split()
        a2_list = []
        for x in a2_input:
            a2_list.append(int(x))
        arr2 = np.array(a2_list)

        print("1. Combine Arrays")
        print("2. Split First Array")
        c = input("Choose option: ")

        if c == "1":
            combined = np.concatenate((arr1, arr2))
            print("Combined array:", combined)

        elif c == "2":
            parts = int(input("Enter number of parts: "))
            result = np.array_split(arr1, parts)
            for i in range(len(result)):
                print("Part", i+1, ":", result[i])
        else:
            print("Invalid choice!")

    # --------------------  SEARCH / SORT / FILTER --------------------
    elif choice == "4":
        print("\n--- SEARCH / SORT / FILTER ---")
        user_input = input("Enter array values separated by space: ").split()
        arr_list = []
        for x in user_input:
            arr_list.append(int(x))
        arr = np.array(arr_list)

        print("1. Search value")
        print("2. Sort array")
        print("3. Filter greater than value")
        act = input("Choose option: ")

        if act == "1":
            value = int(input("Enter value to search: "))
            positions = np.where(arr == value)[0]
            if len(positions) > 0:
                print("Found at indices:", positions)
            else:
                print("Value not found!")

        elif act == "2":
            sorted_arr = np.sort(arr)
            print("Sorted array:", sorted_arr)

        elif act == "3":
            limit = int(input("Enter threshold value: "))
            filtered = arr[arr > limit]
            print("Filtered values:", filtered)

        else:
            print("Invalid action!")
# --------------------  STATISTICS --------------------
    elif choice == "5":
        print("\n--- STATISTICS ---")
        inp = input("Enter numbers separated by space: ").split()
        arr_list = []
        for x in inp:
            arr_list.append(int(x))
        arr = np.array(arr_list)

        print("1. Mean")
        print("2. Median")
        print("3. Standard Deviation")
        print("4. Sum")
        st = input("Choose option: ")

        if st == "1":
            print("Mean:", np.mean(arr))
        elif st == "2":
            print("Median:", np.median(arr))
        elif st == "3":
            print("Standard Deviation:", np.std(arr))
        elif st == "4":
            print("Sum:", np.sum(arr))
        else:
            print("Invalid choice!")

    # --------------------  EXIT --------------------
    elif choice == "6":
        print("Exiting program...")
        run = False

    else:
        print("Invalid menu choice! Please enter 1-6.")