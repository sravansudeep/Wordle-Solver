# Wordle Solver

A Python-based Wordle solver to help you crack the popular word-guessing game! This project uses a word list (`answers.txt`) and a Chrome WebDriver (`chromedriver.exe`) for automation and logic implementation.

## Features
- Efficiently narrows down possible answers using logic and constraints.
- Supports integration with Wordle's web interface for automated input.
- Simple and easy-to-use interface.

## Files Included
1. **Wordle Solver Script**
   - The core Python script that implements the solver logic.
2. **answers.txt**
   - A text file containing all possible Wordle answers.
3. **chromedriver.exe**
   - The Chrome WebDriver binary used for automating interaction with the Wordle web interface.

## Prerequisites

- ChromeDriver compatible with your Chrome version

## Installation

1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd wordle-solver
   ```

2. Install required Python packages:
   ```bash
   pip install selenium
   ```

3. Verify that `chromedriver.exe` matches your installed Chrome browser version. [Download ChromeDriver](https://sites.google.com/chromium.org/driver/) if needed.

## Before Running The Code

1. Place `answers.txt` in the same directory as the script.

2. Run the solver:
   ```bash
   python wordle_solver.py
   ```
3. If automation is enabled, ensure `chromedriver.exe` is in the same directory, and the script will interact directly with the Wordle website.

## How It Works

1. The solver will suggest an initial guess (e.g., "CRANE").
2. Input feedback from Wordle (e.g., `C` is green, `R` is yellow, others are gray).
3. The solver will generate subsequent guesses based on the feedback.
4. Repeat until the correct word is found.

## Acknowledgments

- Inspired by the Wordle game by The New York Times.
