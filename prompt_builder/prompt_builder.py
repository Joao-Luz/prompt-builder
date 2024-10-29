import json

class PromptBuilder():
    class PromptTemplate():
        def __init__(self, schema, parts):
            self.schema = schema
            self.parts = parts
        
        def build(self, examples=[], query={}, **kwargs):
            prompt = ''
            for key in self.schema:
                part = self.parts[key]
                if key == 'examples':
                    for example in examples:
                        prompt += part.format(**example) + '\n\n'

                elif key == 'query':
                    prompt += part.format(**query)

                else:
                    prompt += part.format(**kwargs) + '\n\n'

            return prompt

    def __init__(self, prompts_file=None, name=None):
        self.variants = []
        if prompts_file is not None:
            self.load(prompts_file, name)
        pass

    def load(self, prompts_file, name):
        self.name = name
        with open(prompts_file) as f:
            data = json.load(f)
        
        self._prompt_templates = {}

        parts = {}
        for key in data:
            if key not in ['variants', 'schema']:
                parts[key] = data[key]

        if 'variants' not in data:
            variants = {'default': parts}
        else:
            variants = data['variants']

        for variant, template in variants.items():
            self.variants.append(variant)
            schema = data['schema'] if 'schema' not in template else template['schema']

            template_parts = parts.copy()
            for key in template:
                template_parts[key] = template[key]

            self._prompt_templates[variant] = PromptBuilder.PromptTemplate(schema, template_parts)

    def build(self, variant=None, examples=[], query={}, **kwargs):
        if variant not in self.variants:
            raise Exception(f'Unknown variant "{variant}" for prompt template "{self.name}"')

        prompt = self._prompt_templates[variant]
        return prompt.build(examples=examples, query=query, **kwargs)
