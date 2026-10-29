1. Problem Statement:
The Examination Result and Grace-Mark Validation system processes students' marks across multiple subjects. It checks subject-wise pass criteria, applies the specified grace-mark policy to eligible students, and generates final results and classifications. The system ensures that grace marks do not exceed the maximum marks for any subject.
2. Algorithm:
1. Start the program.
2. Input the student's name and number of subjects.
3. Input the maximum marks, obtained marks, and minimum pass marks for each subject.
4. Validate the entered marks.
5. Check whether the student has passed each subject.
6. If a student fails a subject by a small margin, check whether grace marks can help the student pass.
7. Apply grace marks according to the policy, without exceeding the maximum marks.
8. Calculate the total marks and percentage.
9. Determine the final result:
   - PASS: Passed all subjects.
   - FAIL: Failed one or more subjects after applying eligible grace marks.
10. Assign a classification based on the percentage.
11. Display the subject-wise marks, grace marks, total, percentage, result, and classification.
12. Stop the program.
3. Flowchart:
              ┌───────────────┐
              │     START     │
              └───────┬───────┘
                      │
                      ▼
          ┌────────────────────────┐
          │ Input student name and │
          │ number of subjects     │
          └───────────┬────────────┘
                      │
                      ▼
          ┌────────────────────────┐
          │ Input marks, maximum   │
          │ marks and pass marks   │
          └───────────┬────────────┘
                      │
                      ▼
          ┌────────────────────────┐
          │ Validate entered marks │
          └───────────┬────────────┘
                      │
                      ▼
             ◇ All subjects valid? ◇
                /             \
              No               Yes
              │                 │
              ▼                 ▼
       ┌─────────────┐  ┌─────────────────┐
       │ Show error  │  │ Check subject   │
       │ and re-enter│  │ pass criteria   │
       └──────┬──────┘  └────────┬────────┘
              │                  │
              └───► Input        ▼
                       ◇ Student passed? ◇
                           /       \
                         Yes        No
                          │          │
                          │          ▼
                          │   ◇ Eligible for
                          │     grace marks? ◇
                          │       /      \
                          │     Yes       No
                          │      │         │
                          │      ▼         │
                          │  ┌──────────┐  │
                          │  │ Apply    │  │
                          │  │ grace    │  │
                          │  │ marks    │  │
                          │  └────┬─────┘  │
                          │       │        │
                          │       ▼        │
                          │  Check pass    │
                          │  criteria again│
                          │       │        │
                          └───────┴────────┘
                                  │
                                  ▼
                       ┌──────────────────┐
                       │ Calculate total  │
                       │ and percentage   │
                       └────────┬─────────┘
                                │
                                ▼
                       ┌──────────────────┐
                       │ Determine PASS / │
                       │ FAIL and class   │
                       └────────┬─────────┘
                                │
                                ▼
                       ┌──────────────────┐
                       │ Display results  │
                       └────────┬─────────┘
                                │
                                ▼
                         ┌─────────────┐
                         │    STOP     │
                         └─────────────┘

4. Grace-Mark Policy and Classification
For this example, assume the following rules:
- Maximum grace marks: 5 marks per subject.
- Grace marks are given only if the student is short of the pass mark by 5 marks or fewer.
- Grace marks cannot increase a subject's marks beyond its maximum marks.
- A student must pass every subject to receive a PASS result.
- Classification is based on the final percentage.
Percentage	Classification
-
Percentage	Classification
75% and above	Distinction
60% to below 75%	First Class
50% to below 60%	Second Class
35% to below 50%	Pass Class
Below 35%	Fail
6:Sample input
Enter student name: Sailaja
Enter number of subjects: 3

Subject 1
Enter subject name: Mathematics
Enter maximum marks: 100
Enter minimum pass marks: 40
Enter obtained marks: 38

Subject 2
Enter subject name: Python
Enter maximum marks: 100
Enter minimum pass marks: 40
Enter obtained marks: 75

Subject 3
Enter subject name: English
Enter maximum marks: 100
Enter minimum pass marks: 40
Enter obtained marks: 82
