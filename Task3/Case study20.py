```python
# University Admission Decision Engine

# Course-specific eligibility criteria
course_criteria = {
    "CSE": {
        "min_aggregate": 75,
        "min_math": 60,
        "min_physics": 60
    },
    "ECE": {
        "min_aggregate": 65,
        "min_math": 50,
        "min_physics": 50
    }
}

applicants = []

n = int(input("Enter number of applicants: "))

for i in range(n):
    print(f"\nEnter details of applicant {i + 1}")

    name = input("Applicant name: ")
    course = input("Course (CSE/ECE): ").upper()

    math = int(input("Mathematics marks (out of 100): "))
    physics = int(input("Physics marks (out of 100): "))
    chemistry = int(input("Chemistry marks (out of 100): "))
    entrance = int(input("Entrance examination score: "))

    total = math + physics + chemistry
    aggregate = (total / 300) * 100

    if course not in course_criteria:
        print("Invalid course. Applicant is ineligible.")
        continue

    criteria = course_criteria[course]

    eligible = (
        aggregate >= criteria["min_aggregate"]
        and math >= criteria["min_math"]
        and physics >= criteria["min_physics"]
    )

    applicant = {
        "name": name,
        "course": course,
        "math": math,
        "physics": physics,
        "aggregate": aggregate,
        "entrance": entrance,
        "eligible": eligible
    }

    applicants.append(applicant)

# Separate eligible and ineligible applicants
eligible_applicants = [
    a for a in applicants if a["eligible"]
]

ineligible_applicants = [
    a for a in applicants if not a["eligible"]
]

# Ranking criteria:
# 1. Higher aggregate percentage
# 2. Higher entrance examination score
# 3. Higher Mathematics marks

eligible_applicants.sort(
    key=lambda a: (
        a["aggregate"],
        a["entrance"],
        a["math"]
    ),
    reverse=True
)

# Display ranked eligible applicants
print("\n===== RANKED ELIGIBLE APPLICANTS =====")

if eligible_applicants:
    for rank, applicant in enumerate(
        eligible_applicants, start=1
    ):
        print(
            f"Rank: {rank} | "
            f"Name: {applicant['name']} | "
            f"Course: {applicant['course']} | "
            f"Aggregate: {applicant['aggregate']:.2f}% | "
            f"Entrance Score: {applicant['entrance']}"
        )
else:
    print("No eligible applicants found.")

# Display ineligible applicants
print("\n===== INELIGIBLE APPLICANTS =====")

if ineligible_applicants:
    for applicant in ineligible_applicants:
        print(
            f"Name: {applicant['name']} | "
            f"Course: {applicant['course']} | "
            f"Aggregate: {applicant['aggregate']:.2f}% | "
            f"Status: Ineligible"
        )
else:
    print("No ineligible applicants.")
```
