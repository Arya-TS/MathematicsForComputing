
from logic import validate_board
from solver import solve_n_queens
from game import place_queen, check_win
from hints import get_hint
from timer import GameTimer


def display_board(queens, n):
    """Display the chessboard in the terminal."""

    print()
    print("   " + " ".join(str(c + 1) for c in range(n)))

    for row in range(n):
        line = []

        for col in range(n):
            if queens.get(row) == col:
                line.append("Q")
            else:
                line.append(".")

        print(f"{row + 1:2} " + " ".join(line))

    print()


def get_board_size():
    while True:
        try:
            n = int(input("Enter board size (1-13): "))

            if 1 <= n <= 13:
                return n

            print("Please enter a number between 1 and 13.")

        except ValueError:
            print("Please enter a valid whole number.")


def play_user_mode(n):
    queens = {}
    timer = GameTimer()
    timer.start()

    print("\nUSER MODE")
    print("Enter row and column numbers from 1 to", n)
    print("Type H for a hint or Q to quit.")

    while True:
        display_board(queens, n)

        if check_win(queens, n):
            timer.pause()
            print("🎉 YOU WON! All queens are safe!")
            print("Time taken:", timer.formatted_time())
            break

        command = input("Enter row, H, or Q: ").strip().lower()

        if command == "q":
            timer.pause()
            print("Game ended. Better luck next time!")
            print("Time played:", timer.formatted_time())
            break

        if command == "h":
            hint = get_hint(queens, n)

            if hint is None:
                print("No solution fits the current placements.")
            else:
                row, col = hint
                print(
                    f"Hint: try row {row + 1}, "
                    f"column {col + 1}."
                )
            continue

        try:
            row = int(command) - 1
            col = int(input("Enter column: ").strip()) - 1
        except ValueError:
            print("Please enter valid numbers.")
            continue

        success, message = place_queen(queens, n, row, col)
        print(message)

        if success and check_win(queens, n):
            display_board(queens, n)
            timer.pause()
            print("🎉 YOU WON! All queens are safe!")
            print("Time taken:", timer.formatted_time())
            break


def play_ai_mode(n):
    timer = GameTimer()
    timer.start()

    print("\nAI MODE")
    print("The AI is solving the puzzle using backtracking...")

    solution = solve_n_queens(n)

    timer.pause()

    if solution is None:
        print(f"No solution exists for N = {n}.")
        return

    display_board(solution, n)

    if check_win(solution, n):
        print("🤖 AI SOLVED THE PUZZLE!")
        print("Solution:", solution)
        print("Time taken:", timer.formatted_time())
    else:
        print("The solution failed validation.")


def main():
    print("=" * 35)
    print("       N-QUEENS PUZZLE")
    print("=" * 35)

    n = get_board_size()

    print("\nChoose a mode:")
    print("1. User mode")
    print("2. AI mode")

    mode = input("Enter 1 or 2: ").strip()

    if mode == "1":
        play_user_mode(n)
    elif mode == "2":
        play_ai_mode(n)
    else:
        print("Invalid choice. Please run the program again.")


if __name__ == "__main__":
    main()