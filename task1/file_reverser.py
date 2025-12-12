# Task: Reverse the text on each line of a file and save it to a new file.

# Instructions:
# - get the file name from the user
# - Open the original file and read each line.
# - Reverse the text of each line word by word -> 'hello my name is george' -> 'george is name my hello'
# - Write the reversed lines into a new file - the output file name should be the input filename + _reverse.txt
# for example: 'story.txt' -> 'story.txt_reverse.txt'

import os
from pathlib import Path

def reverse_line_words(line):
    has_newline = line.endswith('\n')
    line_content = line.rstrip('\n')

    words = line_content.split()

    reversed_words = ' '.join(reversed(words))

    if has_newline:
        return reversed_words + '\n'
    return reversed_words

def simple_file_reverser():
    print("=" * 60)
    print("FILE REVERSER - Simple Version")
    print("=" * 60)
    
    filename = input("Enter the filename to process: ").strip()
    
    if not os.path.exists(filename):
        print(f"\nERROR: File '{filename}' not found.")
        print("\nAvailable text files in current directory:")
        text_files = [f for f in os.listdir('.') if f.endswith('.txt')]
        for file in text_files:
            print(f"  - {file}")
        return
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        reversed_lines = []
        for line in lines:
            reversed_line = reverse_line_words(line)
            reversed_lines.append(reversed_line)

        output_filename = f"{filename}_reverse.txt"

        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.writelines(reversed_lines)

        print(f"\nSUCCESS: Processed {len(lines)} lines.")
        print(f"Original file: {filename}")
        print(f"Output file: {output_filename}")
        
        print("\nSample of reversed lines (first 5):")
        print("-" * 40)
        for i in range(min(5, len(lines))):
            original_line = lines[i].rstrip('\n')
            reversed_line = reversed_lines[i].rstrip('\n')
            print(f"Original line {i+1}: {original_line}")
            print(f"Reversed line {i+1}: {reversed_line}")
            print()
            
    except UnicodeDecodeError:
        print(f"\nERROR: Cannot read '{filename}' as a text file.")
        print("The file may be binary or use a different encoding.")
    except Exception as e:
        print(f"\nERROR: An error occurred: {e}")

def enhanced_file_reverser():
    print("=" * 60)
    print("FILE REVERSER - Enhanced Version")
    print("=" * 60)
    
    filename = input("Enter the filename to process: ").strip()
    
    if not os.path.exists(filename):
        print(f"\nERROR: File '{filename}' not found.")
        return
    
    try:
  
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            file.seek(0)
            lines = file.readlines()
        
        reversed_lines = []
        line_stats = []
        
        for i, line in enumerate(lines, 1):
            original_line = line.rstrip('\n')
            reversed_line = reverse_line_words(line).rstrip('\n')

            original_word_count = len(original_line.split())
            reversed_word_count = len(reversed_line.split())
            
            reversed_lines.append(reverse_line_words(line))
            line_stats.append({
                'line_num': i,
                'original': original_line,
                'reversed': reversed_line,
                'original_words': original_word_count,
                'reversed_words': reversed_word_count
            })

        output_filename = f"{filename}_reverse.txt"

        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.writelines(reversed_lines)

        total_lines = len(lines)
        total_words_original = sum(stat['original_words'] for stat in line_stats)
        total_words_reversed = sum(stat['reversed_words'] for stat in line_stats)

        print(f"\nSUCCESS: File processed successfully!")
        print(f"Original file: {filename}")
        print(f"Output file: {output_filename}")
        print(f"Total lines processed: {total_lines}")
        print(f"Total words (original): {total_words_original}")
        print(f"Total words (reversed): {total_words_reversed}")

        print("\nDetailed sample (first 3 lines):")
        print("-" * 50)
        for i in range(min(3, len(line_stats))):
            stat = line_stats[i]
            print(f"Line {stat['line_num']}:")
            print(f"  Original: '{stat['original']}'")
            print(f"  Reversed: '{stat['reversed']}'")
            print(f"  Words: {stat['original_words']} -> {stat['reversed_words']}")
            print()

        mismatched = [stat for stat in line_stats if stat['original_words'] != stat['reversed_words']]
        if mismatched:
            print(f"Warning: {len(mismatched)} lines had word count differences after reversal.")

        report_filename = f"{filename}_reversal_report.txt"
        with open(report_filename, 'w', encoding='utf-8') as report_file:
            report_file.write("FILE REVERSAL REPORT\n")
            report_file.write("=" * 60 + "\n\n")
            report_file.write(f"Original file: {filename}\n")
            report_file.write(f"Output file: {output_filename}\n")
            report_file.write(f"Total lines: {total_lines}\n")
            report_file.write(f"Total words (original): {total_words_original}\n")
            report_file.write(f"Total words (reversed): {total_words_reversed}\n\n")
            
            report_file.write("LINE-BY-LINE ANALYSIS:\n")
            report_file.write("-" * 60 + "\n")
            for stat in line_stats:
                report_file.write(f"Line {stat['line_num']}:\n")
                report_file.write(f"  Original: {stat['original']}\n")
                report_file.write(f"  Reversed: {stat['reversed']}\n")
                report_file.write(f"  Word count: {stat['original_words']}\n")
                report_file.write("-" * 40 + "\n")
        
        print(f"Detailed report saved to: {report_filename}")
            
    except Exception as e:
        print(f"\nERROR: {e}")

def process_specific_files():
    """
    Process the specific text files provided in the assignment.
    """
    print("=" * 60)
    print("PROCESS SPECIFIC TEXT FILES")
    print("=" * 60)

    specific_files = [
        "spooky_story.txt",
        "giraffe_facts.txt",
        "capybara_facts.txt"
    ]

    available_files = []
    for filename in specific_files:
        if os.path.exists(filename):
            available_files.append(filename)
            print(f"✓ {filename} - Found")
        else:
            print(f"✗ {filename} - Not found")
    
    if not available_files:
        print("\nNo specific files found to process.")
        return
    
    print("\nWhich file would you like to process?")
    for i, filename in enumerate(available_files, 1):
        print(f"{i}. {filename}")
    
    try:
        choice = int(input(f"\nEnter your choice (1-{len(available_files)}): "))
        if 1 <= choice <= len(available_files):
            filename = available_files[choice-1]
            process_single_file(filename)
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid number.")

def process_single_file(filename):
    print(f"\nProcessing file: {filename}")
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        reversed_lines = []
        for line in lines:
            reversed_lines.append(reverse_line_words(line))

        output_filename = f"{filename}_reverse.txt"

        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.writelines(reversed_lines)
        
        print(f"SUCCESS: Created {output_filename}")
        print(f"Processed {len(lines)} lines")
        
        print("\nInteresting statistics:")
        print("-" * 40)
        
        longest_line = max(lines, key=lambda x: len(x.split()))
        longest_line_words = len(longest_line.split())
        print(f"Longest line has {longest_line_words} words")
        
        empty_lines = sum(1 for line in lines if line.strip() == '')
        print(f"Empty lines: {empty_lines}")
        
        print("\nSample of reversed content (first 3 non-empty lines):")
        print("-" * 40)
        count = 0
        for i, line in enumerate(lines):
            if line.strip():
                original = line.rstrip('\n')
                reversed_line = reversed_lines[i].rstrip('\n')
                print(f"Original: {original[:80]}{'...' if len(original) > 80 else ''}")
                print(f"Reversed: {reversed_line[:80]}{'...' if len(reversed_line) > 80 else ''}")
                print()
                count += 1
                if count >= 3:
                    break
                    
    except Exception as e:
        print(f"ERROR processing {filename}: {e}")

def batch_process_files():
    print("=" * 60)
    print("BATCH PROCESS MULTIPLE FILES")
    print("=" * 60)
    
    files_input = input("Enter filenames to process (separated by commas or spaces): ").strip()
    
    if not files_input:
        print("No files specified.")
        return
    import re
    filenames = re.split(r'[,\s]+', files_input)
    filenames = [f.strip() for f in filenames if f.strip()]
    
    if not filenames:
        print("No valid filenames provided.")
        return
    successful = []
    failed = []
    
    for filename in filenames:
        if not os.path.exists(filename):
            print(f"\n✗ {filename}: File not found")
            failed.append(filename)
            continue
        
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            
            reversed_lines = [reverse_line_words(line) for line in lines]
            
            output_filename = f"{filename}_reverse.txt"
            
            with open(output_filename, 'w', encoding='utf-8') as output_file:
                output_file.writelines(reversed_lines)
            
            print(f"✓ {filename}: Successfully processed ({len(lines)} lines)")
            successful.append((filename, output_filename, len(lines)))
            
        except Exception as e:
            print(f"✗ {filename}: Error - {e}")
            failed.append(filename)

    print("\n" + "=" * 60)
    print("PROCESSING SUMMARY")
    print("=" * 60)
    print(f"Total files: {len(filenames)}")
    print(f"Successfully processed: {len(successful)}")
    print(f"Failed: {len(failed)}")
    
    if successful:
        print("\nSuccessfully processed files:")
        for orig, output, line_count in successful:
            print(f"  {orig} -> {output} ({line_count} lines)")

def demonstrate_example():
    print("=" * 60)
    print("DEMONSTRATION: How Line Reversal Works")
    print("=" * 60)
    
    example_lines = [
        "hello my name is george",
        "Python programming is fun",
        "The quick brown fox jumps over the lazy dog",
        "This is a test",
        ""
    ]
    
    print("Example lines and their reversed versions:")
    print("-" * 60)
    
    for i, line in enumerate(example_lines, 1):
        reversed_line = reverse_line_words(line + '\n').rstrip('\n')
        print(f"Line {i}:")
        print(f"  Original: '{line}'")
        print(f"  Reversed: '{reversed_line}'")
        print()
    
    print("As you can see, each line's words are reversed in order.")
    print("Empty lines remain empty in the output.")

def main_menu():
    while True:
        print("\n" + "=" * 60)
        print("FILE REVERSER - Main Menu")
        print("=" * 60)
        print("1. Simple file reverser (basic functionality)")
        print("2. Enhanced file reverser (with statistics)")
        print("3. Process specific text files (spooky_story.txt, etc.)")
        print("4. Batch process multiple files")
        print("5. View demonstration of how reversal works")
        print("6. Exit")
        print("-" * 40)
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            simple_file_reverser()
        elif choice == "2":
            enhanced_file_reverser()
        elif choice == "3":
            process_specific_files()
        elif choice == "4":
            batch_process_files()
        elif choice == "5":
            demonstrate_example()
        elif choice == "6":
            print("\nThank you for using File Reverser. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")
        
        input("\nPress Enter to continue...")

def basic_file_reverser():
    filename = input("Enter filename: ")    
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        reversed_lines = []
        for line in lines:
            words = line.strip().split()
            reversed_words = ' '.join(reversed(words))
            reversed_lines.append(reversed_words + '\n')
        
        output_filename = filename + '_reverse.txt'
        
        with open(output_filename, 'w') as output_file:
            output_file.writelines(reversed_lines)
        
        print(f"File reversed and saved as: {output_filename}")
        
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Welcome to File Reverser!")
    print("This program reverses the words on each line of a text file.")

    main_menu()
