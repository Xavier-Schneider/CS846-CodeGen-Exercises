# Week 6 Example Problems: CodeGen / Planning

**Authors:** Xavier Schneider, Greg French, Max Ku

## Instructions

Problems A, B, and C will be completed in Python. Problem D may be completed in any language.

Throughout these exercises you will be asked to run unit tests. For example, to test problem A you will run the command:
```
python3 -m unittest tests.test_problem_A
```
Alternatively, you may have installed the python as: 'py' or 'python' instead of 'python3'. Make sure to adjust your commands accordingly.

**GitHub Repository:**
https://github.com/Xavier-Schneider/CS846-CodeGen-Exercises

**Model:**  
Please select **Grok Code Fast 1**

## 1. Example Problems

### Problem A: Sudoku Puzzle Validator (15 minutes)

**Description:**  
IMPORTANT: For problem A, pay close attention to how Copilot tries to test its own output. Allow Copilot to run the tests.

A [Sudoku puzzle](https://en.wikipedia.org/wiki/Sudoku) is a puzzle in which a user is given a 9x9 grid partially filled in with numbers 1-9. To complete the puzzle, the user must fill in each row, column, and 3x3 sub-square so that each contains exactly one number from 1-9. For a partially-completed puzzle, each row, column, and 3x3 sub-grid must contain at most one instance of numbers 1-9. In our case, an empty square will be represented by the character ‘*’. Your job is to write Python code to validate if a given Sudoku puzzle is valid or not.

To begin, run the following test command:

```
python3 -m unittest tests.test_problem_A
```

You should see 15 failing tests. If you see 15 failing tests, you can move on to problem A_1. (Every subproblem should fix 5 tests.)

**Starter Code:**  
https://github.com/Xavier-Schneider/CS846-CodeGen-Exercises/Problems/problem_A.py
https://github.com/Xavier-Schneider/CS846-CodeGen-Exercises/tests/test_problem_A.py

### Problem A_1: Validate rows

**Task Description:**  
Write Python code for the ‘validate_rows’ method in the SudokuPuzzleValidator class such that it returns ‘True’ if no row contains duplicate numbers and  ‘False’ if at least one does.

### Problem A_2: Validate columns

**Task Description:**  
Write Python code for the ‘validate_cols’ method in the SudokuPuzzleValidator class such that it returns ‘True’ if no column contains duplicate numbers and  ‘False’ if at least one does.

### Problem A_3: Validate sub-grids

**Task Description:**  
Write Python code for the ‘validate_boxes’ method in the SudokuPuzzleValidator class such that it returns ‘True’ if no 3x3 sub-grid contains duplicate numbers and  ‘False’ if at least one does.

**Test**
Test your solution with:

```
python3 -m unittest tests.test_problem_A
```

You should now see all tests passing. Hooray!

---

### Problem B Exam Score Analysis (10 minutes)

**Task Description:**  
You are given an iterable of student exam records.
Each record represents one student and must contain:

  - "name":   a non-empty string
  - "score":  a number between 0 and 100 (inclusive)
  - "weight": a positive number representing exam credit

Example input:

records = [
    {"name": "Alice", "score": 78, "weight": 1.0},
    {"name": "Bob", "score": 45, "weight": 0.5},
    {"name": "Charlie", "score": 88, "weight": 1.5},
    {"name": "Diana", "score": 60, "weight": 1.0},
    {"name": "Eve", "score": 52, "weight": 1.0},
]

------------------------------------------------------------
Complete the function to compute the following statistics:

1. Weighted Average Score
   - Compute the weighted average using:
       sum(score * weight) / sum(weight)
   - Round the result to two decimal places.

2. Top-Performing Student
   - Return the name of the student with the highest score.
   - If multiple students share the highest score, returning
     any one of them is acceptable.

3. Pass Rate
   - Calculate the percentage of students whose score is
     greater than or equal to the pass mark.
   - The default pass mark is 50.
   - Round the result to two decimal places.

4. Grade Distribution
   - Count how many students fall into each grade using
     the default boundaries:

       * A: score >= 70
       * B: score >= 60 and < 70
       * C: score >= 50 and < 60
       * F: score < 50

------------------------------------------------------------
Data validation requirements:

- The records iterable must not be None or empty
- Each record must be dict-like and include all required keys
- "name" must be a non-empty string
- "score" must be a valid number (not NaN) between 0 and 100
- "weight" must be a valid number (not NaN) greater than 0

If invalid data is encountered, raise an error with a clear,
descriptive message explaining the problem.

------------------------------------------------------------
Final output:

Produce a summary dictionary with the following keys:

  - "count": total number of student records
  - "weighted_average": weighted average score (float)
  - "top_student": name of the top-performing student (string)
  - "pass_rate": percentage of passing students (float)
  - "grade_distribution": dictionary mapping grades to counts

Example output shape:

{
    "count": 5,
    "weighted_average": 70.33,
    "top_student": "Charlie",
    "pass_rate": 80.0,
    "grade_distribution": {"A": 2, "B": 1, "C": 1, "F": 1}
}

**Starter Code:**
https://github.com/Xavier-Schneider/CS846-CodeGen-Exercises/blob/main/Problems/problem_B.py

**Test**
Test your solution with:
```
python3 -m unittest tests.test_problem_B
```
---

### Problem C: INI Config Validator + Normalizer (10 minutes)

**Task Description:**  
INI files are a common way to store simple configuration using sections and key=value pairs. In this problem, you will implement a restricted INI parser that can both validate an INI-like text input and normalize it into a canonical format.

Your goal is to write Python code that takes an INI config string and outputs a normalized INI string with sorted sections/keys and standardized formatting.

**Starter Code:**
https://github.com/Xavier-Schneider/CS846-CodeGen-Exercises/Problems/problem_C.py

**Test**
Test your solution with:

```
python3 -m unittest tests.test_problem_C
```

### Problem D: Building a Personal Website (10 minutes)

**Task Description:**  
Every graduate student needs a website. Make one! You may use any technology available to you.

Build a website for a graduate student named [Name] who goes to the University of Waterloo. The website needs to be hosted on a server. Include an image of [Your favorite animal] on the website.

---

