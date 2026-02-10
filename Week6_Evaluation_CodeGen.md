# Week 6 Evaluation: CodeGen / Planning

**Authors:** Xavier Schneider, Greg French, Max Ku 

## 1. Evaluation Criteria

* The code should pass the automated tests (correctness)
* The code should be readable
* The code should be well-architected (modular, extensible, etc.)

---

## 2. Evalation specifically for Example Problems

### Problem A_1: Validate rows

**Evaluation Description:**  
* The code should return True in the validate_rows method if all rows are valid. False otherwise
* The code should pass the first 5 automated tests (correctness)
* The agent should correctly, and promptly execute the test command corresponding to problem A.

**Bad example:**

Context (full git repo): https://github.com/Xavier-Schneider/CS846-CodeGen-Exercises

Prompt: Write Python code for the ‘validate_rows’ method in the SudokuPuzzleValidator class such that it returns ‘True’ if no row contains duplicate numbers and ‘False’ if at least one does.

Copilot:
```
def validate_rows(self):
        for row in self.grid:
            seen = set()
            for num in row:
                if num != "*":
                    if num in seen:
                        return False
                    seen.add(num)
        return True
```

Copilot: Ran terminal command: cd "c:\Users\xmanp\Desktop\LLMs for Software Engineering\CS846-CodeGen-Exercises"; python -m pytest tests/test_problem_A.py -v

Copilot: Ran terminal command: "C:/Users/xmanp/Desktop/LLMs for Software Engineering/CS846-CodeGen-Exercises/.venv/Scripts/python.exe" -m pytest tests/test_problem_A.py -v

Copilot: Ran terminal command: & "C:/Users/xmanp/Desktop/LLMs for Software Engineering/CS846-CodeGen-Exercises/.venv/Scripts/python.exe" -m pytest tests/test_problem_A.py -v

Copilot: Installing pytest in Python 3.12.3 (.venv)

Copilot: Ran terminal command: & "C:/Users/xmanp/Desktop/LLMs for Software Engineering/CS846-CodeGen-Exercises/.venv/Scripts/python.exe" -m unittest tests.test_problem_A

Copilot: ...

(you get the idea, Copilot continuously fails to run the test command)

**Good example:**

Context (full git repo): https://github.com/Xavier-Schneider/CS846-CodeGen-Exercises

Prompt: Write Python code for the ‘validate_rows’ method in the SudokuPuzzleValidator class such that it returns ‘True’ if no row contains duplicate numbers and ‘False’ if at least one does. When you are finished, please run tests using the test command ‘python3 -m unittest tests.test_problem_A’.

Copilot:
```
def validate_rows(self):
        for row in self.grid:
            seen = set()
            for num in row:
                if num != "*":
                    if num in seen:
                        return False
                    seen.add(num)
        return True
```

Copilot: Ran terminal command: python3 -m unittest tests.test_problem_A

Copilot: The `validate_rows` method has been successfully implemented. The test results show that all 5 tests for `validate_rows` passed (the dots in the output), while the other methods (`validate_cols` and `validate_boxes`) are not yet implemented, causing the remaining failures. The implementation correctly checks each row for duplicate non-empty values, returning `True` if no duplicates are found and `False` otherwise.

**Analysis:**

Both the “Bad” and “Good” examples produce identical code, but in the bad example, Copilot repeatedly attempts to call a test command (even though the prompt doesn’t mention tests) and continuously gets it wrong. In the “Good” example, Copilot has been given the command, so it executes the test command flawlessly one its first try (guideline 1).

---

### Problem A_2: Validate columns

**Evaluation Description:**  
* The code should return True in the validate_cols method if all columns are valid. False otherwise
* The code should pass the next 5 automated tests (correctness)
* The agent should correctly, and promptly execute the test command corresponding to problem A.

**Bad example:**

Context (full git repo): https://github.com/Xavier-Schneider/CS846-CodeGen-Exercises

Prompt: Write Python code for the ‘validate_cols’ method in the SudokuPuzzleValidator class such that it returns ‘True’ if no column contains duplicate numbers and ‘False’ if at least one does.

Copilot:
```
def validate_cols(self):
        for col in range(9):
            seen = set()
            for row in self.grid:
                num = row[col]
                if num != "*":
                    if num in seen:
                        return False
                    seen.add(num)
        return True
```
Copilot: Ran terminal command: cd "c:\Users\xmanp\Desktop\LLMs for Software Engineering\CS846-CodeGen-Exercises"; python -m pytest tests/test_problem_A.py -v

Copilot: Ran terminal command: "C:/Users/xmanp/Desktop/LLMs for Software Engineering/CS846-CodeGen-Exercises/.venv/Scripts/python.exe" -m pytest tests/test_problem_A.py -v

Copilot: Ran terminal command: & "C:/Users/xmanp/Desktop/LLMs for Software Engineering/CS846-CodeGen-Exercises/.venv/Scripts/python.exe" -m pytest tests/test_problem_A.py -v

Copilot: Installing pytest in Python 3.12.3 (.venv)

Copilot: Ran terminal command: & "C:/Users/xmanp/Desktop/LLMs for Software Engineering/CS846-CodeGen-Exercises/.venv/Scripts/python.exe" -m unittest tests.test_problem_A

Copilot: ...

(you get the idea, Copilot continuously fails to run the test command)

**Good example:**

Context (full git repo): https://github.com/Xavier-Schneider/CS846-CodeGen-Exercises

Prompt: Write Python code for the ‘validate_cols’ method in the SudokuPuzzleValidator class such that it returns ‘True’ if no column contains duplicate numbers and ‘False’ if at least one does. When you are finished, please run tests using the test command ‘python3 -m unittest tests.test_problem_A’.

Copilot:
```
def validate_cols(self):
        for col in range(9):
            seen = set()
            for row in range(9):
                num = self.grid[row][col]
                if num != "*":
                    if num in seen:
                        return False
                    seen.add(num)
        return True
```

Copilot: Ran terminal command: py -m unittest tests.test_problem_A The `validate_cols` method has been successfully implemented. It now correctly returns `True` if no column contains duplicate numbers (ignoring empty cells marked with "*") and `False` if at least one column does. The test results show that all tests for `validate_rows` and `validate_cols` are now passing (the dots in the output), with only the `validate_boxes` method still needing implementation. The 5 remaining failures are for the box validation tests.

**Analysis:**

Both the “Bad” and “Good” examples produce identical code, but in the bad example, Copilot repeatedly attempts to call a test command (even though the prompt doesn’t mention tests) and continuously gets it wrong. In the “Good” example, Copilot has been given the command, so it executes the test command flawlessly one its first try (guideline 1).

---

### Problem A_3: Validate sub-grids
Note: The previous issue with the test command applies to problems A_1 through C; however, from this point onward, we omit it from our "bad" examples, as the focus shifts to other guidelines and we don't want to be repetitive.

**Evaluation Description:**  
* The code should return True in the validate_boxes method if all sub-grids are valid. False otherwise
* The code should pass the last 5 automated tests (correctness)
* The agent should correctly, and promptly execute the test command corresponding to problem A.
* The code should be efficient
* The code should be readable

**Bad example:**

Context (full git repo): https://github.com/Xavier-Schneider/CS846-CodeGen-Exercises

Prompt: Write Python code for the ‘validate_boxes’ method in the SudokuPuzzleValidator class such that it returns ‘True’ if no 3x3 sub-grid contains duplicate numbers and ‘False’ if at least one does.

Copilot:
```
def validate_boxes(self):
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen = set()
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        num = self.grid[r][c]
                        if num != "*":
                            if num in seen:
                                return False
                            seen.add(num)
        return True
```

**Good example:**

Context (full git repo): https://github.com/Xavier-Schneider/CS846-CodeGen-Exercises

Write Python code for the ‘validate_boxes’ method in the SudokuPuzzleValidator class such that it returns ‘True’ if no 3x3 sub-grid contains duplicate numbers and ‘False’ if at least one does. When you are finished, please run tests using the test command ‘python3 -m unittest tests.test_problem_A’.
You must also meet the following 2 conditions:  
- Use only two nested loops in the method overall. 
- Divide each row and column by 3 to check which sub-grid you are in

Copilot:
```
def validate_boxes(self):
        boxes = [[set() for _ in range(3)] for _ in range(3)]
        for row in range(9):
            for col in range(9):
                num = self.grid[row][col]
                if num != "*":
                    box_row = row // 3
                    box_col = col // 3
                    if num in boxes[box_row][box_col]:
                        return False
                    boxes[box_row][box_col].add(num)
        return True
```

**Analysis:**

In the “Bad” example, Copilot produces code with four nested loops instead of two. If the prompter knows about this problem ahead of time, they can leverage that knowledge to get the model to output a solution using only two nested loops and the technique of dividing the row and column by 3 to perform a lookup to determine whether duplicate numbers exist in the same sub-grid (guideline 2). Additionally, because the model was explicitly told the test command, Copilot was able to execute it in one shot rather than making many failed attempts (guideline 1). 

---

### Problem B: Exam Score Analysis

**Evaluation Description:**  

* The code should use the provided python library
* The code should be short (no more than 30 lines)
* The code should pass the automated tests (correctness)

**Bad example:**

Context (full git repo): https://github.com/Xavier-Schneider/CS846-CodeGen-Exercises

Prompt: Solve problem B 

Copilot:
```
def problem_B(records):
    # Validate input
    if records is None:
        raise ValueError("Records cannot be None")
    records = list(records)  # Convert to list to allow multiple iterations
    if not records:
        raise ValueError("Records cannot be empty")
    
    # Validate each record
    required_keys = {"name", "score", "weight"}
    total_weight = 0.0
    weighted_sum = 0.0
    max_score = -1
    top_student = ""
    pass_count = 0
    grade_counts = {"A": 0, "B": 0, "C": 0, "F": 0}
    
    for record in records:
        if not isinstance(record, dict):
            raise ValueError(f"Each record must be a dictionary, got {type(record)}")
        if not required_keys.issubset(record.keys()):
            missing = required_keys - record.keys()
            raise ValueError(f"Record missing required keys: {missing}")
        
        name = record["name"]
        score = record["score"]
        weight = record["weight"]
        
        # Validate name
        if not isinstance(name, str) or not name.strip():
            raise ValueError(f"Name must be a non-empty string, got {name}")
        
        # Validate score
        if not isinstance(score, (int, float)) or score != score:  # Check for NaN
            raise ValueError(f"Score must be a valid number, got {score}")
        if not (0 <= score <= 100):
            raise ValueError(f"Score must be between 0 and 100, got {score}")
        
        # Validate weight
        if not isinstance(weight, (int, float)) or weight != weight:  # Check for NaN
            raise ValueError(f"Weight must be a valid number, got {weight}")
        if weight <= 0:
            raise ValueError(f"Weight must be positive, got {weight}")
        
        # Accumulate for weighted average
        weighted_sum += score * weight
        total_weight += weight
        
        # Check for top student
        if score > max_score:
            max_score = score
            top_student = name
        
        # Count passes
        if score >= 50:
            pass_count += 1
        
        # Grade distribution
        if score >= 70:
            grade_counts["A"] += 1
        elif score >= 60:
            grade_counts["B"] += 1
        elif score >= 50:
            grade_counts["C"] += 1
        else:
            grade_counts["F"] += 1
    
    # Compute statistics
    weighted_average = round(weighted_sum / total_weight, 2)
    pass_rate = round((pass_count / len(records)) * 100, 2)
    
    return {
        "count": len(records),
        "weighted_average": weighted_average,
        "top_student": top_student,
        "pass_rate": pass_rate,
        "grade_distribution": grade_counts
    }
```

**Good example:**

Context (full git repo): https://github.com/Xavier-Schneider/CS846-CodeGen-Exercises

Prompt: Solve problem B by making use of the examlib library under misc -> src -> library.py
run the command py -m unittest tests.test_problem_B to test your solution.

Copilot:
```
from problems.misc.src import library as examlib

def problem_B(records):
    # Validate records using examlib
    validated_records = examlib.validate_records(records)
    
    # Compute statistics using examlib functions
    count = len(validated_records)
    weighted_avg = examlib.weighted_average(records)
    top_student_name = examlib.top_student(records)
    pass_rate_pct = examlib.pass_rate(records)
    grade_dist = examlib.grade_distribution(records)
    
    # Return the summary dictionary
    return {
        "count": count,
        "weighted_average": weighted_avg,
        "top_student": top_student_name,
        "pass_rate": pass_rate_pct,
        "grade_distribution": grade_dist
    }
```

**Analysis:**

The good example makes use of guideline 3, i.e. it used the library that was in the repository. The bad example does not use the library, as a result it produced a giant block of duplicate code.

---

### Problem C: INI Config Anaylsis

**Evaluation Description:** 

* The code should have good readability
* The code should pass the automated tests (correctness)
* The code should have clear control flow


**Bad example:**

Context (full git repo): https://github.com/Xavier-Schneider/CS846-CodeGen-Exercises

Prompt: implement a INI Config Validator + Normalizer at problem_C.

Copilot:
```
def problem_C(text: str) -> str:
    lines = text.splitlines()
    sections = {}
    current_section = None
    seen_sections = set()
    
    for line_num, line in enumerate(lines, 1):
        # Strip whitespace
        stripped = line.strip()
        
        # Skip blank lines
        if not stripped:
            continue
        
        # Skip comments
        if stripped.startswith(';') or stripped.startswith('#'):
            continue
        
        # Remove trailing comments
        if ';' in stripped:
            stripped = stripped.split(';', 1)[0].strip()
        if '#' in stripped:
            stripped = stripped.split('#', 1)[0].strip()
        
        # Section header
        if stripped.startswith('[') and stripped.endswith(']'):
            section_name = stripped[1:-1]
            if not re.match(r'^[a-z0-9_]+$', section_name):
                raise ValueError(f"INVALID_SECTION at line {line_num}")
            if section_name in seen_sections:
                raise ValueError(f"DUPLICATE_SECTION at line {line_num}")
            seen_sections.add(section_name)
            current_section = section_name
            sections[current_section] = {}
            continue
        
        # Key-value pair
        if '=' in stripped:
            if current_section is None:
                raise ValueError(f"KEY_OUTSIDE_SECTION at line {line_num}")
            key, value = stripped.split('=', 1)
            key = key.strip()
            value = value.strip()
            if not re.match(r'^[a-z0-9_]+$', key):
                raise ValueError(f"INVALID_KEY at line {line_num}")
            if key in sections[current_section]:
                raise ValueError(f"DUPLICATE_KEY at line {line_num}")
            sections[current_section][key] = value
            continue
        
        # Invalid line
        raise ValueError(f"INVALID_LINE at line {line_num}")
    
    # Normalize: sort sections and keys
    sorted_sections = sorted(sections.keys())
    output_lines = []
    for i, section in enumerate(sorted_sections):
        if i > 0:
            output_lines.append('')
        output_lines.append(f'[{section}]')
        sorted_keys = sorted(sections[section].keys())
        for key in sorted_keys:
            output_lines.append(f'{key}={sections[section][key]}')
    
    return '\n'.join(output_lines)
```

**Good example:**

Context (full git repo): https://github.com/Xavier-Schneider/CS846-CodeGen-Exercises

Prompt:

Solve Problem C. Implement problem_C(text: str) -> str.

Input: text is a single newline-separated string representing a configuration file containing section headers [section] and key–value lines key=value, possibly with blank lines and comments starting with # or ;.

Output: return a normalized configuration string in which sections are sorted alphabetically and keys are sorted within each section, formatted as [section] followed by its key=value lines, with exactly one blank line between sections, and the returned string must end with a final newline character (\n).

There should be two helper methods, _parse_and_validate as well as normalize.

run the command py -m unittest tests.test_problem_C to test your solution.


Copilot:
```
import re

def _parse_and_validate(text: str) -> dict:
    sections = {}
    current_section = None
    lines = text.splitlines()
    for line_num, line in enumerate(lines, 1):
        line = line.strip()
        if not line:
            continue
        if line.startswith('#') or line.startswith(';'):
            continue
        # remove trailing comments
        if '#' in line:
            line = line.split('#', 1)[0].strip()
        elif ';' in line:
            line = line.split(';', 1)[0].strip()
        if not line:
            continue
        if line.startswith('[') and line.endswith(']'):
            section = line[1:-1].strip()
            if not re.match(r'^[a-z0-9_]+$', section):
                raise ValueError(f"INVALID_SECTION at line {line_num}")
            if section in sections:
                raise ValueError(f"DUPLICATE_SECTION at line {line_num}")
            current_section = section
            sections[section] = {}
        else:
            if '=' not in line:
                raise ValueError(f"INVALID_LINE at line {line_num}")
            key, value = line.split('=', 1)
            key = key.strip()
            value = value.strip()
            if not re.match(r'^[a-z0-9_]+$', key):
                raise ValueError(f"INVALID_KEY at line {line_num}")
            if current_section is None:
                raise ValueError(f"KEY_OUTSIDE_SECTION at line {line_num}")
            if key in sections[current_section]:
                raise ValueError(f"DUPLICATE_KEY at line {line_num}")
            sections[current_section][key] = value
    return sections

def normalize(sections: dict) -> str:
    sorted_sections = sorted(sections.keys())
    result = []
    for sec in sorted_sections:
        result.append(f"[{sec}]")
        sorted_keys = sorted(sections[sec].keys())
        for key in sorted_keys:
            result.append(f"{key}={sections[sec][key]}")
        if sec != sorted_sections[-1]:
            result.append("")
    return '\n'.join(result) + '\n'

def problem_C(text: str) -> str:
    parsed = _parse_and_validate(text)
    return normalize(parsed)
```

**Analysis:**

The 'bad' example fails to pass the test cases, since the output format is underspecified (output requires a trailing '\n'). In the bad example, preprocessing, validation, and rendering are mixed inside a single loop, making the control flow harder to follow and maintain. In contrast, the good example enforces a clear input–process–output structure, making use of helpers _parse_and_validate and normalize (guideline 2). It also specifies the i.o. format, so the code passes the test case (guideline 4).

### Problem D: Building a personal website

Note: In the following examples Copilot is instructed to create a website. Rather than include all Copilot output, we simply document the resulting website as a picture since the Copilot logs/generated code is overly long and complex. We find that an image is sufficient to demonstrate the results.

**Evaluation Description:**

* The website is compelling (looks good)
* The website is functional (it has the elements of a graduate student website - publications, socials, etc.)

**Bad Example:**

Context: (No context given - empty folder)

Prompt: build a website for a graduate student named Xavier Schneider who goes to the University of Waterloo. The website needs to be hosted on a server. Include an image of a rabbit on the website.

Copilot: ![Bad example](bad.png)

**Good Example:**

Context: (No context given - empty folder)

Prompt1: Create a simple python app that serves a static webpage using flask. Manage your dependencies in a virtual environment.

Prompt2: Use the html/javascript from this website as a base for my own. https://kuwingfung.github.io/

Prompt3: Change it so that it's about Xavier Schneider, and a bunch of made up publications.

Prompt4: Use a picture of a rabbit instead of the human.

Copilot: ![Good example](good.png)

**Analysis:**

The good example makes use of guidelines 3 and 5. As a result, the final website is much more compelling visually and in terms of content. This is because a solid architectural foundation was established with guideline 3 (use flask), and the user iterated with Copilot to create the website, rather than creating it in a single prompt (guideline 5).

---

These Evalutations were created in collaboration with GPT 5.2
