students = []
while True:
    print('1 Add 2 Display 3 Search 4 Update 5 Delete 6 Name sort 7 Marks sort 8 Topper 9 Average 10 Exit')
    choice = input('Choose: ')
    if choice == '1':
        students.append([input('Name: '), float(input('Marks: '))])
    elif choice == '2':
        print(students)
    elif choice == '3':
        name = input('Name: ')
        print([student for student in students if student[0] == name])
    elif choice == '4':
        name = input('Name: ')
        for student in students:
            if student[0] == name:
                student[1] = float(input('New marks: '))
    elif choice == '5':
        name = input('Name: ')
        students = [student for student in students if student[0] != name]
    elif choice == '6':
        students.sort(key=lambda student: student[0])
    elif choice == '7':
        students.sort(key=lambda student: student[1], reverse=True)
    elif choice == '8':
        print(max(students, key=lambda student: student[1]) if students else 'No records')
    elif choice == '9':
        print(sum((student[1] for student in students)) / len(students) if students else 'No records')
    elif choice == '10':
        break
