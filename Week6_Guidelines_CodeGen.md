# Week 6 Guidelines: CodeGen / Planning

**Authors:** Xavier Schneider, Greg French, Max Ku  
**Readings Assigned:**  
- Leveraging Print Debugging To Improve Code Generation In Large Language Models \[1\]  
- LLM-Based Test-Driven Interactive Code Generation: User Study and Empirical Evaluation \[2\]  
- Self-Collaboration Code Generation via ChatGPT \[3\]  
- SOEN-101: Code Generation by Emulating Software Process Models Using LLM Agents \[4\]  
- Self-Organized Agents: A LLM Multi-Agent Framework \[5\]  
- Empowering Agile-Based Generative Software Development through Human-AI Teamwork \[6\]  
- Guidelines to Prompt Large Language Models for Code Generation: An Empirical Characterization \[7\]  
- How AI-assisted coding will change software engineering: hard truths \[8\]  
- OpenSpec: A Spec-Driven Workflow for AI Coding Assistants \[9\]  

## 1. Guidelines For Code Generation / Planning

### Guideline 1: Specify any project specific Tool and Workflow Execution Mechanics
**Description:**  
Be specific, not just about whether a tool in your workflow should be run, but also about the specific command to run it. If you want the LLM to run a unit test, don’t just tell it to run tests; give it the exact command it should use to run the test \[8\].

**Reasoning:**  
If you don’t specify how the LLM should use a tool, it may end up spinning its wheels, making multiple attempts to get it right. It may even give up if, after many attempts, it can’t guess the correct command.

**Good Example:**
"From the repo root, run the backend unit tests with:
poetry run pytest tests/unit -q
If any tests fail, paste the full failure output and then fix the code so the suite passes.
After that, run the frontend tests with:
pnpm -C web test -- --runInBand."

**Bad Example:**
"Run the tests to make sure everything still works, and fix anything that fails."

---

### Guideline 2: Add algorithmic details when logic is complex 
**Description:**  
If you know additional algorithmic information about a specific problem, make sure to include that information in your prompt. This will help guide the code generation to a cleaner and/or more optimal solution \[7\].

**Reasoning:**  
When a problem admits multiple valid solutions, an LLM will often default to the simplest or most general approach unless guided otherwise. This can result in code that is correct but not optimal in terms of time complexity, structure, or clarity. By specifying relevant algorithmic details—such as the desired technique, performance expectations, and preferred control flow—you reduce ambiguity and communicate which design qualities matter. This helps the model choose an approach that not only meets efficiency goals but also produces cleaner logic, more predictable control flow, and improved readability, making the resulting code easier to follow, maintain, and verify.

**Good Example:**  
If as part of your algorithm you need to search for a number in a sorted list, the LLM may write a linear-time algorithm, assuming that the list size is small, or unordered, and because it’s simpler to write. Specifically, telling it to write a binary search algorithm that runs in O(log(n)) time helps steer the LLM toward producing more efficient software.

**Bad Example:**
Write a function to search for a number in the list.

---

### Guideline 3: Specify required external libraries/packages and their purpose.
**Description:**  
When you want Copilot to generate code that relies on non-standard libraries, explicitly specify which packages to use and what each is for, so the generated code imports and uses them correctly \[7\]. 

**Reasoning:**  
When requirements are vague, LLMs may omit imports, or implement inefficient solutions. \[7\] found that explicitly naming dependencies helps generate more accurate and compatible code by reducing ambiguity and guiding the model toward the intended implementation approach.

**Good Example:**
"Use NumPy for numerical array operations" or "use pandas for tabular data manipulation".

**Bad Example:**
"Write code that computes the sum of each column in a csv."

---

### Guideline 4:  Specify the input type and output format.
**Description:**
Explicitly specify the function's input types, output type, and the exact output format and constraints, including representation details such as value ranges, structure, and whether the function should return or print the result. For code-generation tasks, ambiguity about these aspects can lead to implementations that are logically correct but incompatible with the expected interface or tests \[7\].

**Reasoning:**  
Large language models often infer missing interface details. If the prompt only loosely describes the task, the model may return a different data structure (e.g., a dictionary instead of a float), print the result instead of returning it, or produce outputs outside the expected value range. Even when the algorithm is correct, these mismatches can cause downstream failures such as broken tests, invalid API responses, or inconsistent data formats. Specifying the function signature, output structure, and value constraints ensures the generated code aligns with the expected contract.

**Good Example:**
"Write a Python function average(numbers: list[float]) -> float" that returns the arithmetic mean of the input list.

The function must return a float (do not print the result).
If the list is empty, return 0.0.
The output must be a single float value."

**Bad Example:**
"Write a function that processes a list of numbers and gives the result."

**Update**
This guideline was updated to address feedback that specifying only the input and output types is insufficient. The revised version now also requires explicitly defining the output representation, behavioral contract (return vs. print), and value constraints (e.g., ranges or edge-case handling). These additions help prevent cases where the generated code produces structurally correct but incompatible outputs, such as returning dictionaries instead of scalar values or producing results outside the expected range.

> The updated guideline addressing issues identified in the feedback from groups 2, 3, 6.

---

### Guideline 5: Work in Short, Iterative Cycles

**Description:**
Break the interaction into small, repeated steps: generate -> review -> refine -> regenerate, rather than trying to build an entire system in a single prompt \[8\]\[9\].

**Reasoning:**
Frequent, incremental updates improve accuracy and alignment. Short feedback loops help surface issues earlier, make corrections easier, and give you more control over how the solution evolves.

**Good Example:**
Iteration 1: Propose the data model (entities, fields, relationships).
Iteration 2: Draft the API endpoints + request/response schemas.
Iteration 3: Implement one endpoint end-to-end.
Iteration 4: Add integration tests and handle edge cases.

**Bad Example:**
In one step, generate the full architecture, implementation, tests, documentation, and optimizations for the entire system.

---

## 2. Guideline to use in each problem

Problem A_1:
* Guideline 1 (hint: provide the command that runs the test to Copilot 'python3 -m unittest tests.test_problem_A'") 

Problem A_2:
* Guideline 1 (hint: same as above)

Problem A_3:
* Guideline 1 (hint: same as above)
* Guideline 2 (hint: - Use only two nested loops in the method overall. - Divide each row and column by 3 to check which sub-grid you are in)

Problem B:
* Guideline 1 (hint: same as above)
* Guideline 3 (hint: look under problems -> misc -> src -> library.py)

Problem C:
* Guideline 1 (hint: same as above)
* Guideline 4 (hint: output format requires a trailing '\n')
* Guideline 2 (hint: INI Config Validator + Normalizer can (and should!) be split into two helper functions)

Problem D:
* Guideline 3 (hint: flask is a simple python module for deploying websites), (hint: here are some great graduate student websites: https://kuwingfung.github.io/, https://benjaminschneider.ca/ and Copilot can access the internet, so... you have permission to give them to Copilot as examples)
* Guideline 5 (hint: don't ask Copilot to do the previous 2 steps at once!)

## 2. References

\[1\] Hu, X., et al. "Leveraging Print Debugging to Improve Code Generation in LLMs"\
\[2\] Fakhoury, S., et al. "LLM-Based Test-Driven Interactive Code Generation: User Study and Empirical Evaluation" DOI\
\[3\] Dong, Y., et al. "Self-Collaboration Code Generation via ChatGPT" ACM\
\[4\] Lin, F., et al. "SOEN-101: Code Generation by Emulating Software Process Models Using Large Language Model Agents" arXiv\
\[5\] Ishibashi, Y., & Nishimura, Y. "Self-Organized Agents: A LLM Multi-Agent Framework toward Ultra Large-Scale Code Generation and Optimization" arXiv\
\[6\] Zhang, S., et al. "Empowering Agile-Based Generative Software Development through Human-AI Teamwork" ACM\
\[7\] Midolo, A., et al. "Guidelines to Prompt Large Language Models for Code Generation: An Empirical Characterization" arXiv\
\[8\] Orosz, G., & Osmani, A. "How AI-assisted coding will change software engineering: hard truths" Pragmatic Engineer Blog\
\[9\] Code Coup "OpenSpec: A Spec-Driven Workflow for AI Coding Assistants (No API Keys Needed)" Medium

---

These Guidelines were created in collaboration with GPT 5.2