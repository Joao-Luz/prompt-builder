# Prompt Builder

Simple library to build LLM prompts.

## Usage

Create a `.json` file containing a template for your prompts. Prompts are made out of parts and their order is defined by the `schema`. Each part is formatted in Python's `f-string` format, with variables being sourced from `kwargs` passed to the `PromptBuilder`'s `build` method. Here's a list of possible prompt parts:

- `examples`: used to pass examples for LLM In Context Learning. This is a template for a single example, but multiple examples may be passed to the `build` method as a list under the `examples` argument. Each example is succeeded by a line break;
- `query`: used to pass a query to the LLM. Information is passed via the `query` argument.
- Any other name except for `variants` and `schema`: the remainder of the prompt's parts. Information is passed via the `build`'s method kwargs.

Variants may be defined under the `"variants"` object, but are optional. Each variant may redefine the prompt's schema and parts **for that variant only**. If a variant doesn't redefine a component, it'll use the prompt's respective default component. You may set a default variant by using the `set_variant` method, but a variant may also be specified with the `variant` argument.

Here is an example usage, with both the `.json` file and Python call:

```json
{
    "schema": ["description", "guidance", "examples", "query"],
    "examples": "{description} = {result}",
    "query": "{description} = ",
    "variants": {
        "en": {
            "description": "You are an {nationality} mathematician.",
            "guidance": "Answer with numeric solutions.",
        },
        "pt": {
            "description": "Você é um matemático {nationality}.",
            "guidance": "Responda com soluções numéricas.",
        }
    }
}
```
Python call:

```python
from prompt_builder import PromptBuilder

builder = PromptBuilder('math_problems.json', name='math_problems')
examples = [
    {'description': '1 + 1', 'result': '2'},
    {'description': '2 + 2', 'result': '4'},
    {'description': '5 / 2', 'result': '2.5'},
]

query = {'description': '5 * 3'}

builder.set_variant('pt')
prompt_pt = builder.build(examples=examples, query=query, nationality='brasileiro')
prompt_en = builder.build(variant='en', examples=examples, query=query, nationality='english')
```