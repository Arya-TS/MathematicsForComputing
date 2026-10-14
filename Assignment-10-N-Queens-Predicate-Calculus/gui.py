
import tkinter as tk
from tkinter import messagebox, simpledialog
import time

from logic import is_safe, validate_board
from solver import solve_n_queens
from game import check_win
from hints import get_hint


class NQueensApp:
    def __init__(self, root):
        self.root = root
        self.root.title("N-Queens Puzzle")
        self.root.geometry("750x800")
        self.root.minsize(500, 550)

        self.n = 8
        self.queens = {}
        self.mode = "User"
        self.dark_mode = False
        self.start_time = None
        self.elapsed_before_pause = 0
        self.running = False
        self.finished = False

        self.light_bg = "#F5F5F5"
        self.dark_bg = "#202124"

        self.build_interface()
        self.reset_game()
        self.update_clock()

    def build_interface(self):
        self.header = tk.Frame(self.root)
        self.header.pack(fill="x", padx=10, pady=10)

        tk.Label(
            self.header,
            text="N-QUEENS PUZZLE",
            font=("Arial", 20, "bold")
        ).pack(pady=5)

        controls = tk.Frame(self.root)
        controls.pack(fill="x", padx=10, pady=5)

        tk.Label(controls, text="Board size:").pack(side="left")

        self.size_var = tk.StringVar(value="8")
        self.size_box = tk.Spinbox(
            controls,
            from_=1,
            to=13,
            width=4,
            textvariable=self.size_var
        )
        self.size_box.pack(side="left", padx=5)

        tk.Button(
            controls,
            text="New Game",
            command=self.reset_game
        ).pack(side="left", padx=5)

        tk.Button(
            controls,
            text="Switch Theme",
            command=self.toggle_theme
        ).pack(side="left", padx=5)

        modes = tk.Frame(self.root)
        modes.pack(pady=5)

        tk.Button(
            modes,
            text="User Mode",
            command=lambda: self.change_mode("User")
        ).pack(side="left", padx=5)

        tk.Button(
            modes,
            text="AI Mode",
            command=lambda: self.change_mode("AI")
        ).pack(side="left", padx=5)

        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack(padx=10, pady=10, expand=True)

        actions = tk.Frame(self.root)
        actions.pack(pady=5)

        tk.Button(
            actions,
            text="Get Hint",
            command=self.show_hint
        ).pack(side="left", padx=5)

        tk.Button(
            actions,
            text="Solve with AI",
            command=self.solve_board
        ).pack(side="left", padx=5)

        tk.Button(
            actions,
            text="Clear Board",
            command=self.clear_board
        ).pack(side="left", padx=5)

        self.status = tk.Label(
            self.root,
            text="Click a square to place a queen.",
            font=("Arial", 11)
        )
        self.status.pack(pady=5)

        self.timer_label = tk.Label(
            self.root,
            text="Time: 00:00",
            font=("Arial", 12, "bold")
        )
        self.timer_label.pack(pady=5)

    def reset_game(self):
        try:
            n = int(self.size_var.get())
            if not 1 <= n <= 13:
                raise ValueError
        except ValueError:
            messagebox.showerror(
                "Invalid Size",
                "Choose a board size from 1 to 13."
            )
            return

        self.n = n
        self.queens = {}
        self.finished = False
        self.elapsed_before_pause = 0
        self.start_time = time.perf_counter()
        self.running = True

        self.draw_board()
        self.status.config(
            text="Click a square to place a queen."
        )

    def draw_board(self):
        for widget in self.board_frame.winfo_children():
            widget.destroy()

        self.board_buttons = []

        available_width = max(self.root.winfo_width() - 80, 320)
        cell_size = max(24, min(65, available_width // self.n))

        for row in range(self.n):
            button_row = []

            for col in range(self.n):
                is_light = (row + col) % 2 == 0

                if self.dark_mode:
                    color = "#D6D6D6" if is_light else "#555555"
                    fg = "#111111"
                else:
                    color = "#F0D9B5" if is_light else "#9B7653"
                    fg = "#111111"

                text = "♛" if self.queens.get(row) == col else ""

                button = tk.Button(
                    self.board_frame,
                    text=text,
                    width=2,
                    height=1,
                    font=("Arial", max(10, cell_size // 2), "bold"),
                    bg=color,
                    fg=fg,
                    activebackground="#90CAF9",
                    relief="flat",
                    command=lambda r=row, c=col:
                        self.handle_click(r, c)
                )

                button.grid(
                    row=row,
                    column=col,
                    sticky="nsew"
                )
                button.config(
                    width=max(2, cell_size // 12),
                    height=max(1, cell_size // 24)
                )
                button_row.append(button)

            self.board_buttons.append(button_row)

        for i in range(self.n):
            self.board_frame.grid_rowconfigure(i, weight=1)
            self.board_frame.grid_columnconfigure(i, weight=1)

    def handle_click(self, row, col):
        if self.finished:
            return

        if self.mode == "AI":
            self.status.config(
                text="AI mode is read-only. Switch to User Mode to play."
            )
            return

        if row in self.queens:
            if self.queens[row] == col:
                del self.queens[row]
                self.draw_board()
                self.status.config(text="Queen removed.")
            else:
                self.status.config(
                    text="This row already has a queen. Remove it first."
                )
            return

        if not is_safe(self.queens, row, col):
            self.status.config(
                text="Invalid move: another queen attacks this square."
            )
            return

        self.queens[row] = col
        self.draw_board()
        self.status.config(text="Queen placed successfully.")

        if check_win(self.queens, self.n):
            self.win_game("You Won!")

    def show_hint(self):
        if self.finished:
            return

        hint = get_hint(self.queens, self.n)

        if hint is None:
            self.status.config(
                text="No solution fits the current queen placements."
            )
            return

        row, col = hint
        self.status.config(
            text=f"Hint: try row {row + 1}, column {col + 1}."
        )

        self.board_buttons[row][col].config(
            bg="#FFD54F",
            activebackground="#FFD54F"
        )

    def solve_board(self):
        solution = solve_n_queens(self.n)

        if solution is None:
            messagebox.showinfo(
                "No Solution",
                f"No solution exists for N = {self.n}."
            )
            return

        self.queens = solution
        self.draw_board()
        self.win_game("AI Solved the Puzzle!")

    def clear_board(self):
        if self.finished:
            self.reset_game()
            return

        self.queens = {}
        self.draw_board()
        self.status.config(text="Board cleared.")

    def change_mode(self, mode):
        self.mode = mode

        if mode == "AI":
            self.solve_board()
        else:
            self.status.config(
                text="User mode: click squares to place queens."
            )

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode

        background = self.dark_bg if self.dark_mode else self.light_bg
        foreground = "#FFFFFF" if self.dark_mode else "#111111"

        self.root.configure(bg=background)

        for widget in self.root.winfo_children():
            if isinstance(widget, (tk.Frame, tk.Label)):
                try:
                    widget.configure(
                        bg=background,
                        fg=foreground
                    )
                except tk.TclError:
                    pass

        self.draw_board()

    def win_game(self, title):
        self.finished = True
        self.running = False

        elapsed = self.get_elapsed()
        minutes, seconds = divmod(elapsed, 60)

        self.status.config(text=title)

        messagebox.showinfo(
            title,
            f"Congratulations!\n\n"
            f"All {self.n} queens are safely placed.\n"
            f"Time: {minutes:02d}:{seconds:02d}"
        )

    def get_elapsed(self):
        elapsed = self.elapsed_before_pause

        if self.running and self.start_time is not None:
            elapsed += time.perf_counter() - self.start_time

        return int(elapsed)

    def update_clock(self):
        elapsed = self.get_elapsed()
        minutes, seconds = divmod(elapsed, 60)

        self.timer_label.config(
            text=f"Time: {minutes:02d}:{seconds:02d}"
        )

        self.root.after(1000, self.update_clock)


if __name__ == "__main__":
    root = tk.Tk()
    app = NQueensApp(root)
    root.mainloop()