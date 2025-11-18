### Layer 1: Schema Definition (SCL Template)

**BEFORE generation:**

1. **Define Schema Structure**
   ```python
   # SCL (Structured Constitution Language) format
   schema = {
       'type': 'object',  # object, array, string, number, boolean
       'required': ['field1', 'field2'],
       'properties': {
           'field1': {
               'type': 'string',
               'description': 'Description of field',
               'constraints': {
                   'min_length': 5,
                   'max_length': 100,
                   'pattern': r'^[A-Za-z0-9]+$',
                   'enum': ['option1', 'option2']  # if limited values
               }
           },
           'field2': {
               'type': 'number',
               'constraints': {
                   'min': 0,
                   'max': 100
               }
           },
           'field3': {
               'type': 'array',
               'items': {
                   'type': 'object',
                   'properties': {...}
               }
           }
       },
       'constitutional_requirements': {
           'forbidden_values': ['banned1', 'banned2'],
           'required_patterns': ['must include X'],
           'validation_rules': ['custom_rule_1', 'custom_rule_2']
       }
   }
   ```

2. **Template Registration**
   ```python
   templates = {
       'api_response': {
           'schema': api_response_schema,
           'version': '1.0',
           'strict_mode': True  # Reject any schema violations
       },
       'config_file': {
           'schema': config_schema,
           'version': '2.1',
           'strict_mode': True
       },
       'report': {
           'schema': report_schema,
           'version': '1.3',
           'strict_mode': False  # Allow extensions
       }
   }

   def get_template(template_name, version=None):
       template = templates.get(template_name)
       if not template:
           raise TemplateNotFoundError(template_name)

       if version and template['version'] != version:
           raise VersionMismatchError(version, template['version'])

       return template
   ```

**Threshold:** Schema must be well-defined and versioned



### Layer 2: Generation with Constraints

**DURING generation:**

1. **Constraint-Aware Generation**
   ```python
   def generate_structured_output(template, data, principles=None):
       schema = template['schema']
       output = {}

       for field, field_schema in schema['properties'].items():
           # Check if field is required
           if field in schema.get('required', []):
               if field not in data:
                   raise MissingRequiredFieldError(field)

           # Generate/validate field value
           value = data.get(field)

           if value is not None:
               # Apply constraints
               validated_value = validate_and_constrain(
                   value=value,
                   field_schema=field_schema
               )
               output[field] = validated_value

       # Apply constitutional requirements
       if 'constitutional_requirements' in schema:
           output = apply_constitutional_checks(
               output,
               schema['constitutional_requirements']
           )

       return output
   ```

2. **Real-Time Validation During Generation**
   ```python
   def validate_and_constrain(value, field_schema):
       field_type = field_schema['type']
       constraints = field_schema.get('constraints', {})

       # Type validation
       if not isinstance(value, get_python_type(field_type)):
           raise TypeValidationError(field_type, type(value))

       # Constraint validation
       if field_type == 'string':
           if 'min_length' in constraints:
               if len(value) < constraints['min_length']:
                   raise ConstraintViolationError('min_length')

           if 'max_length' in constraints:
               if len(value) > constraints['max_length']:
                   value = value[:constraints['max_length']]  # Truncate

           if 'pattern' in constraints:
               if not re.match(constraints['pattern'], value):
                   raise PatternViolationError(constraints['pattern'])

           if 'enum' in constraints:
               if value not in constraints['enum']:
                   raise EnumViolationError(constraints['enum'])

       elif field_type == 'number':
           if 'min' in constraints:
               value = max(value, constraints['min'])
           if 'max' in constraints:
               value = min(value, constraints['max'])

       elif field_type == 'array':
           if 'min_items' in constraints:
               if len(value) < constraints['min_items']:
                   raise ConstraintViolationError('min_items')
           if 'max_items' in constraints:
               value = value[:constraints['max_items']]

       return value
   ```

3. **Nested Structure Handling**
   ```python
   def generate_nested(schema, data):
       if schema['type'] == 'object':
           return generate_structured_output({'schema': schema}, data)

       elif schema['type'] == 'array':
           items_schema = schema.get('items', {})
           return [
               generate_nested(items_schema, item)
               for item in data
           ]

       else:
           return validate_and_constrain(data, schema)
   ```

**Threshold:** All constraints satisfied, no validation errors



### Layer 3: Post-Generation Validation

**AFTER generation:**

1. **Schema Compliance Verification**
   ```python
   def verify_schema_compliance(output, schema):
       errors = []

       # Required fields check
       for required_field in schema.get('required', []):
           if required_field not in output:
               errors.append({
                   'type': 'missing_required',
                   'field': required_field,
                   'severity': 'critical'
               })

       # Type and constraint verification
       for field, value in output.items():
           if field in schema['properties']:
               field_schema = schema['properties'][field]
               try:
                   validate_and_constrain(value, field_schema)
               except ValidationError as e:
                   errors.append({
                       'type': 'validation_error',
                       'field': field,
                       'error': str(e),
                       'severity': 'high'
                   })

       # Extra fields check (if strict mode)
       if schema.get('strict_mode', False):
           allowed_fields = set(schema['properties'].keys())
           actual_fields = set(output.keys())
           extra_fields = actual_fields - allowed_fields

           if extra_fields:
               errors.append({
                   'type': 'extra_fields',
                   'fields': list(extra_fields),
                   'severity': 'medium'
               })

       compliance_score = 1.0 - (len(errors) / max(len(schema['properties']), 1))

       return {
           'compliant': len([e for e in errors if e['severity'] == 'critical']) == 0,
           'score': compliance_score,
           'errors': errors
       }
   ```

2. **Constitutional Requirements Check**
   ```python
   def validate_constitutional_requirements(output, requirements):
       violations = []

       # Forbidden values
       for forbidden in requirements.get('forbidden_values', []):
           if contains_value(output, forbidden):
               violations.append({
                   'type': 'forbidden_value',
                   'value': forbidden,
                   'action': 'BLOCK'
               })

       # Required patterns
       for pattern in requirements.get('required_patterns', []):
           if not matches_pattern(output, pattern):
               violations.append({
                   'type': 'missing_pattern',
                   'pattern': pattern,
                   'action': 'REFACTOR'
               })

       # Custom validation rules
       for rule in requirements.get('validation_rules', []):
           if not execute_validation_rule(output, rule):
               violations.append({
                   'type': 'rule_violation',
                   'rule': rule,
                   'action': 'REFACTOR'
               })

       return violations
   ```

3. **Drift Detection (Semantic Validation)**
   ```python
   # If principles provided during generation
   if principles:
       drift_score = drift_detector.detect(
           original=principles,
           output=json.dumps(output, indent=2)
       )

       if drift_score >= 0.3:
           REFACTOR('Semantic drift detected')
   ```

**Threshold:** 100% schema compliance, zero critical errors

## Integrated Flow

```
Input Data + Template Name
    ↓
[Schema Loading]
    ├─ Retrieve template
    ├─ Validate schema definition
    └─ Check version compatibility
    ↓
[Constraint-Aware Generation]
    ├─ Generate each field
    ├─ Apply constraints in real-time
    ├─ Handle nested structures
    └─ Apply constitutional requirements
    ↓
[Post-Generation Validation]
    ├─ Verify schema compliance
    ├─ Check constitutional requirements
    ├─ Detect semantic drift (if principles provided)
    └─ Calculate compliance score
    ↓
[Gate Decision]
    ├─ 100% compliance → APPROVE
    ├─ Critical errors → BLOCK
    └─ Non-critical errors → REFACTOR or APPROVE (depends on strict_mode)
    ↓
OUTPUT: Validated structured output + compliance report
```

## Common Templates

### Template 1: API Response

```python
api_response_template = {
    'schema': {
        'type': 'object',
        'required': ['status', 'data'],
        'properties': {
            'status': {
                'type': 'string',
                'constraints': {'enum': ['success', 'error']}
            },
            'data': {
                'type': 'object'
            },
            'error': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'string'},
                    'message': {'type': 'string'}
                }
            },
            'metadata': {
                'type': 'object',
                'properties': {
                    'timestamp': {'type': 'string'},
                    'version': {'type': 'string'}
                }
            }
        }
    },
    'version': '1.0',
    'strict_mode': True
}
```

### Template 2: Configuration File

```python
config_template = {
    'schema': {
        'type': 'object',
        'required': ['app_name', 'environment'],
        'properties': {
            'app_name': {
                'type': 'string',
                'constraints': {'pattern': r'^[a-z0-9-]+$'}
            },
            'environment': {
                'type': 'string',
                'constraints': {'enum': ['development', 'staging', 'production']}
            },
            'database': {
                'type': 'object',
                'properties': {
                    'host': {'type': 'string'},
                    'port': {'type': 'number', 'constraints': {'min': 1, 'max': 65535}},
                    'credentials': {
                        'type': 'object',
                        'properties': {
                            'username': {'type': 'string'},
                            'password': {'type': 'string'}
                        }
                    }
                }
            },
            'features': {
                'type': 'array',
                'items': {'type': 'string'}
            }
        },
        'constitutional_requirements': {
            'forbidden_values': ['password=admin', 'debug=true'],
            'validation_rules': ['no_plain_text_passwords']
        }
    },
    'version': '2.0',
    'strict_mode': True
}
```

### Template 3: Report Structure

```python
report_template = {
    'schema': {
        'type': 'object',
        'required': ['title', 'summary', 'sections'],
        'properties': {
            'title': {
                'type': 'string',
                'constraints': {'min_length': 10, 'max_length': 200}
            },
            'summary': {
                'type': 'string',
                'constraints': {'min_length': 50, 'max_length': 500}
            },
            'sections': {
                'type': 'array',
                'constraints': {'min_items': 1},
                'items': {
                    'type': 'object',
                    'properties': {
                        'heading': {'type': 'string'},
                        'content': {'type': 'string'},
                        'subsections': {
                            'type': 'array',
                            'items': {'type': 'object'}
                        }
                    }
                }
            },
            'metadata': {
                'type': 'object',
                'properties': {
                    'author': {'type': 'string'},
                    'date': {'type': 'string'},
                    'version': {'type': 'string'}
                }
            }
        }
    },
    'version': '1.3',
    'strict_mode': False  # Allow additional fields
}
```

## Red Flags

- "Just generate JSON, no schema needed"
- "Skip validation for speed"
- "Structure is flexible"
- "Constraints slow us down"
- "90% compliance is good enough"

**ALL mean: STOP. Use structured generation.**

## Integration

**REQUIRED by:**
- `api-development` - Response formatting
- `config-management` - Configuration generation
- `document-generation` - Structured documents

**Complementary:**
- `drift-detection` - Semantic validation
- `principle-validation` - Constitutional compliance
- `self-validation` - Output verification

## Example: API Response Generation

**Input:**
```python
data = {
    'user_id': 12345,
    'name': 'John Doe',
    'email': 'john@example.com',
    'role': 'admin'
}

template_name = 'api_response'
```

**Execution:**

1. **Generate with constraints:**
   ```python
   output = generate_structured_output(
       template=get_template('api_response'),
       data={
           'status': 'success',
           'data': data,
           'metadata': {
               'timestamp': '2024-01-15T10:30:00Z',
               'version': '1.0'
           }
       }
   )
   ```

2. **Validation:**
   ```python
   compliance = verify_schema_compliance(
       output,
       get_template('api_response')['schema']
   )

   # Result:
   # {
   #   'compliant': True,
   #   'score': 1.0,
   #   'errors': []
   # }
   ```

**Output:**
```json
{
  "status": "success",
  "data": {
    "user_id": 12345,
    "name": "John Doe",
    "email": "john@example.com",
    "role": "admin"
  },
  "metadata": {
    "timestamp": "2024-01-15T10:30:00Z",
    "version": "1.0"
  }
}
```

**Compliance:** 100% ✓

## Verification Checklist

- [ ] Schema defined and versioned
- [ ] Template registered
- [ ] All required fields present
- [ ] Type validation passed
- [ ] Constraints satisfied
- [ ] Constitutional requirements met
- [ ] Nested structures validated
- [ ] Schema compliance = 100%
- [ ] Zero critical errors
- [ ] Drift detection passed (if applicable)
- [ ] TraceVault logged

## Final Rule

```
Structured Output → Schema compliance = 100% AND Constitutional requirements met
Otherwise → REFACTOR or BLOCK
```

Structure without validation is fragile.