"""
CodeToAGI — Episode 45 Challenge
Modern Python Syntax Data Pipeline

Task:
- Use TypeAlias for clean type names
- Use keyword-only arguments (*)
- Use walrus operator (:=) in a loop
- Bonus: Add ParamSpec to a decorator
"""

from typing import TypeAlias, Generator, Callable, ParamSpec, TypeVar
import csv
from pathlib import Path

# TypeAlias — clean readable names
Row: TypeAlias = dict[str, str]
Rows: TypeAlias = Generator[Row, None, None]

P = ParamSpec("P")
T = TypeVar("T")


def logged(fn: Callable[P, T]) -> Callable[P, T]:
    """Bonus: ParamSpec decorator that preserves signature for mypy."""
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        print(f"→ Calling {fn.__name__} with {len(args)} positional args")
        return fn(*args, **kwargs)
    return wrapper


@logged
def read_csv_pipeline(path: str, *, chunk_size: int = 1000) -> Rows:
    """Modern syntax data pipeline: clean, typed, and readable."""
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        while row := next(reader, None):   # walrus operator
            # Process chunk
            if len(row) > 0:  # simple filter
                yield row
            
            # Every chunk_size rows, we could do batch processing here
            if (processed := sum(1 for _ in [])) % chunk_size == 0:  # example
                pass  # batch processing point


# ====================== TEST ======================
if __name__ == "__main__":
    print("=== Modern Python Syntax Challenge (EP45) ===\n")
    
    # Create sample data
    sample_file = "sample_data.csv"
    with open(sample_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'name', 'score'])
        writer.writeheader()
        for i in range(25):
            writer.writerow({'id': str(i), 'name': f'user_{i}', 'score': str(80 + i)})
    
    # Use the pipeline
    print("Processing data with modern syntax:\n")
    for row in read_csv_pipeline(sample_file, chunk_size=10):
        print(f"  → {row}")
    
    print("\n✅ Pipeline completed using:")
    print("   • TypeAlias")
    print("   • Keyword-only argument (*)")
    print("   • Walrus operator (:=)")
    print("   • ParamSpec decorator (bonus)")
