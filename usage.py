from prompt_builder import PromptBuilder

builder = PromptBuilder('prompts.json', name='math_problems')
examples = [
    {'description': '1 + 1', 'result': '2'},
    {'description': '2 + 2', 'result': '4'},
    {'description': '5 / 2', 'result': '2.5'},
]

query = {'description': '5 * 3'}

builder.set_variant('pt')

prompt = builder.build(examples=examples, query=query, nationality='brasileiro')
print(prompt)

prompt = builder.build(variant='en', examples=examples, query=query, nationality='english') 
print(prompt)