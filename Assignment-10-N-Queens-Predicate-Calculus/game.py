
from logic import is_safe, validate_board


def place_queen(queens, n, row, col):
    """
    Place a queen if the position is valid and safe.

    Returns (True, message) if successful,
    otherwise (False, error_message).
    """

    if not (0 <= row < n and 0 <= col < n):
        return False, "Position is outside the board."

    if row in queens:
        return False, "A queen is already placed in this row."

    if not is_safe(queens, row, col):
        return False, "Unsafe position! A queen attacks this square."

    queens[row] = col
    return True, "Queen placed successfully."


def check_win(queens, n):
    """Return True if exactly n safe queens are placed."""
    return len(queens) == n and validate_board(queens, n)