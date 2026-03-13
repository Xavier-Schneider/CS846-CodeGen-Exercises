# Week 6 Raw Guidelines: CodeGen / Planning

**Authors:** Xavier Schneider, Greg French, Max Ku  
**Readings:**   
- [Additional sources explored beyond assigned readings]

## 1. Guidelines from Readings

### Guideline 1 \[1\]: Prompt the Model to Instrument Code, Not Just Explain It

**Description:**\
When debugging, explicitly instruct the LLM to insert logging/print
statements at key points to trace variable values and execution flow,
rather than only explaining the code.

**Reasoning:**\
Print-debugging improves bug localization by exposing intermediate state
changes and execution traces. Research shows iterative debugging with
inserted logs helps identify inconsistencies between expected and actual
behavior, especially in complex algorithmic tasks.

**Example:**

    Do not rewrite the function yet.
    Add print/log statements to show:
    - loop indices
    - intermediate variable values
    - state changes
    Then analyze the logs to locate the bug.

---

### Guideline 2 \[2\]: Clarify Intent by Generating Tests First

**Description:**\
Ask the LLM to generate test cases that refine and partially formalize
the natural-language requirement before writing the implementation.

**Reasoning:**\
Natural language requirements can be ambiguous. Generating tests first
helps disambiguate intent and improves correctness by constraining
acceptable implementations and surfacing edge cases early.

**Example:**

    Before writing code:
    1) Generate 8–10 test cases covering edge cases.
    2) Ask clarifying questions based on these tests.
    3) Only then implement the function.

---

### Guideline 3 \[3\]: Assign Roles in the Prompt (Architect, Developer, Tester)

**Description:**\
Structure prompts so the model simulates different engineering roles
(e.g., requirements engineer, architect, developer, tester) that
collaborate sequentially.

**Reasoning:**\
Emulating software process models encourages planning, design
validation, testing, and refinement. Multi-role prompting has been shown
to improve accuracy, stability, and overall code quality.

**Example:**

    Act in stages:

    Role 1: Requirements Engineer -> extract constraints
    Role 2: Architect -> design modules
    Role 3: Developer -> implement
    Role 4: Tester -> write tests and review

---
### Guideline 4 \[4\]: Decompose Large Systems into Independent Components

**Description:**\
Prompt the model to break large problems into independent modules and
solve each separately before integrating.

**Reasoning:**\
Large codebases are difficult for single-agent reasoning due to context
limits. Breaking tasks into smaller components improves scalability,
focus, and reliability of generated code.

**Example:**

    Split the system into:
    - data processing module
    - API layer
    - storage layer
    Implement each independently, then compose.
---
### Guideline 5 \[5\]: Specify I/O, Constraints, and Edge Cases Explicitly

**Description:**\
Include precise input/output formats, preconditions, postconditions, and
exceptional cases directly in the prompt.

**Reasoning:**\
Empirical studies show prompt quality improves significantly when
parameters, return values, constraints, and exceptional conditions are
explicitly defined. Missing details often lead to incorrect or
underspecified implementations.

**Example:**

    Function requirements:
    Input:
    - list[int], length ≥ 1
    Output:
    - list[int] of same length

    Constraints:
    - handle empty sublists
    - O(n) time
    - raise ValueError on invalid input

---

## 2. Guidelines from from any related research/grey literature like practitioner or developer tool blogs

### Guideline 1 \[6\]: Start With a Written Spec Before Generating Code

**Description:**\
Ask the LLM to first produce a clear, structured specification
(requirements, constraints, expected outputs) and confirm it before
writing any code.

**Reasoning:**\
Spec-driven prompting reduces ambiguity and prevents the model from
"guessing" intent. The OpenSpec workflow emphasizes drafting a spec
first so the assistant operates against explicit requirements instead of
improvising solutions. This mirrors traditional software engineering
best practices where requirements clarity improves design quality and
reduces rework \[6\].

**Example:**\
**Prompt (step 1):**

    Before writing code, create a spec for a REST API that manages tasks.
    Include endpoints, data models, validation rules, and edge cases.

**Prompt (step 2 after approval):**

    Now implement the API in FastAPI based on the approved spec.

---
### Guideline 2 \[7\]: Scope Prompts to One Clear Task at a Time

**Description:**\
Structure prompts around a single objective (e.g., "write tests,"
"refactor function," "add caching") rather than combining multiple
changes.

**Reasoning:**\
LLMs perform best on well-defined, narrow tasks. The Pragmatic Engineer
article highlights that AI is strongest when applied to focused, bounded
work where developers can iterate and review outputs incrementally.
Breaking work into small steps reduces errors, improves reliability, and
makes outputs easier to verify \[7\].

**Example:**\
Instead of:

    Refactor this code, add logging, optimize performance, and write tests.

Use:

    Task 1: Refactor this function for readability.
    Task 2: Add structured logging.
    Task 3: Write unit tests.
---
### Guideline 3 \[6\]: Treat AI Output as a First Draft, Not Final Code

**Description:**\
Explicitly prompt the LLM to generate an initial implementation, then
refine it through structured follow-ups (refactoring, error handling,
documentation, and tests).

**Reasoning:**\
AI excels at producing working starting points but not always
production-ready systems. The Pragmatic Engineer article stresses that
AI accelerates early-stage coding but still requires engineering rigor
to reach maintainable quality. Prompting for iteration encourages better
architecture and reliability \[6\].

**Example:**

    Step 1: Generate a basic implementation of a CSV parser.
    Step 2: Refactor for modularity.
    Step 3: Add error handling and edge-case tests.
    Step 4: Document design decisions.
---
### Guideline 4 \[6\]\[7\]: Use Short Iterative Feedback Loops

**Description:**\
Run prompts in small cycles: generate -> review -> adjust -> regenerate,
rather than attempting a complete system in one prompt.

**Reasoning:**\
Frequent iteration improves alignment and correctness. Engineering
workflows increasingly rely on tight feedback loops when using AI tools,
as smaller iterations make it easier to catch issues early and maintain
control over the codebase. Spec-driven workflows also benefit from
incremental validation at each stage, ensuring the solution evolves in a
controlled way \[6\]\[7\].

**Example:**

    Iteration 1: Generate function signature + docstring.
    Iteration 2: Implement logic.
    Iteration 3: Add unit tests.
    Iteration 4: Optimize performance.
---
### Guideline 5 \[6\]: Require Verification Steps in the Prompt

**Description:**\
Ask the LLM to include validation steps such as tests, edge-case
analysis, and risk checks as part of the output.

**Reasoning:**\
LLMs can produce plausible but flawed code. Embedding verification into
the prompt ensures the model anticipates failure modes and strengthens
correctness. The Pragmatic Engineer article emphasizes that human review
and validation remain critical even as AI accelerates development \[1\].

**Example:**

    Implement a login endpoint.
    Also:
    - List possible edge cases
    - Add unit tests for each
    - Identify security risks (e.g., injection, brute force)
---

## 3. Guidelines from LLMs

### Guideline 1: State the Desired Level of Abstraction

**Description:**\
Tell the LLM whether you want high-level architecture, pseudocode, or
production-ready code before it starts generating.

**Reasoning:**\
LLMs default to an assumed level of detail. If you don't specify
abstraction level, they may over-engineer simple tasks or produce
shallow drafts for complex systems. Explicitly setting expectations
aligns output depth with task needs and reduces rework.

**Example:**

    Generate production-ready Python code with:
    - full type hints
    - docstrings
    - input validation
    - no placeholders
---
### Guideline 2: Provide a Reference Style or Pattern to Follow

**Description:**\
Include an example function, file structure, or coding pattern that the
model should mimic.

**Reasoning:**\
LLMs are highly pattern-driven. Supplying a stylistic or structural
reference improves consistency across files, enforces conventions, and
reduces mismatches with an existing codebase.

**Example:**

    Follow this structure:

    class Service:
        def __init__(self, repo):
            self.repo = repo

        def execute(self, input):
            ...

    Now implement UserService using the same pattern.
---
### Guideline 3: Constrain the Solution Space

**Description:**\
Explicitly limit tools, libraries, complexity, and approaches the model
is allowed to use.

**Reasoning:**\
Without constraints, LLMs may choose unexpected frameworks, unnecessary
dependencies, or overly complex solutions. Constraints improve
determinism, reproducibility, and maintainability.

**Example:**

    Implement using:
    - standard library only
    - no recursion
    - time complexity O(n)
    - no third-party dependencies
---
### Guideline 4: Ask the Model to Expose Assumptions

**Description:**\
Require the LLM to list any assumptions it is making about inputs,
environment, or requirements.

**Reasoning:**\
Hidden assumptions are a common source of bugs. By surfacing them
explicitly, you can catch incorrect interpretations early and refine the
prompt before implementation begins.

**Example:**

    Before coding:
    List all assumptions you are making about:
    - input format
    - error conditions
    - data size
    - performance constraints
---
### Guideline 5: Separate Generation from Review

**Description:**\
Use two-phase prompting: first generate the code, then ask the model to
critique and improve it.

**Reasoning:**\
LLMs are often better at reviewing than generating. A structured
self-review pass helps catch logical errors, missing edge cases, and
poor design choices. This mimics real engineering workflows (write ->
review -> revise).

**Example:**

    Phase 1: Generate the implementation.

    Phase 2: Review your code for:
    - correctness
    - performance issues
    - edge cases
    - readability improvements

    Then produce a revised version.
---

## 4. References

\[1\] Hu, X., et al. "Leveraging Print Debugging to Improve Code Generation in LLMs"\
\[2\] Fakhoury, S., et al. "LLM-Based Test-Driven Interactive Code Generation: User Study and Empirical Evaluation" DOI\
\[3\] Lin, F., et al. "SOEN-101: Code Generation by Emulating Software Process Models Using Large Language Model Agents" arXiv\
\[4\] Ishibashi, Y., & Nishimura, Y. "Self-Organized Agents: A LLM Multi-Agent Framework toward Ultra Large-Scale Code Generation and Optimization" arXiv\
\[5\] Midolo, A., et al. "Guidelines to Prompt Large Language Models for Code Generation: An Empirical Characterization" arXiv\
\[6\] Orosz, G., & Osmani, A. "How AI-assisted coding will change software engineering: hard truths" Pragmatic Engineer Blog\
\[7\] Code Coup "OpenSpec: A Spec-Driven Workflow for AI Coding Assistants (No API Keys Needed)" Medium

---