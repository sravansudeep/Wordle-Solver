from selenium import webdriver # Open and control a browser
from selenium.webdriver.common.by import By # Locate elements
from selenium.webdriver.common.keys import Keys # Simulate key board inputs
from collections import defaultdict # To create defualt values in a dict
import time # Give some time for the program to load.
from selenium.webdriver.chrome.service import Service # Make chrome driver easier to implement
import random;

def load_dictionary(file_path):
    try:
        with open(file_path) as f:
            words = [line.strip().lower() for line in f if len(line.strip()) == 5] # CSP
        print(f"Loaded {len(words)} words from {file_path}.")
        return words
    except Exception as e:
        print(f"Error loading dictionary: {e}")
        return []

def evaluate_guess(guess, word, word_length=5):
    feedback = ['B'] * word_length  # Feedback length is 5, matching Wordle's guess length
    word_list = list(word)

    # Check for correct letters (Green)
    for i in range(word_length):
        if guess[i] == word_list[i]:
            feedback[i] = 'G'
            word_list[i] = None  # Mark the letter as used

    # Check for present letters (Yellow)
    for i in range(word_length):
        if feedback[i] == 'B' and guess[i] in word_list:
            feedback[i] = 'Y'
            word_list[word_list.index(guess[i])] = None  # Mark the letter as used

    return ''.join(feedback)

def filter_words_with_feedback(guesses, feedbacks, possible_words): #implements reinforcement learning
    filtered_words = []
    for word in possible_words:
        matches = True
        for i, guess in enumerate(guesses):
            feedback = evaluate_guess(guess, word)
            if feedback != feedbacks[i]:
                matches = False
                break
        if matches:
            filtered_words.append(word)
    return filtered_words

def select_best_guess(possible_words):
    if not possible_words:
        return None

    best_guess = None
    best_score = float('inf')

    for guess in possible_words:
        partitions = defaultdict(list)
        for word in possible_words:
            partitions[evaluate_guess(guess, word)].append(word)

        max_partition_size = max(len(part) for part in partitions.values()) # Takes the max for better results.
        if max_partition_size < best_score:
            best_score = max_partition_size
            best_guess = guess

    return best_guess

def wordle_selenium(answers):
    driver_path = r"chromedriver.exe"
    try:
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service)
    except Exception as e:
        print(f"Error initializing WebDriver. Ensure ChromeDriver is available: {e}")
        return

    driver.get("https://www.nytimes.com/games/wordle/index.html")
    
    time.sleep(5)  # Wait for the page to load

    # Initialize Variables
    possible_words = answers[:]
    guesses = []
    feedback = []
    # Get the HTML element <body>
    body = driver.find_element(By.TAG_NAME, 'body')

    for attempt in range(1, 7):
        if not possible_words: 
            print("No possible words left!")
            break
        
        if attempt == 1:
            guess = random.choice(possible_words)
        else:
            guess = select_best_guess(possible_words)
        
        if not guess:
            print("AI failed to make a valid guess.")
            break
        
        guesses.append(guess)
        
        # Simulate typing the guess
        body.send_keys(guess)
        body.send_keys(Keys.RETURN)
        
        time.sleep(3)  # Wait for the result to be processed

        try:
            row = driver.find_elements(By.CSS_SELECTOR, f'[aria-label="Row {attempt}"] div')
            feedback_colors = [tile.get_attribute("data-state") for tile in row]

        except Exception as e:
            print(f"Error retrieving feedback for attempt {attempt}: {e}")
            continue
        
        feedback_string = ''.join(
            'G' if color == 'correct' else 'Y' if color == 'present' else 'B' 
            for color in feedback_colors if color
        )
        
        print(f"Feedback for attempt {attempt}: {feedback_string}")
        feedback.append(feedback_string)
        print(feedback)

        if feedback_string == 'GGGGG':  # Word is guessed correctly
            print(f"AI guessed the word in {attempt} attempts: {guess}")
            break

        possible_words = filter_words_with_feedback(guesses, feedback, possible_words)
        print(f"Remaining possible words: {len(possible_words)}")

    else:
        print("AI failed to guess the word.")

    driver.quit()

# Load word list
answers_file = r"answers.txt" # Give File Path
answers = load_dictionary(answers_file)

# Run the AI-powered Selenium Wordle solver
if answers:
    wordle_selenium(answers)