from prompt_builder import PromptBuilder

builder = PromptBuilder('prompts.json', name='math_problems')
examples = [
    {'description': '1 + 1', 'result': '2'},
    {'description': '2 + 2', 'result': '4'},
    {'description': '5 / 2', 'result': '2.5'},
]

query = {'description': '5 * 3'}

prompt = builder.build(query=query, examples=examples, variant='pt')
print(prompt)

prompt = builder.build(query=query, examples=examples, variant='en')
print(prompt)