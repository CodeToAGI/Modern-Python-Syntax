# CodeToAGI — Episode 45: Modern Python Syntax

**Python 3.8+ → 3.13 Features**

---

## 🎯 What You Learned

- Walrus Operator `:=` — assign + test in one expression
- Positional-only `/` and Keyword-only `*` in function signatures
- `TypeAlias` for readable complex types
- `ParamSpec` for better decorator typing
- Key features from Python 3.10 to 3.13

---

## 🚀 Challenge: Build a Modern-Syntax Data Pipeline

**Goal**: Create a clean, typed data reader using modern Python features.

### Requirements

1. Use `TypeAlias` for row types
2. Use keyword-only argument (`*`) for `chunk_size`
3. Use walrus operator (`:=`) in the reading loop
4. Bonus: Add a `ParamSpec` logging decorator

---

### Solution

See `challenge_modern_pipeline.py`

---

## How to Run

```bash
python challenge_solution.py
