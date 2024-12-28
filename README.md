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

- Python 3.7 or higher
- Google Chrome browser
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

## Usage

1. Place `answers.txt` in the same directory as the script.

2. Run the solver:
   ```bash
   python wordle_solver.py
   ```

3. Follow the on-screen prompts to input results (green, yellow, and gray feedback).

4. If automation is enabled, ensure `chromedriver.exe` is in the same directory, and the script will interact directly with the Wordle website.

## Example Workflow

1. The solver will suggest an initial guess (e.g., "CRANE").
2. Input feedback from Wordle (e.g., `C` is green, `R` is yellow, others are gray).
3. The solver will generate subsequent guesses based on the feedback.
4. Repeat until the correct word is found.

## Customization

- Update `answers.txt` to include additional words or remove uncommon ones.
- Modify the logic in the script to change guess priorities.

## Troubleshooting

- **ChromeDriver Issues**: Ensure `chromedriver.exe` is compatible with your installed version of Chrome.
- **Missing Dependencies**: Re-run `pip install selenium`.
- **Accuracy Issues**: Verify that `answers.txt` contains a complete and valid word list.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgments

- Inspired by the Wordle game by The New York Times.
