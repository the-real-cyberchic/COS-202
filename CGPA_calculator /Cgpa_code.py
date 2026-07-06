print("    PERSONAL POCKET CGPA CALCULATOR")

number_of_courses = int(input("Enter the number of courses: "))

total_course_units = 0
total_grade_points = 0

for course_number in range(number_of_courses):

    print("\nCourse", course_number + 1)

    course_unit = int(input("Enter course unit: "))
    grade = input("Enter grade (A-F): ").upper()

    match grade:
        case "A":
            grade_point = 5
        case "B":
            grade_point = 4
        case "C":
            grade_point = 3
        case "D":
            grade_point = 2
        case "E":
            grade_point = 1
        case "F":
            grade_point = 0
        case _:
            print("Invalid grade! Course skipped.")
            continue

    total_course_units = total_course_units + course_unit
    total_grade_points = total_grade_points + (course_unit * grade_point)

if total_course_units > 0:
    cgpa = total_grade_points / total_course_units

    print("\n" + "=" * 40)
    print("RESULT")
    print("=" * 40)
    print("Total Course Units:", total_course_units)
    print("Total Grade Points:", total_grade_points)
    print("CGPA:", round(cgpa, 2))
else:
    print("No valid courses entered.")
