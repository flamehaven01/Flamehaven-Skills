# Examples

**Original Code:**
```python
def calculate_total(items):
    return sum(item.price for item in items)
```

**Principles:**
- Preserve functionality: sum all item prices
- Handle empty list
- Type safety

**Refactored:**
```python
def calculate_total(items: List[Item]) -> float:
    return sum(item.price for item in items) if items else 0.0
```

**Validation:**
1. **SHALLOW**: ✓ "sum", "price", "items" present
2. **DEEP**: ✓ LLM confirms semantic preservation (score: 0.95)
3. **ATTENTION**: ✓ Drift score: 0.15 (OBSERVE)

**Result:** DELIVER ✓

