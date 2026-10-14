
# fopc.py
"""
First-Order Predicate Calculus specification for N-Queens.

Predicate:
    Queen(r, c): a queen occupies row r, column c.

The quantified formulas are grounded over the finite domain
{0, 1, ..., n-1} before being passed to Z3.
"""

from z3 import Bool, Solver, PbEq, And, Not


def build_fopc_constraints(n, fixed_queens=None):
    if not 1 <= n <= 13:
        raise ValueError("Board size must be between 1 and 13.")

    fixed_queens = dict(fixed_queens or {})

    for r, c in fixed_queens.items():
        if not (0 <= r < n and 0 <= c < n):
            raise ValueError("Fixed queen is outside the board.")

    solver = Solver()

    # Ground instances of the predicate Queen(r, c).
    Queen = [
        [Bool(f"Queen_{r}_{c}") for c in range(n)]
        for r in range(n)
    ]

    # FOPC: For every row r, there exists exactly one c
    # such that Queen(r, c).
    #
    # Existential quantification is grounded by considering
    # every possible column in the finite domain.
    for r in range(n):
        solver.add(
            PbEq([(Queen[r][c], 1) for c in range(n)], 1)
        )

    # FOPC: Two queens in the same column must be in the same row.
    # Since each row already has exactly one queen, forbid
    # any two different rows from choosing the same column.
    for r1 in range(n):
        for r2 in range(r1 + 1, n):
            for c in range(n):
                solver.add(
                    Not(And(Queen[r1][c], Queen[r2][c]))
                )

    # FOPC: Distinct rows cannot contain queens on the same diagonal.
    for r1 in range(n):
        for r2 in range(r1 + 1, n):
            for c1 in range(n):
                for c2 in range(n):
                    if abs(r1 - r2) == abs(c1 - c2):
                        solver.add(
                            Not(And(Queen[r1][c1], Queen[r2][c2]))
                        )

    # Facts supplied by the user: Queen(r, c).
    for r, c in fixed_queens.items():
        solver.add(Queen[r][c])

    return solver, Queen