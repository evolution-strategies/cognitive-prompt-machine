#!/usr/bin/env python3
"""
run_cpl.py
---------------

This script executes **Cognitive Prompt Language (CPL)** programs by sending a
single combined prompt to OpenAI’s GPT‑4o model.  It concatenates the
interpreter specification and the CPL program into one message so that the
language model can perform the entire execution internally.  Unlike the
previous implementation, it does not fragment the program into multiple API
calls.

Usage::

    export OPENAI_API_KEY="sk-..."
    pip install openai
    python run_cpl.py programs/example1.cpl

You can also pass multiple `.cpl` files separated by spaces.

Environment variables:

    OPENAI_API_KEY  Your OpenAI API key.  Required to call the GPT‑4o model.
"""

import os
import sys
from typing import List

try:
    import openai
except ImportError:
    openai = None  # We'll handle the import error later


def call_openai(prompt: str) -> str:
    """Call the OpenAI GPT‑4o model with the given prompt and return its response.

    This function requires the `openai` package and the `OPENAI_API_KEY`
    environment variable.  If the package is missing, it raises an informative
    error.
    """
    if openai is None:
        raise ImportError(
            "The openai package is not installed.  Please run 'pip install openai' to "
            "use this interpreter."
        )
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY environment variable is not set.")
    openai.api_key = api_key
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an interpreter for the cognitive prompt language."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.0,
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        raise RuntimeError(f"OpenAI API call failed: {e}")


def run_program(program_path: str, interpreter_path: str) -> None:
    """Read the interpreter specification and a CPL program, combine them into a
    single prompt and send it to GPT‑4o.

    The model is expected to simulate the CPL interpreter internally and return
    the full execution trace, including prompts, responses and memory updates.
    """
    # Read interpreter specification
    with open(interpreter_path, "r", encoding="utf-8") as f:
        interpreter_text = f.read()
    # Read program
    with open(program_path, "r", encoding="utf-8") as f:
        program_text = f.read()
    # Compose the prompt
    prompt = (
        "You are a cognitive prompt machine interpreter.\n\n"
        "Interpreter specification:\n"
        f"{interpreter_text}\n\n"
        "CPL program:\n"
        f"{program_text}\n\n"
        "Run the program according to the interpreter specification and provide the complete execution trace, "
        "including any prompts sent, model responses, memory updates and final state."
    )
    # Call the model
    response = call_openai(prompt)
    # Print the model's response
    print(response)


def main(argv: List[str]) -> None:
    if not argv:
        print("Usage: run_cpl.py <program1.cpl> [program2.cpl ...]")
        return
    # Default interpreter specification path
    interpreter_path = os.path.join(
        os.path.dirname(__file__), "interpreter", "interpreter.cpl"
    )
    for path in argv:
        print(f"\nRunning {path}\n" + "=" * (9 + len(path)))
        run_program(path, interpreter_path)


if __name__ == "__main__":
    main(sys.argv[1:])