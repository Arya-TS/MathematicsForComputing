
from solver import solve_n_queens


def get_hint(queens, n):
    """
    Return a safe next position as (row, column).
    Return None if no completion is possible.
    """

    solution = solve_n_queens(n, fixed_queens=queens)

    if solution is None:
        return None

    # Prefer the first empty row
    for row in range(n):
        if row not in queens:
            return row, solution[row]

    # All rows are occupied
    return None