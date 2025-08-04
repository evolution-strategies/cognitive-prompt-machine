# Cognitive Prompt Machine Repository

This repository contains a lightweight framework for running **Cognitive Prompt Language (CPL)** programs on top of a large language model.  The goal is to make it easy to experiment with memory‑augmented reasoning inside the prompt space without relying on external code.

The code here is inspired by the paper *“Cognitive Prompt Machines: A BASIC‑Inspired Language for Cognitive Prompt Agents”*.  In that work, a minimal scripting language – reminiscent of early BASIC interpreters – is used to control how an LLM processes information, updates declarative/procedural memory and resolves contradictions.

## Repository structure

```
cognitive-prompt-machine/
├── README.md              # This file
├── interpreter/           # Interpreter specification(s)
│   └── interpreter.md     # Description of how the CPL interpreter works
├── commands/              # Prompt templates for the command set
│   ├── basic_commands.md  # Definitions for the base command set
│   └── extended_commands.md
│                           # Additional commands used in the photosynthesis example
├── programs/              # Sample CPL programs
│   ├── example1.cpl       # “A looks like B” sample program
│   ├── example2.cpl       # “Photosynthesis” sample program
│   └── example3.cpl       # A third example illustrating belief revision
└── run_cpl.py             # Python script to execute CPL programs via GPT‑4o
```

### `interpreter/interpreter.md`

This document describes the overall CPL execution model, how memory is organised (goal, working memory, declarative memory, procedural memory, mental models) and how the interpreter processes lines sequentially.  It also notes the output format used to log each step.

### `commands/basic_commands.md`

Defines the core CPL commands such as `LET`, `ExtractFacts`, `EvaluateFacts`, `EvaluateSteps`, `IdentifyConflict`, `Assimilate`, `IF`, `FOR`, `NEXT` and `END`.  Each definition includes a **prompt template** (the text sent to the language model) and a description of how the memory should be updated.

### `commands/extended_commands.md`

Provides additional commands used in more advanced CPL scripts.  In the photosynthesis example these commands include `StartModel`, `FindModel` and `ExtendModel` to manage mental models.

### `programs/*.cpl`

The `.cpl` files in the `programs` folder are pure CPL programs – they contain only the numbered instructions and do not include interpreter documentation or command definitions.  You can run these examples with the provided Python script.

### `run_cpl.py`

This script demonstrates how to execute CPL programs using the OpenAI GPT‑4o API.  **Unlike the initial version of this project, the interpreter no longer fragments the program into separate API calls.**  Instead, `run_cpl.py` reads the interpreter specification from the `interpreter/` folder and the selected `.cpl` program from the `programs/` folder, concatenates them into a single prompt and sends that prompt to GPT‑4o.  The response returned by the model contains the complete execution trace, including memory updates and logs.  You will need to set the environment variable `OPENAI_API_KEY` to your own API key and install the `openai` Python package to use this script.

## Getting started

1. **Install the dependencies**:

   ```bash
   pip install openai
   ```

2. **Set your OpenAI API key**:

   ```bash
   export OPENAI_API_KEY="sk-..."
   ```

3. **Run an example program**:

   ```bash
  python run_cpl.py programs/example1.cpl
   ```

   The interpreter will send the entire interpreter specification and program to the model in a single call and then print the model’s response.

Feel free to modify the program files or write your own `.cpl` scripts.  New commands can be added by creating additional prompt templates in the `commands` folder and referencing them in your `.cpl` file.  The interpreter specification can also be extended or replaced by adding new files under the `interpreter/` directory and adjusting `run_cpl.py` to read the appropriate specification.

## License

This repository is provided for educational purposes.  Feel free to use, modify and extend it as you see fit.