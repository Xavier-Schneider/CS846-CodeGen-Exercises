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

### Guideline 1: Make requirements explicit in terms of needed packages or libraries, and explain what to use them for.
**Description:**  
Clearly specify all required libraries, frameworks, tools, and dependencies in the prompt, and explain what each one should be used for. Instead of only naming a package, describe its role in the solution.

**Reasoning:**  
When requirements are vague, LLMs may choose the wrong tools, omit imports, or implement inefficient solutions. The study found that explicitly naming dependencies helps generate more accurate and compatible code by reducing ambiguity and guiding the model toward the intended implementation approach.

**Example:**  
"Use NumPy for numerical array operations" or "use pandas for tabular data manipulation".

---

### Guideline 2:  Always clearly specify the exact input type and exact output format.
**Description:**
Always explicitly state what the function takes as input and what it must return, including the exact data type and representation. For code-generation tasks ambiguity about input/output format may leads to incorrect implementations even if the internal logic is mostly right.

**Reasoning:**  
Without explicit input and output, the LLM may perform any unexpected behavior such as return a dict instead of a string, print output instead of returning, or normalize differently than tests expect.


**Example:**  
Instead of saying: 

"Write a function to parse an INI file."

Say:

"Complete problem_C(text) where text is a string containing INI config.
The function must return a normalized INI string with sorted sections/keys and a final newline.
Raise ValueError on invalid input."

---

### Guideline 3:  Specify Tool and Workflow Execution Mechanics
**Description:**  
Be specific, not just about whether a tool in your workflow should be run, but also about the specific command to run it. If you want the LLM to run a unit test, don’t just tell it to run tests; give it the exact command it should use to run the test.

**Reasoning:**  
If you don’t specify how the LLM should execute a tool, it may end up spinning its wheels, making multiple attempts to get it right. It may even give up if, after many attempts, it can’t guess the correct command.

**Example:**  
Instead of saying at the end of your prompt:  

“When you are finished, please run tests.”

Say:

“When you are finished, please run tests using the test command ‘python3 -m unittest tests.test_problem_B’”

---

### Guideline N: [Short, Actionable Title]
(Repeat the same structure for each guideline.)


### Guideline 5: Break large requests into steps
**Description:**
When the task is large or multi-part, explicitly decompose it into a sequence of smaller steps (or milestones) the model should follow. Each step should have a clear goal and a concrete output (e.g., “define interfaces,” “write parsing function,” “add tests,” “run example”). If relevant, specify an order of operations (plan → implement → validate) and what “done” looks like for each step.

**Reasoning:**
LLMs are more reliable when they can focus on one objective at a time. Step-by-step decomposition reduces omissions (forgotten edge cases, missing imports, unhandled error paths), lowers the chance of inconsistent design decisions, and improves overall coherence—especially for longer code generation tasks. It also makes it easier to verify correctness at each stage and to iterate when requirements change.

**Example:**
“Build a log-processing tool in four steps: (1) define the input format and output schema, (2) implement the parser and normalization logic, (3) add aggregation + reporting functions, (4) write unit tests and provide a small demo run with sample logs.”


### Guideline 6: Use targeted examples from the domain
**Description:**
Include 1–3 small, representative examples drawn from the target domain (inputs, outputs, edge cases, or typical workflows). Prefer examples that mirror real-world patterns the system will encounter, and make them specific enough to constrain interpretation (e.g., include realistic field names, units, timestamps, or error formats). If applicable, include both a “happy path” and a tricky edge case.

**Reasoning:**
Domain-targeted examples anchor the model’s interpretation of requirements and reduce ambiguity about formats, conventions, and correctness criteria. They act as “implicit tests,” guiding the model toward the expected behavior and preventing generic solutions that don’t match real data or real constraints. This is especially helpful in specialized domains where small formatting differences (units, time zones, IDs, naming conventions) can break the solution.

**Example:**
“If you’re generating code for financial transactions, include sample rows like: {"id":"txn_001","amount":-12.34,"currency":"USD","timestamp":"2026-02-05T14:03:22Z","category":"fees"} and an edge case like a reversal/refund transaction, so the model handles negative amounts and status changes correctly.”

---

## 2. Guideline to use in each problem

Problem A: Guideline 1 (hint: look under problems -> misc -> src -> library.py)


Now it's time to test what you've learned!

Problem D: Guideline 1 (hint: flask is a simple python module for deploying websites), Guideline 6 (here are some great graduate student websites... https://kuwingfung.github.io/, https://benjaminschneider.ca/ and Copilot can access the internet, so... (you have permission to use them as examples)), Guideline 5 (Don't ask copilot to do the previous 2 steps at once!) 

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