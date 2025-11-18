# Algorithms

```python
for principle in principles:
       if principle.lower() not in output.lower():
           DRIFT_DETECTED()
   
```

```python
def calculate_total(items):
    return sum(item.price for item in items)

```

```python
def calculate_total(items: List[Item]) -> float:
    return sum(item.price for item in items) if items else 0.0

```