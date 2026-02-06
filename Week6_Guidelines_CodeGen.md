# Week 6 Guidelines: CodeGen / Planning

**Authors:** Xavier Schneider, Greg French, Max Ku  
**Readings Assigned:**  
- Leveraging Print Debugging To Improve Code Generation In Large Language Models  
- LLM-Based Test-Driven Interactive Code Generation: User Study and Empirical Evaluation
- Self-Collaboration Code Generation via ChatGPT
- SOEN-101: Code Generation by Emulating Software Process Models Using LLM Agents
- Self-Organized Agents: A LLM Multi-Agent Framework
- Empowering Agile-Based Generative Software Development through Human-AI Teamwork
- Guidelines to Prompt Large Language Models for Code Generation: An Empirical Characterization
- How AI-assisted coding will change software engineering: hard truths
- OpenSpec: A Spec-Driven Workflow for AI Coding Assistants

## 1. Guidelines

### Guideline 1: Make requirements explicit in terms of needed packages or libraries, and explain what to use them for.
**Description:**  
Clearly specify all required libraries, frameworks, tools, and dependencies in the prompt, and explain what each one should be used for. Instead of only naming a package, describe its role in the solution.

**Reasoning:**  
When requirements are vague, LLMs may choose the wrong tools, omit imports, or implement inefficient solutions. The study found that explicitly naming dependencies helps generate more accurate and compatible code by reducing ambiguity and guiding the model toward the intended implementation approach.

**Example:**  
"Use NumPy for numerical array operations" or "use pandas for tabular data manipulation".

---

### Guideline 2:  Specify pre-conditions (e.g., a data structure provided as input must be non-empty).
(Repeat the same structure for each guideline.)

---

### Guideline N: [Short, Actionable Title]
(Repeat the same structure for each guideline.)

### Guideline 5: Break Large Requests into Steps
(Repeat the same structure for each guideline.)

### Guideline 6: Use Examples
(Repeat the same structure for each guideline.)

---

## 2. Guideline to use in each problem

Problem A: Guideline 1 (hint: look under problems -> misc -> src -> library.py)

## 2. References

[1]  
[2] 

---