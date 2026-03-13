# Week 6 Evaluation: CodeGen / Planning

**Authors:** Xavier Schneider, Greg French, Max Ku 


## 1. Evaluation Criteria

* The code should pass the automated tests (correctness)
* The code should be readable
* The code should be well-architected (modular, extensible, etc.)

---

## 2. Evalation specifically for Example Problems

### Problem A: Exam Score Analysis

**Evaluation Description:**  

* The code should use the provided python library
* The code should be short (no more than 30 lines)
* The code should pass the automated tests (correctness)

**Bad example**

Context (full git repo): https://github.com/Xavier-Schneider/CS846-CodeGen-Exercises

Prompt: Solve problem A 

```
def problem_A(records):
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

**Good example**

Context (full git repo): https://github.com/Xavier-Schneider/CS846-CodeGen-Exercises

Prompt: Solve problem A by making use of the examlib library under misc -> src -> library.py

```
from problems.misc.src import library as examlib

def problem_A(records):
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

**Analysis**
The good example makes use of guideline 1, i.e. it used the provided library. The bad example does not use the library, as a result it produced a giant block of duplicate code.

---

### Problem B_1: Validate rows

**Evaluation Description:**  
* The code should return True in the validate_rows method if all rows are valid. False otherwise
* The code should pass the first 5 automated tests (correctness)

**Bad example**

Prompt: Write Python code for the ‘validate_rows’ method in the SudokuPuzzleValidator class such that it returns ‘True’ if no row contains duplicate numbers and ‘False’ if at least one does.

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

**Good example**

Prompt: Write Python code for the ‘validate_rows’ method in the SudokuPuzzleValidator class such that it returns ‘True’ if no row contains duplicate numbers and ‘False’ if at least one does. When you are finished, please run tests using the test command ‘python3 -m unittest tests.test_problem_B’.

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

**Analysis**
Both the “Bad” and “Good” examples produce identical code, but in the chat window, it repeatedly attempts to call a test command (even though the prompt doesn’t mention tests) until it gets it right. With the “Good” example, Grok executes the test command flawlessly the first time.

---

### Problem B_2: Validate columns

**Evaluation Description:**  
* The code should return True in the validate_cols method if all columns are valid. False otherwise
* The code should pass the next 5 automated tests (correctness)

**Bad example**

Prompt: Write Python code for the ‘validate_cols’ method in the SudokuPuzzleValidator class such that it returns ‘True’ if no column contains duplicate numbers and ‘False’ if at least one does.

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

**Good example**

Prompt: Write Python code for the ‘validate_cols’ method in the SudokuPuzzleValidator class such that it returns ‘True’ if no column contains duplicate numbers and ‘False’ if at least one does. When you are finished, please run tests using the test command ‘python3 -m unittest tests.test_problem_B’.

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

**Analysis**
Both the “Bad” and “Good” examples produce very similar code, but in the chat window, Grok repeatedly attempts to run a test command (even though the prompt doesn’t mention tests) until it succeeds. With the “Good” example, Grok executes the test command flawlessly the first time.

---

### Problem B_3: Validate sub-grids

**Evaluation Description:**  
* The code should return True in the validate_boxes method if all sub-grids are valid. False otherwise
* The code should pass the last 5 automated tests (correctness)

**Bad example**

Prompt: Write Python code for the ‘validate_boxes’ method in the SudokuPuzzleValidator class such that it returns ‘True’ if no 3x3 sub-grid contains duplicate numbers and ‘False’ if at least one does.

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

**Good example**

Write Python code for the ‘validate_boxes’ method in the SudokuPuzzleValidator class such that it returns ‘True’ if no 3x3 sub-grid contains duplicate numbers and ‘False’ if at least one does. When you are finished, please run tests using the test command ‘python3 -m unittest tests.test_problem_B’.
You must also meet the following 2 conditions:  
- Use only two nested loops in the method overall. 
- Divide each row and column by 3 to check which sub-grid you are in

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

**Analysis**
In the “Bad” example, Grok produces code with four nested loops instead of two. If the prompter knows about this problem ahead of time, they can leverage that knowledge to get the model to output a solution using only two nested loops and the technique of dividing the row and column by 3 to perform a lookup to determine whether duplicate numbers exist in the same sub-grid. Additionally, because the model was explicitly told the test command, Grok was able to execute it in one shot rather than making many failed attempts. 

---

### Problem C: INI Config Anaylsis

**Evaluation Description:** 

* The code should have good readability
* The code should pass the automated tests (correctness)
* The code should have clear control flow


**Bad example**
Prompt:
```
implement a INI Config Validator + Normalizer at problem_C.
```

Code:
```python
import re

def problem_C(text: str) -> str:
    lines = text.splitlines()
    sections = {}
    current_section = None
    line_num = 0
    
    for line in lines:
        line_num += 1
        # Remove trailing comments
        line = re.split(r'[;#]', line)[0].strip()
        if not line:
            continue  # blank line or comment
        
        if line.startswith('[') and line.endswith(']'):
            section_name = line[1:-1]
            if not re.match(r'^[a-z_][a-z0-9_]*$', section_name):
                raise ValueError(f"INVALID_SECTION at line {line_num}")
            if section_name in sections:
                raise ValueError(f"DUPLICATE_SECTION at line {line_num}")
            sections[section_name] = {}
            current_section = section_name
        elif '=' in line:
            if current_section is None:
                raise ValueError(f"KEY_OUTSIDE_SECTION at line {line_num}")
            key, value = line.split('=', 1)
            key = key.strip()
            value = value.strip()
            if not re.match(r'^[a-z_][a-z0-9_]*$', key):
                raise ValueError(f"INVALID_KEY at line {line_num}")
            if key in sections[current_section]:
                raise ValueError(f"DUPLICATE_KEY at line {line_num}")
            sections[current_section][key] = value
        else:
            raise ValueError(f"INVALID_LINE at line {line_num}")
    
    # Now normalize
    output_lines = []
    sorted_sections = sorted(sections.keys())
    for i, section in enumerate(sorted_sections):
        output_lines.append(f"[{section}]")
        sorted_keys = sorted(sections[section].keys())
        for key in sorted_keys:
            output_lines.append(f"{key}={sections[section][key]}")
        if i < len(sorted_sections) - 1:
            output_lines.append("")
    output_lines.append("")
    return "\n".join(output_lines)
```

**Good example**

Prompt:
```
Complete problem_C(text) in Python (stdlib only, do not use configparser).
text is a raw INI string. Return a normalized INI string: sections sorted, keys sorted, exactly one blank line between sections, and a final newline.

Before coding, write a 3-step plan: preprocessing -> parsing/validation -> rendering.

Implement using helpers (define them in the same file):

_clean_line(raw_line: str) -> str (remove comments starting at first ; or #, then strip whitespace)

_parse_section(line: str, line_no: int) -> str (validate section regex, raise ValueError)

_parse_kv(line: str, line_no: int) -> tuple[str, str] (split on first =, validate key regex, trim value)

_render(sections: dict[str, dict[str, str]]) -> str

Classification rule: after cleaning, each non-empty line must be either a section header or a key=value line; otherwise raise INVALID_LINE.

Error format: raise ValueError with message "{CODE} line {line_no}: {details}", where CODE ∈ {KEY_OUTSIDE_SECTION, INVALID_SECTION, DUPLICATE_SECTION, INVALID_KEY, DUPLICATE_KEY, INVALID_LINE}.

Keep helpers short and readable; avoid nested conditionals when possible.
```

Code:
```python
import re

def problem_C(text: str) -> str:
    # 3-step plan:
    # 1. Preprocessing: Split text into lines, clean each line (remove comments and strip), filter empty lines.
    # 2. Parsing/Validation: Parse sections and key-value pairs, validate formats, check for duplicates and structure.
    # 3. Rendering: Sort sections and keys, render normalized INI string with blank lines between sections and final newline.
    
    lines = text.splitlines()
    cleaned_lines = [_clean_line(line) for line in lines]
    sections = {}
    current_section = None
    line_no = 0
    
    for cleaned in cleaned_lines:
        line_no += 1
        if not cleaned:
            continue
        if cleaned.startswith('[') and cleaned.endswith(']'):
            section_name = _parse_section(cleaned, line_no)
            if section_name in sections:
                raise ValueError(f"DUPLICATE_SECTION line {line_no}: {cleaned}")
            sections[section_name] = {}
            current_section = section_name
        elif '=' in cleaned:
            if current_section is None:
                raise ValueError(f"KEY_OUTSIDE_SECTION line {line_no}: {cleaned}")
            key, value = _parse_kv(cleaned, line_no)
            if key in sections[current_section]:
                raise ValueError(f"DUPLICATE_KEY line {line_no}: {cleaned}")
            sections[current_section][key] = value
        else:
            raise ValueError(f"INVALID_LINE line {line_no}: {cleaned}")
    
    return _render(sections)

def _clean_line(raw_line: str) -> str:
    # Remove comments starting at first ; or #
    line = re.split(r'[;#]', raw_line)[0]
    return line.strip()

def _parse_section(line: str, line_no: int) -> str:
    if not (line.startswith('[') and line.endswith(']')):
        raise ValueError(f"INVALID_SECTION line {line_no}: {line}")
    section_name = line[1:-1]
    if not re.match(r'^[a-z_][a-z0-9_]*$', section_name):
        raise ValueError(f"INVALID_SECTION line {line_no}: {line}")
    return section_name

def _parse_kv(line: str, line_no: int) -> tuple[str, str]:
    if '=' not in line:
        raise ValueError(f"INVALID_LINE line {line_no}: {line}")
    key, value = line.split('=', 1)
    key = key.strip()
    value = value.strip()
    if not re.match(r'^[a-z_][a-z0-9_]*$', key):
        raise ValueError(f"INVALID_KEY line {line_no}: {line}")
    return key, value

def _render(sections: dict[str, dict[str, str]]) -> str:
    output_lines = []
    sorted_sections = sorted(sections.keys())
    for i, section in enumerate(sorted_sections):
        output_lines.append(f"[{section}]")
        sorted_keys = sorted(sections[section].keys())
        for key in sorted_keys:
            output_lines.append(f"{key}={sections[section][key]}")
        if i < len(sorted_sections) - 1:
            output_lines.append("")
    output_lines.append("")
    return "\n".join(output_lines)
```

**Analysis**

After applying the guideline, the code becomes more readable and interpretable without changing the core logic. In the bad example, preprocessing, validation, and rendering are mixed inside a single loop, making the control flow harder to follow and maintain. In contrast, the good example enforces a clear input–process–output structure: problem_C reads as a high-level pipeline, while helper functions isolate specific responsibilities such as cleaning lines, parsing sections, and rendering output. This separation reduces nesting, clarifies intent, and makes both correctness and errors easier to reason about.

### Problem D: Building a personal website

**Evaluation Description:**

* The website is compelling (looks good)
* The website is functional (it has the elements of a graduate student website - publications, socials, etc.)

**Bad Example**

Context: (No context given - empty folder)

Prompt: build a website for a graduate student named xavier schneider who goes to the university of waterloo. The website needs to be hosted on a server. Include an image of a rabbit on the website.

Copilot: ... (output too large to include, see end result)

result:

![Bad example](bad.png)

**Good Example**

Context: (No context given - empty folder)

Prompt: Create a simple python app that serves a static webpage using flask. Manage your dependencies in a virtual environment.

Copilot: ... (output too large to include, see end result)

Prompt: Use the html/javascript from this website as a base for my own. https://kuwingfung.github.io/

Copilot: ... (output too large to include, see end result)

Prompt: Change it so that it's about Xavier Schneider, and a bunch of made up publications.

Copilot: ... (output too large to include, see end result)

Prompt: Use a picture of a rabbit instead of the human.

result:

![Good example](good.png)

**Analysis**
The good example makes use of guidelines 1, 5 and 6. As a result, the final website is much more compelling visually and in terms of content. (note: in this particular example, we use other websites as examples - examples like this must be used with permission, or else simply draw inspiration from these websites.)

---

## 3. References

[1]  
[2] 

---
