# Basic CPL Commands

    This file defines the core commands used by the Cognitive Prompt Language.  
Each command consists of a **prompt template** and a description of how it 
updates the interpreter’s memory.  The placeholders (e.g. `{{input}}`, 
`{{goal}}`) are filled in by the interpreter before the prompt is sent to the 
language model.

    ### `LET`

    * **Prompt**: `Set the following goal: {{input}}`
    * **Write**: `goal ← input`

    Assigns the provided input string to the `goal` variable.  This sets the 
topic or task the interpreter is working on.

    ### `ExtractFacts`

    * **Prompt**: `For this topic {{goal}}, generate up to 3 declarative and 3 
procedural facts from your knowledge. (do not translate them in logical 
formulas)`
    * **Write**: `declarative ← [...], procedural ← [...]`

    Given a goal, the model extracts a handful of relevant facts and actions.  
The declarative facts are stored in the `declarative` memory and the procedural 
steps are stored in the `procedural` memory.

    ### `EvaluateFacts`

    * **Prompt**: `Evaluate confidence for fact: {{input}}`
    * **Write**: `declarative ← confidence updated`

    Assigns or updates a confidence score for a declarative fact.  The 
interpreter should merge the returned confidence into the stored fact.

    ### `EvaluateSteps`

    * **Prompt**: `Evaluate utility of procedural steps.`
    * **Write**: `procedural ← updated steps with utility`

    Updates the success metric associated with each procedural step based on the
 model’s assessment.

    ### `IdentifyConflict`

    * **Prompt**: `Identify conflicts with: {{input}}`
    * **Write**: `working_memory[conflict] ← result`

    Checks whether a given fact contradicts existing entries in the declarative 
memory.  If a conflict is detected the interpreter sets 
`working_memory['conflict']` to `True`.

    ### `Assimilate`

    * **Prompt**: `Reconcile contradictions in declarative memory by 
generalizing, adding exceptions, or revising conflicting facts.`
    * **Write**: `declarative ← updated memory with resolved contradictions`

    Applies belief revision strategies to resolve inconsistencies in the 
declarative memory.  This might weaken conflicting assertions or annotate them 
with qualifiers like "is not a typical".

    ### `IF`

    * **Prompt**: `(conditional execution based on working_memory or result)`
    * **Write**: Branch based on boolean

    Evaluates a condition stored in `working_memory` and jumps to a specified 
line if the condition is true.  The interpreter handles the branching logic 
directly.

    ### `FOR`

    * **Prompt**: `(loop start over memory array)`
    * **Write**: Set loop variable in `working_memory`

    Begins a loop over a collection such as `declarative` or `procedural`.  The 
interpreter sets the loop variable and advances through the collection until a 
corresponding `NEXT` is encountered.

    ### `NEXT`

    * **Prompt**: `(advance loop)`
    * **Write**: Repeat or continue

    Advances the loop variable to the next element in the collection.  If more 
elements remain, execution jumps back to the corresponding `FOR` line; 
otherwise, it continues after the `NEXT` line.

    ### `END`

    * **Prompt**: `Execution complete.`
    * **Write**: `(none)`

    Terminates program execution.