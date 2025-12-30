# Constitution for the Python Command-Line Todo Application

## 1. Core Mission

To create a fully-featured, command-line interface (CLI) todo application, developed and maintained entirely by an agentic software development stack. This project serves as a testbed for AI-driven software engineering, from specification to implementation and testing, without direct human coding.

## 2. Core Principles

### 2.1. Agentic Development Stack
All software, documentation, and specifications will be generated, reviewed, and modified by autonomous or semi-autonomous AI agents. Human intervention is limited to providing high-level goals, and reviewing and approving agent-generated plans and code.

### 2.2. No Human-Written Code
No code will be written directly by humans. All application source code, tests, and related artifacts must be the product of agentic generation.

### 2.3. Technology Stack
- **Language:** Python 3.13 or newer.
- **Data Storage:** All task data will be stored exclusively in-memory. There will be no file-based or database persistence. Application state is ephemeral and resets on each launch.
- **Standard Library:** The use of the Python standard library is strongly preferred. Third-party libraries should be avoided unless absolutely necessary for core functionality and must be approved in the specification.

### 2.4. Architectural Philosophy
- **CLI-First Design:** The application must be designed as a pure command-line tool. All user interactions will occur through shell commands, arguments, and options.
- **Clean Architecture:** The codebase will be structured to separate concerns, promoting readability, maintainability, and testability. A clear distinction will be made between the presentation layer (CLI), business logic (services), and data models.
- **Deterministic Behavior:** Given the same sequence of commands, the application must produce the exact same output and internal state. Randomness or reliance on external, unpredictable factors is forbidden.
- **Stateless Operations:** Each command should execute as a stateless operation where possible, receiving all necessary information via its arguments.

## 3. Development Process

### 3.1. Specification-Driven Development
All development work must begin with a formal specification. The specification will define the features, command syntax, expected behavior, and data structures. No implementation work may commence until the relevant specification is complete and approved.

### 3.2. Testing
- **Unit Tests:** All business logic must be accompanied by a comprehensive suite of unit tests.
- **Integration Tests:** Tests will be written to verify the correct interaction between different components of the application.
- **Test-Driven Development (TDD):** While not strictly mandatory for all changes, a TDD-like approach (where tests are written before or alongside the implementation) is highly encouraged.
- **Deterministic Tests:** All tests must be deterministic and produce the same results on every run.

## 4. Operational Rules

- **No Side Effects:** Functions and methods should be pure where possible, minimizing side effects.
- **Error Handling:** The application must handle errors gracefully and provide clear, informative error messages to the user.
- **Code Style:** All Python code must adhere to the PEP 8 style guide. Readability is paramount.

This constitution is the supreme governing document for this project. All specifications, code, and documentation must adhere to its principles.
