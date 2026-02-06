# Week 6 Example Problems: CodeGen / Planning

**Authors:** Xavier Schneider, Greg French, Max Ku

## Instructions

Problems A, B, and C will be completed in Python. Problem D may be completed in any language.

**GitHub Repository:**
https://github.com/Xavier-Schneider/CS846-CodeGen-Exercises

**Model:**  
Please use **Grok Code Fast 1** as the model to stay consistent with our results.

## 1. Example Problems

### Problem A Exam Score Analysis:

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
https://github.com/Xavier-Schneider/CS846-CodeGen-Exercises/blob/main/Problems/problem_A.py

---

### Problem A_2: [Title]

**Task Description:**  
Describe the task clearly and precisely.

**Starter Code:**  
// Include all necessary starter code here or in a repo and share the link.

---

### Problem A_n: [Title]

**Task Description:**  
Describe the task clearly and precisely.

**Starter Code:**  
// Include all necessary starter code here or in a repo and share the link.

---

### Problem B: Sudoku Puzzle Validator

**Description:**  
A [Sudoku puzzle](https://en.wikipedia.org/wiki/Sudoku) is a puzzle in which a user is given a 9x9 grid partially filled in with numbers 1-9. To complete the puzzle, the user must fill in each row, column, and 3x3 sub-square so that each contains exactly one number from 1-9. For a partially-completed puzzle, each row, column, and 3x3 sub-grid must contain at most one instance of numbers 1-9. In our case, an empty square will be represented by the character ‘*’. Your job is to write Python code to validate if a given Sudoku puzzle is valid or not.

To begin, start by downloading the code from here: https://github.com/Xavier-Schneider/CS846-CodeGen-Exercises

Once you’ve downloaded the code, run the following test command:
```
python3 -m unittest tests.test_problem_B
```

You should see 15 failing tests. If you see 15 failing tests, you can move on to problem B_1.

**Starter Code:**  
https://github.com/Xavier-Schneider/CS846-CodeGen-Exercises (The files required are Problems/problem_B.py and tests/test_problem_B.py)

### Problem B_1: Validate rows

**Task Description:**  
Write Python code for the ‘validate_rows’ method in the SudokuPuzzleValidator class such that it returns ‘True’ if no row contains duplicate numbers and  ‘False’ if at least one does.

Re-run the test command:
```
python3 -m unittest tests.test_problem_B
```

You should now see only 10 failing tests. If you see 10 failing tests, you can move on to problem B_2.

---

### Problem B_2: Validate columns

**Task Description:**  
Write Python code for the ‘validate_cols’ method in the SudokuPuzzleValidator class such that it returns ‘True’ if no column contains duplicate numbers and  ‘False’ if at least one does.

Re-run the test command:
```
python3 -m unittest tests.test_problem_B
```

You should now see only 5 failing tests. If you see 5 failing tests, you can move on to problem B_3.

---

### Problem B_3: Validate sub-grids

**Task Description:**  
Write Python code for the ‘validate_boxes’ method in the SudokuPuzzleValidator class such that it returns ‘True’ if no 3x3 sub-grid contains duplicate numbers and  ‘False’ if at least one does.

Re-run the test command:
```
python3 -m unittest tests.test_problem_B
```

You should now see all tests passing. Hooray!

---

### Problem C: INI Config Validator + Normalizer

Description:
INI files are a common way to store simple configuration using sections and key=value pairs. In this problem, you will implement a restricted INI parser that can both validate an INI-like text input and normalize it into a canonical format.

Your goal is to write Python code that takes an INI config string and:

Validates it according to the rules in Problems/problem_C.py

Parses it into an internal mapping

Outputs a normalized INI string with sorted sections/keys and standardized formatting

To begin, start by downloading the code from here: https://github.com/Xavier-Schneider/CS846-CodeGen-Exercises

Once you’ve downloaded the code, run the following test command:

```
python3 -m unittest tests.test_problem_C
```

You should see failing tests. If you see failing tests, you can move on to problem C_1.


### Problem C_1: Validate + normalize a single section

Task Description:
Implement `problem_C(text)` in `Problems/problem_C.py` so that it can correctly handle:

* A single section like `[db]`
* Multiple `key=value` lines inside that section
* Whitespace around keys/values
* Blank lines
* Trailing comments (`;` or `#`)

Return the normalized output using the canonical formatting rules.

Re-run the test command:

```
python3 -m unittest tests.test_problem_C
```

You should now see fewer failing tests. If the remaining failures mention sorting or multiple sections, you can move on to problem C_2.

### Problem C_2: Sorting + multi-section normalization

Task Description:
Extend `problem_C(text)` so that it can correctly handle multiple sections, and ensure the normalized output satisfies:

Sections sorted lexicographically

Keys sorted lexicographically within each section

Exactly one blank line between sections

Output ends with a final newline `\n`

Re-run the test command:

```
python3 -m unittest tests.test_problem_C
```

You should now see fewer failing tests. If the remaining failures mention duplicates or invalid input, move on to problem C_3.

### Problem C_3: Error handling (invalid inputs)

Task Description:
Update `problem_C(text)` so that it raises ValueError with a clear message whenever the input is invalid. Your error message must include:
* One of the required error code substrings:
  * `KEY_OUTSIDE_SECTION`
  * `INVALID_SECTION`
  * `DUPLICATE_SECTION`
  * `INVALID_KEY`
  * `DUPLICATE_KEY`
  * `INVALID_LINE`
* The 1-based line number substring like: `line 3`
Examples of invalid inputs you must detect:
* Key-value line before any section header
* Invalid section name (wrong characters)
* Duplicate section header
* Invalid key name (uppercase or illegal format)
* Duplicate key within a section
* Any non-empty non-comment line that is not a section header or key=value

Re-run the test command:

```
python3 -m unittest tests.test_problem_C
```
You should now see all tests passing. Hooray!


---

### Problem D: Building a personal website

**Task Description:**  
Every graduate student needs a website. Make one! You may use any technology available to you.

Build a website for a graduate student named [Name] who goes to the University of Waterloo. The website needs to be hosted on a server. Include an image of [Your favorite animal] on the website.

---

