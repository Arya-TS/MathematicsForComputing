from z3 import sat, is_true
from fopc import build_fopc_constraints


def solve_n_queens(n, fixed_queens=None):
    solver, Queen = build_fopc_constraints(n, fixed_queens)

    result = solver.check()

    if result != sat:
        return None

    model = solver.model()
    solution = {}

    for r in range(n):
        for c in range(n):
            value = model.evaluate(
                Queen[r][c],
                model_completion=True
            )

            if is_true(value):
                solution[r] = c
                break

    if len(solution) != n:
        return None

    return solution