print("==============================================")
print("        SIMPLE DATA ANALYSIS PROGRAM          ")
print("==============================================")

import pandas as pd
import matplotlib.pyplot as plt

data_loaded = False
data = None

while True:
    print("\nChoose an option:")
    print("1. Load CSV File")
    print("2. View Dataset Info")
    print("3. Select Columns")
    print("4. Fix Missing Values")
    print("5. Show Statistics")
    print("6. Draw Graph")
    print("7. Save Graph")
    print("8. Exit")

    try:
        opt = int(input("Enter choice (1-8): "))
    except:
        print("Please enter numbers only.")
        continue

if opt == 1:
        file_name = input("Enter CSV file path: ")
        try:
            data = pd.read_csv(file_name)
            data_loaded = True
            print("File loaded!")
        except:
            print("Could not open file. Try again.")
elif opt == 2:
        if data_loaded:
            print("\nFirst five rows:")
            print(data.head())

            print("\nInformation:")
            print(data.info())

            print("\nDescription:")
            print(data.describe())
        else:
            print("Load a file first (Option 1).")
elif opt == 3:
        if data_loaded:
            print("Columns available:")
            print(list(data.columns))

            cols = input("Enter columns separated by commas: ")
            col_list = [c.strip() for c in cols.split(",")]

            try:
                print(data[col_list].head())
            except:
                print("Column name not found.")
        else:
            print("Load a file first.")
elif opt == 4:
        if data_loaded:
            data = data.fillna(method="ffill")
            print("Missing values filled using forward fill.")
        else:
            print("Load a file first.")
elif opt == 5:
        if data_loaded:
            print("Statistics:")
            print(data.describe())
        else:
            print("Load a file first.")
elif opt == 6:
        if data_loaded:
            col = input("Enter column name to plot: ")
            try:
                plt.hist(data[col].dropna(), bins=20)
                plt.title("Histogram of " + col)
                plt.xlabel(col)
                plt.ylabel("Count")
                plt.show()
            except:
                print("Column name not valid.")
        else:
            print("Load a file first.")
elif opt == 7:
        try:
            save_file = input("Enter file name to save graph (ex: graph.png): ")
            plt.savefig(save_file)
            print("Graph saved!")
        except:
            print("Could not save the file.")
elif opt == 8:
        print("Program closed.")
        break
else:
        print("Invalid option. Choose between 1-8.")