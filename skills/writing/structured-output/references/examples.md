# Examples

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

