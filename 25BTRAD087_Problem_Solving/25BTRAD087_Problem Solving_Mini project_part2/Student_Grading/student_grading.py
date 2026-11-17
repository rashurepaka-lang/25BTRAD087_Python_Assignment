print("========== STUDENT GRADING SYSTEM ==========")
print("Enter student details")
print("-" * 40)

name = input("Enter student name: ").strip()
while not name:
    print("Student name cannot be empty.")
    name = input("Enter student name: ").strip()

while True:
    try:
        num_subjects = int(input("Enter number of subjects: "))
        if num_subjects <= 0:
            print("Number of subjects must be greater than zero.")
            continue
        break
    except ValueError:
        print("Invalid input! Enter a whole number.")

marks = []
for i in range(num_subjects):
    subject = input(f"Enter subject {i+1} name: ").strip()
    while not subject:
        print("Subject name cannot be empty.")
        subject = input(f"Enter subject {i+1} name: ").strip()
    while True:
        try:
            mark = float(input(f"Enter marks for {subject} (out of 100): "))
            if not 0 <= mark <= 100:
                print("Marks must be between 0 and 100.")
                continue
            break
        except ValueError:
            print("Invalid input! Enter a numeric mark.")
    marks.append((subject, mark))

total = sum(m[1] for m in marks)
average = total / num_subjects

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B+"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F (Fail)"

print("\n" + "=" * 50)
print("              REPORT CARD")
print("=" * 50)
print(f"  Student Name : {name}")
print("-" * 50)
print(f"  {'Subject':<20} {'Marks':<10}")
print("-" * 50)

for subject, mark in marks:
    print(f"  {subject:<20} {mark:<10}")

print("-" * 50)
print(f"  {'Total':<20} {total}")
print(f"  {'Average':<20} {round(average, 2)}")
print(f"  {'Grade':<20} {grade}")
print("=" * 50)
print("  Result: PASS" if average >= 40 else "  Result: FAIL - Needs improvement")
print("=" * 50)
