# Task: Open a file and calculate the total number of lines, words, and characters.

# Instructions:
# - get the file name from the user
# - Read the file contents.
# - Count how many lines, words, and characters are in the file.
# - Print out the totals for each.

def analyze_file():
    print("=" * 50)
    print("TEXT FILE ANALYZER")
    print("=" * 50)
    
    # Get filename from user
    filename = input("Enter the filename to analyze (e.g., 'spooky_story.txt'): ").strip()
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        lines = content.split('\n')
        line_count = len(lines)
        
        words = content.split()
        word_count = len(words)

        char_count = len(content)

        char_count_no_whitespace = len(content.replace(' ', '').replace('\n', '').replace('\t', ''))
        
        print("\n" + "=" * 50)
        print(f"ANALYSIS RESULTS for '{filename}':")
        print("=" * 50)
        print(f"Lines: {line_count}")
        print(f"Words: {word_count}")
        print(f"Characters (including spaces): {char_count}")
        print(f"Characters (excluding whitespace): {char_count_no_whitespace}")
        
        print("\nAdditional Statistics:")
        print("-" * 30)
        
        if line_count > 0:
            avg_words_per_line = word_count / line_count
            print(f"Average words per line: {avg_words_per_line:.2f}")
        
        if word_count > 0:
            avg_chars_per_word = char_count_no_whitespace / word_count
            print(f"Average characters per word: {avg_chars_per_word:.2f}")
        
        import os
        if os.path.exists(filename):
            file_size = os.path.getsize(filename)
            print(f"File size: {file_size} bytes")
        
        print("\nSample of file content (first 3 lines):")
        print("-" * 30)
        for i, line in enumerate(lines[:3]):
            if line:
                display_line = line[:80] + "..." if len(line) > 80 else line
                print(f"Line {i+1}: {display_line}")
        
        if len(lines) > 3:
            print(f"... and {len(lines)-3} more lines")
            
    except FileNotFoundError:
        print(f"\nERROR: File '{filename}' not found.")
        print("Please make sure the file exists in the current directory.")
        print("\nAvailable text files in current directory:")
        import glob
        text_files = glob.glob("*.txt")
        if text_files:
            for file in text_files:
                print(f"  - {file}")
        else:
            print("  (No .txt files found)")
            
    except UnicodeDecodeError:
        print(f"\nERROR: Unable to read '{filename}' as a text file.")
        print("The file may be binary or use a different encoding.")
        
    except Exception as e:
        print(f"\nERROR: An unexpected error occurred: {e}")

def analyze_specific_files():
    """
    Optional function to analyze the specific text files provided
    (giraffe_facts.txt, spooky_story.txt, capybara_facts.txt)
    """
    print("\n" + "=" * 50)
    print("ANALYZE SPECIFIC FILES")
    print("=" * 50)
    
    files_to_analyze = [
        "giraffe_facts.txt",
        "spooky_story.txt", 
        "capybara_facts.txt"
    ]
    
    for filename in files_to_analyze:
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
            
            lines = content.split('\n')
            words = content.split()
            
            line_count = len(lines)
            word_count = len(words)
            char_count = len(content)
            
            print(f"\n{filename}:")
            print(f"  Lines: {line_count}")
            print(f"  Words: {word_count}")
            print(f"  Characters: {char_count}")
            
            # Calculate averages
            if line_count > 0 and word_count > 0:
                avg_words_per_line = word_count / line_count
                print(f"  Average words per line: {avg_words_per_line:.1f}")
                
        except FileNotFoundError:
            print(f"\n{filename}: File not found")
        except Exception as e:
            print(f"\n{filename}: Error - {e}")

def main():
    """
    Main program with menu options
    """
    while True:
        print("\n" + "=" * 50)
        print("TEXT FILE ANALYZER - MAIN MENU")
        print("=" * 50)
        print("1. Analyze any text file")
        print("2. Analyze specific provided files (giraffe_facts.txt, etc.)")
        print("3. Exit")
        print("-" * 30)
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == "1":
            analyze_file()
        elif choice == "2":
            analyze_specific_files()
        elif choice == "3":
            print("\nThank you for using Text File Analyzer. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")
        
        input("\nPress Enter to continue...")

# Alternative simple version (if you prefer just the basic functionality)
def simple_analyze_file():
    """
    Simplified version that just does what's asked in the instructions
    """
    filename = input("Enter the filename to analyze: ").strip()
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        lines = content.split('\n')
        words = content.split()
        
        line_count = len(lines)
        word_count = len(words)
        char_count = len(content)
        
        print(f"\nFile Analysis Results for '{filename}':")
        print(f"Number of lines: {line_count}")
        print(f"Number of words: {word_count}")
        print(f"Number of characters: {char_count}")
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Welcome to the Text File Analyzer!")
    print("This program will count lines, words, and characters in a text file.")

    main()
