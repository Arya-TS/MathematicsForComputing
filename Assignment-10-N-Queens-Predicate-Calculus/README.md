# N-Queens Puzzle Using First-Order Predicate Calculus

## Overview

This project implements the N-Queens puzzle using Python, Z3 constraint solving, and a Tkinter graphical user interface.

The objective is to place N queens on an N × N chessboard so that no two queens share the same row, column, or diagonal.

## Objectives

- Represent queen placement using the predicate `Queen(r, c)`.
- Express the N-Queens rules as logical constraints.
- Solve the constraints using the Z3 SMT solver.
- Provide an interactive graphical interface using Tkinter.
- Support board sizes from 1 to 13.
- Include user and AI modes, hints, a timer, and light/dark themes.

## Technologies Used

- Python
- Z3 Solver
- Tkinter
- First-Order Predicate Calculus

## Project Structure

- `fopc.py` — defines the logical constraints.
- `solver.py` — solves the N-Queens problem using Z3.
- `logic.py` — validates queen placements.
- `game.py` — checks whether the puzzle is solved.
- `hints.py` — provides hints to the user.
- `main.py` — runs the graphical application.
- `main.tex` — LaTeX source for the project presentation.
- `presentation.pdf` — compiled project presentation.
- `requirements.txt` — lists the required Python packages.

## Installation

1. Install Python 3.
2. Install the required dependency:

   `pip install -r requirements.txt`

3. Run the application:

   `python main.py`

Replace `main.py` in these instructions if your actual application file has a different name.

## Logical Model

`Queen(r, c)` means that a queen occupies row `r` and column `c`.

The constraints enforce exactly one queen per row and prevent queens from sharing columns or diagonals. The quantified rules are grounded over the finite board before being passed to Z3.

## Project Status

Academic project. Test the application in your environment before relying on its results.
