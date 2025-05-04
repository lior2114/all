import tkinter as tk
from tkinter import ttk # Import ttk for themed widgets
import random
import time
from collections import Counter # For error tracking
import os # To check for word file

# --- Constants ---
HEBREW_WORD_FILE = "hebrew_words.txt"
ENGLISH_WORD_FILE = "english_words.txt" # Added English word file
MIN_WORDS_IN_LIST = 20 # Minimum words needed from file (reduced for flexibility)
TARGET_WORD_LIST_LENGTH = 200 # How long the list for the test should be

# --- Theme Colors ---
LIGHT_THEME = {
    "BG": '#F0F0F0',          # Light gray
    "FG": '#111111',          # Near black
    "TEXT_AREA_BG": '#FFFFFF', # White
    "TEXT_AREA_FG": '#AAAAAA', # Medium grey (Future words default)
    "TYPED_FG": '#333333',      # Dark grey/black
    "CURRENT_BG": '#FFFACD', # Lemon Chiffon
    "ERROR_FG": '#D8000C',      # Dark red
    "ERROR_BG": '#FFD2D2',      # Light red
    "FUTURE_FG": '#AAAAAA',     # Medium grey
    "RESULTS_WPM_FG": '#006400', # Dark green
    "RESULTS_ACC_FG": '#00008B', # Dark blue
    "RESULTS_ERR_FG": '#8B0000', # Dark red (for error count)
    "TIMER_FG": '#4682B4',      # Steel blue
    "BUTTON_BG": '#DDDDDD',     # Light grey for button (ttk might override)
    "BUTTON_FG": '#111111',
    "BUTTON_DISABLED_BG": '#CCCCCC',
    "BUTTON_DISABLED_FG": '#777777',
    "SETTINGS_LABEL_FG": '#CCCCCC',
}

DARK_THEME = {
    "BG": '#2E2E2E',          # Dark gray
    "FG": '#E0E0E0',          # Light gray
    "TEXT_AREA_BG": '#3B3B3B', # Slightly lighter dark gray
    "TEXT_AREA_FG": '#777777', # Darker grey (Future words default)
    "TYPED_FG": '#FFFFFF',      # White
    "CURRENT_BG": '#5A5A24', # Dark yellow/olive
    "ERROR_FG": '#FF8888',      # Light red
    "ERROR_BG": '#7A2E2E',      # Dark red background
    "FUTURE_FG": '#777777',     # Darker grey
    "RESULTS_WPM_FG": '#7FFF00', # Chartreuse (bright green)
    "RESULTS_ACC_FG": '#ADD8E6', # Light blue
    "RESULTS_ERR_FG": '#FFA07A', # Light salmon (for error count)
    "TIMER_FG": '#87CEEB',      # Sky blue
    "BUTTON_BG": '#555555',     # Medium dark gray
    "BUTTON_FG": '#E0E0E0',
    "BUTTON_DISABLED_BG": '#444444',
    "BUTTON_DISABLED_FG": '#999999',
    "SETTINGS_LABEL_FG": '#CCCCCC',
}

# --- Fonts ---
FONT_MAIN = ('Arial', 12)
FONT_TEXT_AREA = ('Arial', 18)
FONT_RESULTS = ('Arial', 14, 'bold')
FONT_TIMER = ('Arial', 14)
FONT_SETTINGS_LABEL = ('Arial', 11)
FONT_SETTINGS_WIDGET = ('Arial', 11)
FONT_ERROR_DETAIL = ('Arial', 10)

# Default language
DEFAULT_LANGUAGE = 'heb' # Can be 'heb' or 'eng'

# --- Word Loading ---
def load_words_from_file(filename, language_name):
    """Loads words from the specified file, one word per line."""
    if not os.path.exists(filename):
        print(f"Error: {language_name.capitalize()} word file '{filename}' not found.")
        # Fallback to a basic list
        if language_name == 'hebrew':
            return ["שגיאה", "קובץ", "מילים", "לא", "נמצא"]
        else:
            return ["Error", "word", "file", "not", "found"]
    try:
        # Specify encoding for English too, although utf-8 is often default
        encoding = 'utf-8' # Keep utf-8 for both
        with open(filename, 'r', encoding=encoding) as f:
            words = [line.strip() for line in f if line.strip()]
        if len(words) < MIN_WORDS_IN_LIST:
            print(f"Warning: {language_name.capitalize()} word file '{filename}' has fewer than {MIN_WORDS_IN_LIST} words.")
        print(f"Loaded {len(words)} {language_name} words from {filename}")
        return words
    except Exception as e:
        print(f"Error loading {language_name} word file '{filename}': {e}")
        if language_name == 'hebrew':
            return ["שגיאה", "בטעינת", "קובץ", "מילים"]
        else:
            return ["Error", "loading", "word", "file"]


# Load words once at the start
ALL_WORDS_HEB = load_words_from_file(HEBREW_WORD_FILE, "hebrew")
ALL_WORDS_ENG = load_words_from_file(ENGLISH_WORD_FILE, "english")


def filter_words_by_difficulty(words_to_filter, difficulty, language):
    """Filters the list of words based on the selected difficulty and language."""
    filtered_words = []
    print(f"[Filter] Received difficulty='{difficulty}', language='{language}', total words in pool={len(words_to_filter)}") # DEBUG
    
    # --- Hebrew Filtering Rules ---
    if language == 'heb':
        for word in words_to_filter:
            word_len = len(word)
            has_comma = ',' in word
            has_period = '.' in word
            has_punctuation = has_comma or has_period

            if difficulty == "קל":
                # 1-5 letters, no punctuation
                if 1 <= word_len <= 5 and not has_punctuation:
                    filtered_words.append(word)
            elif difficulty == "בינוני":
                # 5-7 letters, no punctuation
                if 5 <= word_len <= 7 and not has_punctuation:
                    filtered_words.append(word)
            elif difficulty == "קשה":
                # 7-12 letters, must have punctuation (comma or period)
                if 7 <= word_len <= 12 and has_punctuation:
                    filtered_words.append(word)

    # --- English Filtering Rules (Simplified Example) ---
    elif language == 'eng':
         for word in words_to_filter:
            word_len = len(word)
            has_upper = any(c.isupper() for c in word)
            has_comma = ',' in word
            has_period = '.' in word
            has_punctuation = has_comma or has_period

            if difficulty == "Easy": # קל
                # 1-5 letters, no uppercase, no punctuation
                if 1 <= word_len <= 5 and not has_upper and not has_punctuation:
                    filtered_words.append(word)
            elif difficulty == "Medium": # בינוני
                # 1-7 letters, must have uppercase, no punctuation
                if 1 <= word_len <= 7 and has_upper and not has_punctuation:
                    filtered_words.append(word)
            elif difficulty == "Hard": # קשה
                # 5-8 letters, must have uppercase, must have punctuation (comma or period)
                if 5 <= word_len <= 8 and has_upper and has_punctuation:
                    filtered_words.append(word)

    if not filtered_words:
        print(f"Warning: No words found matching difficulty '{difficulty}' for {language}. Using all {language} words as fallback.")
        return words_to_filter # Fallback to all words if filter yields nothing

    print(f"[Filter] Filtered {language} words for difficulty '{difficulty}': {len(filtered_words)}") # DEBUG
    return filtered_words

# --- Global Variables ---
selected_time = 60
selected_difficulty = "קל" # Default difficulty
current_language = DEFAULT_LANGUAGE # Added language tracker
word_list = []
words_typed_count = 0
correct_chars = 0
total_chars_typed = 0
error_count = 0
mistyped_chars_counter = Counter()
timer_running = False
current_word_is_error = False
timer_id = None
start_time = 0
current_theme = 'light'
# --- Text Strings for UI (for easy translation/language switching) ---
UI_TEXT = {
    'heb': {
        'title': "בדיקת מהירות הקלדה בעברית",
        'toggle_lang': "Switch to English",
        'toggle_theme_dark': "🌙 מצב כהה",
        'toggle_theme_light': "💡 מצב בהיר",
        'custom_time': ":מותאם",
        'fixed_time': ":זמן קבוע",
        'difficulty': ":רמת קושי",
        'difficulty_options': ["קל", "בינוני", "קשה"],
        'start_prompt': "לחץ על 'התחל בדיקה' כדי להתחיל...",
        'no_words_error': "שגיאה: לא נטענו מילים.",
        'no_words_for_difficulty': "אין מילים זמינות לרמת קושי '{}'. נסה רמה אחרת.",
        'test_finished': "הבדיקה הסתיימה!",
        'test_stopped': "הבדיקה הופסקה.",
        'time_left': "זמן נותר: {} שניות",
        'time_up': "זמן נותר: 0 שניות",
        'wpm_label': "מהירות נטו: {:.1f} WPM",
        'acc_label': "דיוק: {:.1f}%",
        'err_label': "שגיאות: {}",
        'common_errors': "טעויות נפוצות: {}",
        'start_button': "התחל בדיקה",
        'stop_button': "עצור",
        'current_word_search_fail': "Warning: Could not find word '{}' for tagging (Hebrew).",
    },
    'eng': {
        'title': "English Typing Speed Test",
        'toggle_lang': "עבור לעברית",
        'toggle_theme_dark': "🌙 Dark Mode",
        'toggle_theme_light': "💡 Light Mode",
        'custom_time': "Custom:",
        'fixed_time': "Time:",
        'difficulty': "Difficulty:",
        'difficulty_options': ["Easy", "Medium", "Hard"],
        'start_prompt': "Press 'Start Test' to begin...",
        'no_words_error': "Error: No words loaded.",
        'no_words_for_difficulty': "No words available for difficulty '{}'. Try another level.",
        'test_finished': "Test Finished!",
        'test_stopped': "Test Stopped.",
        'time_left': "Time Left: {} seconds",
        'time_up': "Time Left: 0 seconds",
        'wpm_label': "Net WPM: {:.1f}",
        'acc_label': "Accuracy: {:.1f}%",
        'err_label': "Errors: {}",
        'common_errors': "Common Errors: {}",
        'start_button': "Start Test",
        'stop_button': "Stop",
        'current_word_search_fail': "Warning: Could not find word '{}' for tagging (English).",
    }
}


# --- Functions ---

def get_test_words(difficulty, language):
    """Filters, shuffles, and extends the loaded words for a new test run based on difficulty and language."""
    global ALL_WORDS_HEB, ALL_WORDS_ENG
    print(f"[Get Test Words] Received difficulty='{difficulty}', language='{language}'") # DEBUG
    base_word_pool = ALL_WORDS_HEB if language == 'heb' else ALL_WORDS_ENG

    if not base_word_pool:
        return ["אין", "מילים"] if language == 'heb' else ["No", "words"]

    # Filter words first based on language and difficulty
    base_words = filter_words_by_difficulty(base_word_pool, difficulty, language)

    if not base_words:
         return ["אין", "מילים", "לרמה", "זו"] if language == 'heb' else ["No", "words", "for", "level"]

    random.shuffle(base_words)

    extended_list = base_words[:]
    # Ensure list is long enough, repeat shuffled base words if needed
    base_len = len(base_words)
    while len(extended_list) < TARGET_WORD_LIST_LENGTH and base_len > 0:
        # Shuffle only the original filtered words for repetition
        shuffled_copy = base_words[:]
        random.shuffle(shuffled_copy)
        extended_list.extend(shuffled_copy)

    return extended_list[:TARGET_WORD_LIST_LENGTH]

def get_target_word():
    """Gets the current target word."""
    if not word_list:
        return ""
    return word_list[words_typed_count % len(word_list)]

def update_word_display():
    """Updates the display area using Labels within a Frame."""
    global current_language, word_list, words_typed_count, current_word_is_error
    theme_colors = LIGHT_THEME if current_theme == 'light' else DARK_THEME
    texts = UI_TEXT[current_language]

    # Clear previous labels from the frame
    for widget in word_display_frame.winfo_children():
        widget.destroy()

    # Determine packing side based on language
    pack_side = tk.RIGHT if current_language == 'heb' else tk.LEFT

    # Display current state message if needed (using a single label)
    current_state_message = None
    all_words_available = ALL_WORDS_HEB if current_language == 'heb' else ALL_WORDS_ENG

    if not timer_running and not word_list:
        if not all_words_available:
            current_state_message = texts['no_words_error']
        elif not filter_words_by_difficulty(all_words_available, selected_difficulty, current_language):
            current_state_message = texts['no_words_for_difficulty'].format(selected_difficulty)
        else:
            current_state_message = texts['start_prompt']
    elif not timer_running and word_list:
        if result_label['text'] or error_label['text']:
            current_state_message = texts['test_finished']
        else:
            current_state_message = texts['test_stopped']

    if current_state_message:
        # Use a single label centered in the frame for messages
        msg_label = ttk.Label(word_display_frame, text=current_state_message, style='Word.TLabel', anchor=tk.CENTER)
        # Configure the base Word.TLabel style temporarily for the message
        style.configure('Word.TLabel', foreground=theme_colors["FG"])
        msg_label.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        # Reset Word.TLabel style after use (important!)
        style.configure('Word.TLabel', foreground=theme_colors["FUTURE_FG"]) # Reset to future/default color
        return
    elif not word_list:
        return # Nothing to display

    # --- Display words using Labels --- #
    display_window_before = 3 # Adjust as needed for Label layout
    display_window_after = 10 # Adjust as needed for Label layout
    current_word_idx = words_typed_count

    # Adjust window slightly to keep current word centered better
    start_index = max(0, current_word_idx - display_window_before)
    end_index = min(len(word_list), current_word_idx + display_window_after)

    # Recalculate start_index if near the end, to show more context
    if len(word_list) - current_word_idx < display_window_after:
        start_index = max(0, len(word_list) - (display_window_before + display_window_after))
        end_index = len(word_list)

    for i in range(start_index, end_index):
        word = word_list[i]
        label_style = 'Word.TLabel' # Base style

        if i < current_word_idx:
            label_style = 'Typed.' + label_style
        elif i == current_word_idx:
            if current_word_is_error:
                label_style = 'Error.' + label_style
            else:
                if current_language == 'heb':
                    label_style = 'CurrentHeb.' + label_style # Bold for Hebrew
                else:
                    label_style = 'Current.' + label_style # Background for English
        else: # i > current_word_idx
            label_style = 'Future.' + label_style

        label = ttk.Label(word_display_frame, text=word, style=label_style)
        label.pack(side=pack_side, padx=2) # Pack labels side-by-side

def start_test():
    """Starts the typing test based on current language and settings."""
    global timer_running, word_list, words_typed_count, correct_chars, total_chars_typed, error_count, mistyped_chars_counter, start_time, selected_difficulty, selected_time, timer_id, current_word_is_error, current_language

    if timer_running:
        return

    # --- Get Time Setting --- #
    custom_time_str = custom_time_var.get().strip()
    valid_custom_time = False
    if custom_time_str:
        try:
            custom_time_val = int(custom_time_str)
            if custom_time_val > 0:
                selected_time = custom_time_val
                valid_custom_time = True
                # Check if custom time matches a predefined option
                time_str = str(custom_time_val)
                if time_str in time_options:
                    time_var.set(time_str)
                else:
                    time_var.set("") # Clear predefined if custom doesn't match
            else:
                # Invalid custom time (e.g., 0 or negative)
                custom_time_var.set("")
                # Fallback to default predefined if current selection is empty
                if not time_var.get(): time_var.set("60")
        except ValueError:
             custom_time_var.set("")
             if not time_var.get(): time_var.set("60")

    # If custom time wasn't valid or entered, use the predefined selection
    if not valid_custom_time:
        try:
            selected_time = int(time_var.get()) # Get from dropdown
            if selected_time <= 0: selected_time = 60 # Safety check
        except ValueError:
            selected_time = 60 # Default if dropdown is somehow invalid
            time_var.set("60")
        custom_time_var.set("") # Clear custom field

    # Get difficulty (already updated by UI if changed)
    old_selected_difficulty = selected_difficulty # Store old for comparison
    selected_difficulty = difficulty_var.get()
    print(f"[Start Test] Difficulty selected: '{selected_difficulty}' (was '{old_selected_difficulty}')") # DEBUG

    # Reset state
    timer_running = True
    current_word_is_error = False
    words_typed_count = 0
    correct_chars = 0
    total_chars_typed = 0
    error_count = 0
    mistyped_chars_counter = Counter()
    # Get words for selected language and difficulty
    word_list = get_test_words(selected_difficulty, current_language)

    # Check if word_list is actually populated
    if not word_list:
        print(f"Error: Could not generate word list for lang='{current_language}', difficulty='{selected_difficulty}'. Aborting start.")
        update_word_display() # Show the 'no words available' message
        timer_running = False
        # Re-enable settings immediately
        custom_time_entry.config(state=tk.NORMAL)
        time_menu.config(state=tk.NORMAL)
        difficulty_menu.config(state=tk.NORMAL)
        start_button.config(state=tk.NORMAL)
        stop_button.config(state=tk.DISABLED)
        theme_toggle_button.config(state=tk.NORMAL)
        language_toggle_button.config(state=tk.NORMAL) # Also re-enable language toggle
        return # Stop execution

    result_label.config(text="")
    accuracy_label.config(text="")
    error_label.config(text="")
    error_details_label.config(text="")
    input_entry.delete(0, tk.END)
    input_entry.config(state=tk.NORMAL)
    input_entry.focus_set()

    # Disable settings & Start, Enable Stop
    custom_time_entry.config(state=tk.DISABLED)
    time_menu.config(state=tk.DISABLED)
    difficulty_menu.config(state=tk.DISABLED)
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)
    theme_toggle_button.config(state=tk.DISABLED)
    language_toggle_button.config(state=tk.DISABLED) # Disable language toggle during test

    update_word_display()
    start_time = time.time()
    update_timer() # Start the timer loop

def update_timer():
    """Updates the timer display every second."""
    global timer_id, timer_running, current_language
    if not timer_running:
        return
    elapsed_time = time.time() - start_time
    remaining_time = max(0, selected_time - int(elapsed_time))
    theme_colors = LIGHT_THEME if current_theme == 'light' else DARK_THEME
    texts = UI_TEXT[current_language]
    timer_label.config(text=texts['time_left'].format(remaining_time), foreground=theme_colors["TIMER_FG"])

    if remaining_time > 0:
        # Ensure timer_id is managed correctly
        if timer_id:
            root.after_cancel(timer_id) # Cancel previous if exists
        timer_id = root.after(1000, update_timer)
    else:
        timer_label.config(text=texts['time_up'])
        end_test()

def end_test():
    """Ends the test, calculates results, displays them, and re-enables controls."""
    global timer_running, timer_id, start_time, current_language # Added start_time and current_language here
    was_running = timer_running
    timer_running = False
    if timer_id:
        root.after_cancel(timer_id)
        timer_id = None

    input_entry.config(state=tk.DISABLED)
    texts = UI_TEXT[current_language]

    # --- Calculate and Display Results --- #
    results_calculated = False
    if was_running and start_time > 0 and (total_chars_typed > 0 or error_count > 0):
        actual_elapsed_seconds = time.time() - start_time
        calc_minutes = actual_elapsed_seconds / 60.0 if actual_elapsed_seconds > 0 else (1/60.0) # Min 1 sec duration for calc

        net_wpm = (correct_chars / 5) / calc_minutes if calc_minutes > 0 else 0
        accuracy = (correct_chars / total_chars_typed) * 100 if total_chars_typed > 0 else 0
        results_calculated = True

        theme_colors = LIGHT_THEME if current_theme == 'light' else DARK_THEME
        result_label.config(text=texts['wpm_label'].format(net_wpm), foreground=theme_colors["RESULTS_WPM_FG"])
        accuracy_label.config(text=texts['acc_label'].format(accuracy), foreground=theme_colors["RESULTS_ACC_FG"])
        error_label.config(text=texts['err_label'].format(error_count), foreground=theme_colors["RESULTS_ERR_FG"])

        if mistyped_chars_counter:
            most_common_errors = mistyped_chars_counter.most_common(5)
            error_details_str = texts['common_errors'].format(
                ", ".join([f"'{char}' ({count})" for char, count in most_common_errors])
            )
            error_details_label.config(text=error_details_str)
        else:
            error_details_label.config(text="")
    else:
        # Clear results if test wasn't really run or stopped early
        result_label.config(text="")
        accuracy_label.config(text="")
        error_label.config(text="")
        error_details_label.config(text="")

    # --- Update UI State --- #
    custom_time_entry.config(state=tk.NORMAL)
    time_menu.config(state=tk.NORMAL)
    difficulty_menu.config(state=tk.NORMAL)
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)
    theme_toggle_button.config(state=tk.NORMAL)
    language_toggle_button.config(state=tk.NORMAL) # Re-enable language toggle

    start_time = 0

    update_word_display() # Update display AFTER results are set

def check_word(event):
    """Checks the typed word, tracks errors, and updates display."""
    global words_typed_count, correct_chars, total_chars_typed, error_count, mistyped_chars_counter, timer_running, current_word_is_error

    if not timer_running:
        return

    typed_word = input_entry.get().strip()
    target_word = get_target_word()

    # Don't clear if input is empty - allows correcting mid-word if desired (future feature?)
    # For now, clear on space press as before.
    input_entry.delete(0, tk.END)

    if not typed_word:
        # Allow skipping a word maybe? Or just ignore empty space press?
        # Current behavior: Ignore empty space press.
        return

    total_chars_typed += len(typed_word) + 1 # Count space

    if typed_word == target_word:
        if not current_word_is_error:
            correct_chars += len(target_word) + 1 # Add length of word + space
        current_word_is_error = False # Corrected or was correct
        words_typed_count += 1
    else:
        # Handle error only if it wasn't already marked as an error
        if not current_word_is_error:
            error_count += 1
            current_word_is_error = True
            # Track mistyped characters more accurately
            len_typed = len(typed_word)
            len_target = len(target_word)
            for i in range(len_typed): # Only count mistyped chars that were actually typed
                target_char = target_word[i] if i < len_target else None
                if typed_word[i] != target_char:
                    mistyped_chars_counter[typed_word[i]] += 1
        # Don't advance word count on error
        # words_typed_count += 1 # This would advance on error, remove

    # Update display immediately after checking
    update_word_display()

def toggle_theme():
    """Switches between light and dark themes."""
    global current_theme
    texts = UI_TEXT[current_language]
    if current_theme == 'light':
        current_theme = 'dark'
        theme_toggle_button.config(text=texts['toggle_theme_light']) # Show light option
    else:
        current_theme = 'light'
        theme_toggle_button.config(text=texts['toggle_theme_dark']) # Show dark option
    apply_theme()

def apply_theme():
    """Applies the currently selected theme colors and styles, considering language."""
    global current_language
    theme_colors = LIGHT_THEME if current_theme == 'light' else DARK_THEME
    theme_name = 'vista' if root.tk.call('tk', 'windowingsystem') == 'win32' else 'clam'
    if current_theme == 'dark':
        try:
            style.theme_use('clam') # Clam theme often better for dark mode customization
        except tk.TclError:
             style.theme_use(theme_name) # Fallback if clam not available
    else:
         style.theme_use(theme_name)

    # --- Configure root and main frame ---
    root.config(bg=theme_colors["BG"])
    main_frame.config(style='TFrame') # Ensure frame uses the style
    style.configure('TFrame', background=theme_colors["BG"])

    # --- Configure ttk Styles ---
    style.configure('.', background=theme_colors["BG"], foreground=theme_colors["FG"], font=FONT_MAIN) # Apply base font here
    style.configure('TLabel', background=theme_colors["BG"], foreground=theme_colors["SETTINGS_LABEL_FG"], font=FONT_SETTINGS_LABEL) # Font for settings labels
    style.map('TButton',
              background=[('disabled', theme_colors["BUTTON_DISABLED_BG"]), ('active', theme_colors["BUTTON_BG"]), ('!disabled', theme_colors["BUTTON_BG"])],
              foreground=[('disabled', theme_colors["BUTTON_DISABLED_FG"]), ('!disabled', theme_colors["BUTTON_FG"])])
    style.configure('TMenubutton', background=theme_colors["BUTTON_BG"], foreground=theme_colors["BUTTON_FG"], arrowcolor=theme_colors["FG"], padding=5, font=FONT_SETTINGS_WIDGET) # Font for menu button text
    style.map('TMenubutton', background=[('active', theme_colors["BUTTON_BG"])])

    style.configure('TEntry', fieldbackground=theme_colors["TEXT_AREA_BG"], foreground=theme_colors["FG"], insertcolor=theme_colors["FG"], font=FONT_SETTINGS_WIDGET) # Font for custom time entry
    style.map('TEntry', background=[('disabled', theme_colors["BUTTON_DISABLED_BG"])])

    # Specific styles for results/timer etc.
    style.configure('Results.TLabel', font=FONT_RESULTS, background=theme_colors["BG"]) # Base style config
    style.configure('Timer.TLabel', font=FONT_TIMER, background=theme_colors["BG"], foreground=theme_colors["TIMER_FG"])
    style.configure('ErrorDetails.TLabel', font=FONT_ERROR_DETAIL, background=theme_colors["BG"], foreground=theme_colors["FG"])

    # --- Styles for Word Labels ---
    bold_font = (FONT_TEXT_AREA[0], FONT_TEXT_AREA[1], 'bold')
    # Ensure base Word.TLabel uses the text area background for seamless look
    style.configure('Word.TLabel', font=FONT_TEXT_AREA, padding=(2, 2), background=theme_colors["TEXT_AREA_BG"])
    style.configure('Typed.Word.TLabel', foreground=theme_colors["TYPED_FG"])
    style.configure('Future.Word.TLabel', foreground=theme_colors["FUTURE_FG"])
    # Ensure backgrounds match the frame background for non-highlighted states
    style.map('Typed.Word.TLabel', background=[('!active', theme_colors["TEXT_AREA_BG"])])
    style.map('Future.Word.TLabel', background=[('!active', theme_colors["TEXT_AREA_BG"])])

    style.configure('Current.Word.TLabel', background=theme_colors["CURRENT_BG"], foreground=theme_colors["TYPED_FG"])
    style.configure('CurrentHeb.Word.TLabel', font=bold_font, foreground=theme_colors["TYPED_FG"], background=theme_colors["TEXT_AREA_BG"])
    style.configure('Error.Word.TLabel', background=theme_colors["ERROR_BG"], foreground=theme_colors["ERROR_FG"])

    # Configure the frame that will hold the labels
    word_display_frame.config(style='WordFrame.TFrame')
    style.configure('WordFrame.TFrame', background=theme_colors["TEXT_AREA_BG"]) # Match old text area bg

    # --- Update Input Entry Justification ---
    text_justify = tk.RIGHT if current_language == 'heb' else tk.LEFT
    input_entry.config(justify=text_justify, font=FONT_TEXT_AREA) # Also set font here

    # --- Update Labels with specific foregrounds AND ensure style is applied ---
    result_label.config(foreground=theme_colors["RESULTS_WPM_FG"], style='Results.TLabel')
    accuracy_label.config(foreground=theme_colors["RESULTS_ACC_FG"], style='Results.TLabel')
    error_label.config(foreground=theme_colors["RESULTS_ERR_FG"], style='Results.TLabel')
    timer_label.config(foreground=theme_colors["TIMER_FG"], style='Timer.TLabel')
    error_details_label.config(style='ErrorDetails.TLabel')

    update_word_display() # Refresh display with new theme/language settings

def toggle_language():
    """Switches the application language between Hebrew and English."""
    global current_language, selected_difficulty, word_list, words_typed_count, correct_chars, total_chars_typed, error_count, mistyped_chars_counter, timer_running
    
    # Stop timer if running
    if timer_running:
        end_test() # End the current test gracefully

    # Switch language
    current_language = 'eng' if current_language == 'heb' else 'heb'
    texts = UI_TEXT[current_language]

    # Reset test state variables completely
    word_list = []
    words_typed_count = 0
    correct_chars = 0
    total_chars_typed = 0
    error_count = 0
    mistyped_chars_counter = Counter()
    current_word_is_error = False
    input_entry.delete(0, tk.END)
    input_entry.config(state=tk.DISABLED) # Disable until start
    result_label.config(text="")
    accuracy_label.config(text="")
    error_label.config(text="")
    error_details_label.config(text="")
    timer_label.config(text=texts['time_left'].format(selected_time)) # Reset timer display


    # --- Update UI Elements ---
    root.title(texts['title'])
    language_toggle_button.config(text=texts['toggle_lang'])
    # Update theme toggle button text based on new language and current theme
    theme_toggle_button.config(text=texts['toggle_theme_dark'] if current_theme == 'light' else texts['toggle_theme_light'])

    custom_time_label.config(text=texts['custom_time'])
    time_label.config(text=texts['fixed_time'])
    difficulty_label.config(text=texts['difficulty'])

    # Update Difficulty Dropdown
    difficulty_menu['menu'].delete(0, 'end') # Clear existing options
    new_options = texts['difficulty_options']
    for option in new_options:
        # Add command to update selected_difficulty when menu item is chosen
        difficulty_menu['menu'].add_command(label=option, command=lambda value=option: difficulty_var.set(value))
    difficulty_var.set(new_options[0]) # Set default difficulty for the new language
    selected_difficulty = new_options[0]


    start_button.config(text=texts['start_button'])
    stop_button.config(text=texts['stop_button'])

    # Ensure controls are in correct state (start enabled, stop disabled)
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)
    custom_time_entry.config(state=tk.NORMAL)
    time_menu.config(state=tk.NORMAL)
    difficulty_menu.config(state=tk.NORMAL)
    theme_toggle_button.config(state=tk.NORMAL)


    # Apply theme and update display (this handles text justification and colors)
    apply_theme()

# --- GUI Setup ---
root = tk.Tk()
# root.title("בדיקת מהירות הקלדה") # Initial title set in toggle_language
root.geometry("950x600")
# root.option_add('*Font', FONT_MAIN) # Set via style configuration now

# Style Configuration
style = ttk.Style()

# Main Frame
main_frame = ttk.Frame(root, padding="15 15 15 15")
main_frame.pack(expand=True, fill=tk.BOTH)

# --- Top Row: Settings, Theme Toggle, Language Toggle ---
top_frame = ttk.Frame(main_frame)
top_frame.pack(fill=tk.X, pady=(0, 15))

# Left side controls
left_controls_frame = ttk.Frame(top_frame)
left_controls_frame.pack(side=tk.LEFT, padx=10)

# Theme Toggle (now on left)
theme_toggle_button = ttk.Button(left_controls_frame, command=toggle_theme, width=15) # Width adjusted
theme_toggle_button.pack(side=tk.LEFT, padx=(0, 5))

# Language Toggle (new, on left)
language_toggle_button = ttk.Button(left_controls_frame, command=toggle_language, width=15) # Width adjusted
language_toggle_button.pack(side=tk.LEFT, padx=(5, 0))


# Settings Frame (on the right)
settings_frame = ttk.Frame(top_frame)
settings_frame.pack(side=tk.RIGHT)
# Configure columns for settings (flexible, might need adjustment based on label lengths)
settings_frame.columnconfigure((0, 1, 2, 3, 4, 5), weight=0, uniform="settings")
settings_frame.rowconfigure(0, weight=1)

# Custom Time (Rightmost setting)
custom_time_label = ttk.Label(settings_frame) # Text set in toggle_language
custom_time_label.grid(row=0, column=5, sticky=tk.W, padx=(2, 5))
custom_time_var = tk.StringVar(root)
custom_time_entry = ttk.Entry(settings_frame, textvariable=custom_time_var, width=5, justify=tk.CENTER)
custom_time_entry.grid(row=0, column=4, sticky=tk.E, pady=2, padx=(5, 2))

# Predefined Time (Left of Custom Time)
time_label = ttk.Label(settings_frame) # Text set in toggle_language
time_label.grid(row=0, column=3, sticky=tk.W, padx=(2, 5))
time_var = tk.StringVar(root)
time_options = ["30", "60", "120", "180"] # Keep numeric options
time_var.set("60")
def on_time_select(*args):
    custom_time_var.set("") # Clear custom if predefined selected
time_var.trace_add("write", on_time_select)
time_menu = ttk.OptionMenu(settings_frame, time_var, time_options[1], *time_options, style='TMenubutton')
time_menu.grid(row=0, column=2, sticky=tk.E, pady=2, padx=(5, 2))
# style.configure('Time.TMenubutton', width=5) # Use default TMenubutton style or adjust if needed
# time_menu.config(style='Time.TMenubutton')


# Difficulty Selection (Leftmost setting in this group)
difficulty_label = ttk.Label(settings_frame) # Text set in toggle_language
difficulty_label.grid(row=0, column=1, sticky=tk.W, padx=(2, 5))
difficulty_var = tk.StringVar(root)
# Initial options set later by toggle_language
difficulty_options_heb = UI_TEXT['heb']['difficulty_options']
difficulty_options_eng = UI_TEXT['eng']['difficulty_options']
# Set initial value based on DEFAULT_LANGUAGE
initial_difficulty_options = difficulty_options_heb if DEFAULT_LANGUAGE == 'heb' else difficulty_options_eng
difficulty_var.set(initial_difficulty_options[0])
selected_difficulty = initial_difficulty_options[0] # Sync global var

difficulty_menu = ttk.OptionMenu(settings_frame, difficulty_var, initial_difficulty_options[0], *initial_difficulty_options, style='TMenubutton')
difficulty_menu.grid(row=0, column=0, sticky=tk.E, pady=2, padx=(5, 2))
# style.configure('Difficulty.TMenubutton', width=8) # Adjust width as needed
# difficulty_menu.config(style='Difficulty.TMenubutton')


# --- Word Display Area ---
word_display_frame = ttk.Frame(main_frame, height=100, style='WordFrame.TFrame') # Use height similar to old Text widget
word_display_frame.pack(pady=10, fill=tk.X, padx=5)
word_display_frame.pack_propagate(False) # Prevent frame from shrinking to fit labels initially

# --- Input Entry ---
input_entry_frame = ttk.Frame(main_frame)
input_entry_frame.pack(pady=10)
input_entry = ttk.Entry(input_entry_frame, width=50) # Font/Justify set in apply_theme
input_entry.pack()
input_entry.bind("<space>", check_word)
input_entry.config(state=tk.DISABLED) # Start disabled

# --- Results Area Frame ---
results_area_frame = ttk.Frame(main_frame, padding="10 5 10 5")
results_area_frame.pack(fill=tk.X, pady=5)
results_area_frame.columnconfigure((0, 1, 2, 3), weight=1) # Allow labels to space out

# Results Labels (Pack Right to Left visually still makes sense)
timer_label = ttk.Label(results_area_frame, text="", style='Timer.TLabel')
timer_label.pack(side=tk.RIGHT, padx=15)

error_label = ttk.Label(results_area_frame, text="", style='Results.TLabel')
error_label.pack(side=tk.RIGHT, padx=15)

accuracy_label = ttk.Label(results_area_frame, text="", style='Results.TLabel')
accuracy_label.pack(side=tk.RIGHT, padx=15)

result_label = ttk.Label(results_area_frame, text="", style='Results.TLabel')
result_label.pack(side=tk.RIGHT, padx=15)


# Error Details Label (Below results)
error_details_label = ttk.Label(main_frame, text="", style='ErrorDetails.TLabel')
error_details_label.pack(pady=(0, 10))

# --- Buttons Frame ---
buttons_frame = ttk.Frame(main_frame)
buttons_frame.pack(pady=15)

# Pack order determines visual order (Rightmost first for RTL feel)
stop_button = ttk.Button(buttons_frame, command=end_test, style='TButton', state=tk.DISABLED, width=12)
stop_button.pack(side=tk.RIGHT, padx=10)

start_button = ttk.Button(buttons_frame, command=start_test, style='TButton', cursor="hand2", width=15)
start_button.pack(side=tk.RIGHT, padx=10)

# --- Initial Setup ---
toggle_language() # Call once to set the initial language UI based on DEFAULT_LANGUAGE
if DEFAULT_LANGUAGE == 'eng':
    toggle_language() # Call twice if starting in English to ensure correct state


root.mainloop()