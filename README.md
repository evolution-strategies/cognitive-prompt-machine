# Cognitive Prompt Machine Repository

This repository contains a lightweight framework for running **Cognitive Prompt Language (CPL)** programs on top of a large language model. The goal is to make it easy to experiment with memory‑augmented reasoning inside the prompt space without relying on external code.

The code here is inspired by the paper *“Cognitive Prompt Machines: A BASIC‑Inspired Language for Cognitive Prompt Agents”*. In that work, a minimal scripting language – reminiscent of early BASIC interpreters – is used to control how an LLM processes information, updates declarative/procedural memory and resolves contradictions.

## Repository structure

```
cognitive-prompt-machine/
├── README.md              # This file
├── paper/                 # Associated paper
│   └── paper.pdf          # Full preprint describing the method
├── interpreter/           # Interpreter specification(s)
│   └── interpreter.cpl    # Description of how the CPL interpreter works
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

### `paper/paper.pdf`

This PDF contains the paper *“Cognitive Prompt Machines: A BASIC‑Inspired Language for Cognitive Prompt Agents”*, which outlines the theoretical motivation and architecture behind CPL and its interpreter model.

### `interpreter/interpreter.cpl`

This file describes the CPL execution model, including how memory is structured (e.g., goal, working memory, declarative memory, procedural memory, mental models), and how the interpreter processes each line sequentially.

### `commands/basic_commands.md`

Defines the core CPL commands such as `LET`, `ExtractFacts`, `EvaluateFacts`, `EvaluateSteps`, `IdentifyConflict`, `Assimilate`, `IF`, `FOR`, `NEXT` and `END`. Each command has a prompt template and a description of how it updates memory.

### `commands/extended_commands.md`

Additional CPL commands used for managing mental models. Examples include `StartModel`, `FindModel`, and `ExtendModel`, used in programs like `example2.cpl`.

### `programs/*.cpl`

These `.cpl` files contain the actual CPL programs with numbered instructions. You can run any of them using `run_cpl.py`.

### `run_cpl.py`

Python script that executes `.cpl` programs by sending the full interpreter and program in a single call to OpenAI’s GPT‑4o API. You must set `OPENAI_API_KEY` and install the `openai` package to use it.

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

You may create your own `.cpl` scripts or expand the command set by defining new templates in the `commands/` folder. To switch interpreters, replace or add files in the `interpreter/` directory and point `run_cpl.py` to the correct file.

## License

This repository is provided for educational and research purposes. Feel free to use, modify, and extend it as needed.
