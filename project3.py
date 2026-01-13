print("STUDENT DATA ORGANIZER")

students = []       
student_dict = {}    

while True:
    print("\n1. Add Student")
    print("2. Show Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Show Unique Subjects")
    print("6. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        sid = int(input("Enter ID: "))
        name = input("Enter name: ")
        dob = input("Enter DOB (DD-MM-YYYY): ")
        age = int(input("Enter age: "))
        grade = input("Enter grade: ")

        subs = input("Enter subjects separated by comma: ")
        sub_list = subs.split(",")

        
        id_info = (sid, dob)

        
        info = {
            "id_info": id_info,
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": sub_list
        }

        students.append(info)
        student_dict[sid] = info

        print("Student added.")

    elif ch == "2":
        if len(students) == 0:
            print("No students yet.")
        else:
            for s in students:
                print("\nName:", s["name"])
                print("ID:", s["id_info"][0])
                print("DOB:", s["id_info"][1])
                print("Age:", s["age"])
                print("Grade:", s["grade"])
                print("Subjects:", ", ".join(s["subjects"]))

    elif ch == "3":
        sid = int(input("Enter ID to update: "))

        if sid in student_dict:
            st = student_dict[sid]
            print("1. Update Name")
            print("2. Update Age")
            print("3. Update Grade")
            print("4. Update Subjects")

            op = input("Enter option: ")

            if op == "1":
                st["name"] = input("New name: ")

            elif op == "2":
                st["age"] = int(input("New age: "))

            elif op == "3":
                st["grade"] = input("New grade: ")

            elif op == "4":
                new_sub = input("Enter subjects: ")
                st["subjects"] = new_sub.split(",")


            else:
              print("student not found.")
            
        elif ch=="4":
          sid=int(input("enter Id to delete:"))

          if sid in student_dict:
            for i in range(len(students)):
              if students[i]["id_info"][0]== sid:
                del students[i]
                break

            del student_dict[sid]
            print("student deleted.")
          else:
            print("Id not found.")

        elif ch == "5":
          sub_set= set()
          for s in students:
            for item in s["students"]:
              sub_set.add(item.strip())
              print("unique subjects:",sub_set)

        elif ch == "6":
          print("Thank You!")
          break

        else:
          print("Invalid choice.")