def validate_board(queens, n=None):
    """
    Validate a partial or complete board.

    queens: dictionary {row: column}
    n: optional board size

    Returns True if every queen is within bounds and
    no two queens attack each other.
    """

    if not isinstance(queens, dict):
        return False

    positions = list(queens.items())

    for row, col in positions:
        if not isinstance(row, int) or not isinstance(col, int):
            return False

        if isinstance(row, bool) or isinstance(col, bool):
            return False

        if row < 0 or col < 0:
            return False

        if n is not None and (row >= n or col >= n):
            return False

    for i in range(len(positions)):
        r1, c1 = positions[i]

        for j in range(i + 1, len(positions)):
            r2, c2 = positions[j]

            same_row = r1 == r2
            same_column = c1 == c2
            same_diagonal = abs(r1 - r2) == abs(c1 - c2)

            if same_row or same_column or same_diagonal:
                return False

    return True


def is_safe(queens, row, col, n=None):
    """Check whether a queen can be placed at (row, col)."""

    if not isinstance(row, int) or isinstance(row, bool):
        return False

    if not isinstance(col, int) or isinstance(col, bool):
        return False

    if row < 0 or col < 0:
        return False

    if n is not None and (row >= n or col >= n):
        return False

    if row in queens:
        return False

    proposed = dict(queens)
    proposed[row] = col

    return validate_board(proposed, n)


def predicate_calculus_constraints(queens, n=None):
    """Named entry point for checking the logical constraints."""
    return validate_board(queens, n)