class ExampleSchema:
    def example_schema(self):
        schema_example = {
            'type': 'object',
            'properties': {
                'field_number': {'type': ['number', 'null']},
                'field_object': {'type': ['object', 'null']},
                'field_array': {'type': ['array', 'null']},
                'field_bool': {'type': ['boolean', 'null','string']},
                'field_string': {'type': 'string'}
                },
            # 'required': ['field_string']
        }
        return schema_example
