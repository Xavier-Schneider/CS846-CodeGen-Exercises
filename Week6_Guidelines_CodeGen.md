# Week 6 Guidelines (Updated): CodeGen / Planning

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

**Update Preamble**
In general, the feedback indicates that our existing guidelines are well justified. Rather than revealing broad failures in those guidelines, the feedback highlights a number of edge cases where our existing guidelines are valid, but are not sufficient on their own to solve the problem. In response, we are introducing two new guidelines (6 and 7) to address those cases, as well as updates to guidelines 1, 3 and 4. We validate our new guidelines on an a new problem (problem E).

## 1. Guidelines For Code Generation / Planning

### Guideline 1: Specify any project specific tool and workflow execution mechanics
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

### Guideline 1 (Addendum): Specify any project-specific tool and workflow execution mechanics in the instructions.md file
**Description:**  
Be specific about the tool in your workflow that should be run. If you want the LLM to run a unit test, don’t just tell it to run tests; specify the exact tool to use (e.g., pytest). Place this instruction in an ‘instructions.md’ file within your repo so that everyone on your software development team can make use of it.

**Reasoning:**  
Telling an LLM the exact tool to use, but not necessarily the exact command to use, and placing this information in an ‘instructions.md’ file enables portability with the command, so that, for example, the LLM can run tests on a user's machine without the user needing to know the exact test command ahead of time and give this information to the LLM explicitly.

**Good Example:**
"After every code change, run the backend unit tests using pytest from the repo root.
If any tests fail, paste the full failure output and then fix the code so the suite passes.
After that, run the frontend tests using Jest."

**Bad Example:**
"Run the tests to make sure everything still works, and fix anything that fails."

**Update**  
This guideline was updated to address feedback from Group 4, which noted that it doesn't offer portability and only works on a machine where the user knows the exact command to run in advance. If you tell the command to run the test with ‘python3’, but the user instead uses ‘python’ to run Python commands, the command will fail. With this updated guideline, we can place a more general prompt within an ‘instructions.md’ file, and share it with the entire software team working on the project, so that it will work across whatever machine the developer is working on. The one downside of this generality is that an LLM may still have to try running multiple commands until it gets the test command right, and that is why you should use the original guideline if portability is not an issue. If you do need portability, however, this guideline offers a great alternative to the original.

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

Include the following if known and relevant:
1. Package name and explicit version constraint (or minimum version).
2. Intended purpose and which APIs/features to use.
3. Classification: runtime, test, or dev dependency.
4. Platform/hardware constraints (OS, CPU/GPU).
5. Expected data scale and memory/performance limits.
6. Preferred alternatives and a rule for when to switch.
7. Install command(s) and how to declare the dependency (requirements.txt / pyproject / environment.yml).
8. A minimal usage snippet or expected function signature.

If multiple libraries are acceptable, state the preferred one and a simple threshold (e.g., file size) for switching to an alternative.

**Reasoning:**  
When requirements are vague, LLMs may omit imports, or implement inefficient solutions. \[7\] found that explicitly naming dependencies helps generate more accurate and compatible code by reducing ambiguity and guiding the model toward the intended implementation approach. By providing detailed library specifications, LLMs generate code that accounts for scale, compatibility, and alternatives, avoiding failures like OOM on large data and ensuring production-ready outputs.

**Good Example:**
"Use NumPy for numerical array operations" or "use pandas for tabular data manipulation".

**Bad Example:**
"Write code that computes the sum of each column in a csv."

**Update:**
Feedback pointed out that the previous description of this guideline was overly broad. In many cases, the LLM requires more information than simply "use this library to do x". Instead, specifying what library functions should be used, what version should be used, and performance expectations may be necessary. 

> This guideline update was recommended by group 8


---

### Guideline 4 (Updated):  Specify the input type and output format.
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

> The updated guideline addresses issues identified in the feedback from groups 2, 3, 6.

---

### Guideline 5: Work in short, iterative cycles

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

### Guideline 6 (New): Plan first, implement later
**Description:**  
Before making changes, explicitly ask the LLM to inspect the relevant code, summarize what it intends to do, and identify the files, functions, or components it expects to touch. Require it to present a short implementation plan first, then proceed with the edits only after that plan is established.

**Reasoning:**  
Without an explicit planning step, the LLM may jump into editing too early, make unnecessary changes, or miss dependencies between parts of the codebase. A brief plan improves accuracy, makes the workflow easier to review, and reduces the chance of rework caused by misunderstandings.

**Good Example:**  
"Before writing any code, inspect the authentication flow and give me a short plan.  
Your plan should include:  
1. Which files you expect to modify  
2. What each change will do  
3. Any assumptions or risks  
Once you’ve written the plan, implement it step by step. After coding, summarize exactly what changed."

**Bad Example:**  
"Add the new authentication behavior and update whatever is needed."

**Update**
This guideline was added to address a common thread of criticism: our existing guidelines target the generation phase of LLM prompting, they do not address the pre-generation phase. By planning with the LLM first, we can expose false assumptions before they become problems.

> This guideline was recommended by group 4

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

Problem E:
* Guideline 6

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