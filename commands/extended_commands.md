# Extended CPL Commands

    The following commands extend the basic CPL instruction set and enable 
working with **mental models**.  These commands are used in the `photosynthesis`
 example (`programs/example2.cpl`).

    ### `StartModel`

    * **Prompt**: `Create a new mental model for topic: {{input}}`
    * **Write**: `mental_models ← mental_models + [{{input}}, {declarative: [], 
procedural: []}]`

    Initialises a new mental model keyed by the given topic.  The model contains
 its own declarative and procedural sub‑memories.  Subsequent facts and 
procedures extracted about this topic should be merged into this model via 
`ExtendModel`.

    ### `FindModel`

    * **Prompt**: `Retrieve a mental model related to: {{input}}`
    * **Write**: `working_memory[model] ← retrieved model`

    Searches the `mental_models` list for a model associated with the given 
topic and stores it in `working_memory['model']`.  This allows later commands to
 reference or inspect the retrieved model.

    ### `ExtendModel`

    * **Prompt**: `Add new facts and actions to the mental model: {{input}}`
    * **Write**: `mental_models[{{input}}] ← extended with current declarative 
and procedural memory`

    Copies the current `declarative` and `procedural` memories into the mental 
model associated with `{{input}}`.  This enriches the model with the newly 
discovered knowledge.

    ### `EvaluateSteps`

    This command is part of the basic command set, but it is listed here for 
convenience because it is commonly used with mental models.

    * **Prompt**: `Evaluate utility of procedural steps.`
    * **Write**: `procedural ← updated steps with utility`

    Assigns a utility score to each procedural step based on the model’s 
assessment of its usefulness or success.