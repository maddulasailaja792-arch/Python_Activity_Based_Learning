import math

print("EXAMINATION RESULT AND GRACE-MARK VALIDATION")
print("-" * 50)

student_name = input("Enter student name: ")
n = int(input("Enter number of subjects: "))

MAX_GRACE = 5
PASS_PERCENTAGE = 35

total_marks = 0
total_maximum = 0
failed_subjects = 0

results = []

for i in range(n):
    print(f"\nSubject {i + 1}")

    subject = input("Enter subject name: ")
    maximum = int(input("Enter maximum marks: "))
    marks = int(input("Enter obtained marks: "))

    if maximum <= 0 or marks < 0 or marks > maximum:
        print("Invalid marks! Please enter valid marks.")
        continue

    pass_marks = math.ceil(maximum * PASS_PERCENTAGE / 100)
    grace = 0

    # Check subject-wise passing criteria
    if marks < pass_marks:
        required = pass_marks - marks

        # Apply grace marks only within the permitted limit
        if required <= MAX_GRACE and marks + required <= maximum:
            grace = required
            marks += grace
            print("Grace marks awarded:", grace)
        else:
            print("Grace marks cannot be awarded.")
            failed_subjects += 1

    else:
        print("No grace marks required.")

    # Validate the final marks
    if marks > maximum:
        marks = maximum

    if marks < pass_marks:
        status = "FAIL"
        failed_subjects += 1
    else:
        status = "PASS"

    results.append((subject, marks, maximum, grace, status))

    total_marks += marks
    total_maximum += maximum

# Display subject-wise results
print("\n" + "=" * 65)
print("FINAL EXAMINATION RESULT")
print("=" * 65)
print("Student Name:", student_name)
print("-" * 65)

print(f"{'Subject':<15}{'Marks':<12}{'Maximum':<12}"
      f"{'Grace':<10}{'Status':<10}")

for subject, marks, maximum, grace, status in results:
    print(f"{subject:<15}{marks:<12}{maximum:<12}"
          f"{grace:<10}{status:<10}")

if total_maximum > 0:
    percentage = (total_marks / total_maximum) * 100
else:
    percentage = 0

print("-" * 65)
print("Total Marks:", total_marks, "/", total_maximum)
print(f"Percentage: {percentage:.2f}%")

# Determine final result and classification
if failed_subjects > 0 or len(results) != n:
    classification = "FAIL"
elif percentage >= 75:
    classification = "DISTINCTION"
elif percentage >= 60:
    classification = "FIRST CLASS"
elif percentage >= 50:
    classification = "SECOND CLASS"
elif percentage >= 35:
    classification = "PASS CLASS"
else:
    classification = "FAIL"

print("Final Classification:", classification)
print("=" * 65)
