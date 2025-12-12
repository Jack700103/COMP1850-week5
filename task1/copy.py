# Task: Create an exact copy of a file by reading its content and writing it to a new file.


# Instructions:
# - get the file name from the user
# - Open the original file and read its content.
# - Create a new file, and write the same content into it - the output file should be the input file name + _copy.txt
# e.g. story.txt -> story.txt_copy.txt

# Tip: Consider which file modes will let you read and write text data.

import os
import hashlib

def copy_file_simple():
    print("=" * 60)
    print("FILE COPIER - Simple Version")
    print("=" * 60)
    
    filename = input("Enter the filename to copy: ").strip()
    
    if not os.path.exists(filename):
        print(f"\nERROR: File '{filename}' does not exist.")
        print("\nAvailable files in current directory:")
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        for file in files[:10]:
            print(f"  - {file}")
        if len(files) > 10:
            print(f"  ... and {len(files)-10} more files")
        return
    
    try:
        with open(filename, 'r', encoding='utf-8') as source_file:
            content = source_file.read()

        output_filename = f"{filename}_copy.txt"

        with open(output_filename, 'w', encoding='utf-8') as dest_file:
            dest_file.write(content)
        
        print(f"\nSUCCESS: File copied successfully!")
        print(f"Original: {filename}")
        print(f"Copy: {output_filename}")

        original_size = os.path.getsize(filename)
        copy_size = os.path.getsize(output_filename)
        print(f"\nOriginal file size: {original_size} bytes")
        print(f"Copy file size: {copy_size} bytes")

        if original_size == copy_size:
            print("Verification: File sizes match.")
        else:
            print("Warning: File sizes do not match!")
            
    except UnicodeDecodeError:
        print(f"\nERROR: Cannot read '{filename}' as a text file.")
        print("It might be a binary file. Try a different file.")
    except Exception as e:
        print(f"\nERROR: An error occurred: {e}")

def copy_file_with_verification():
    print("=" * 60)
    print("FILE COPIER - Enhanced Version with Verification")
    print("=" * 60)
    
    filename = input("Enter the filename to copy: ").strip()
    
    if not os.path.exists(filename):
        print(f"\nERROR: File '{filename}' does not exist.")
        return
    
    try:
        def get_file_hash(filepath):
            hash_md5 = hashlib.md5()
            with open(filepath, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_md5.update(chunk)
            return hash_md5.hexdigest()
        
        original_hash = get_file_hash(filename)
        print(f"Original file hash (MD5): {original_hash}")

        output_filename = f"{filename}_copy.txt"

        with open(filename, 'rb') as source_file:
            with open(output_filename, 'wb') as dest_file:
                chunk_size = 8192
                while True:
                    chunk = source_file.read(chunk_size)
                    if not chunk:
                        break
                    dest_file.write(chunk)
        
        print(f"\nFile copied: {output_filename}")
        copy_hash = get_file_hash(output_filename)
        print(f"Copy file hash (MD5): {copy_hash}")
        
        if original_hash == copy_hash:
            print("\n✓ SUCCESS: Copy is identical to original (verified by MD5 hash)")
        else:
            print("\n✗ ERROR: Copy does not match original!")
            
    except Exception as e:
        print(f"\nERROR: {e}")

def copy_multiple_files():
    print("=" * 60)
    print("FILE COPIER - Batch Copy Multiple Files")
    print("=" * 60)
    
    file_input = input("Enter filenames to copy (separated by commas or spaces): ").strip()
    
    import re
    filenames = re.split(r'[,\s]+', file_input)
    filenames = [f.strip() for f in filenames if f.strip()]
    
    if not filenames:
        print("No filenames provided.")
        return
    
    successful_copies = []
    failed_copies = []
    
    for filename in filenames:
        if not os.path.exists(filename):
            print(f"\n✗ '{filename}': File not found")
            failed_copies.append(filename)
            continue
        
        try:
            output_filename = f"{filename}_copy.txt"
            
            with open(filename, 'r', encoding='utf-8') as source_file:
                content = source_file.read()
            
            with open(output_filename, 'w', encoding='utf-8') as dest_file:
                dest_file.write(content)
            
            print(f"✓ '{filename}': Successfully copied to '{output_filename}'")
            successful_copies.append((filename, output_filename))
            
        except UnicodeDecodeError:
            try:
                output_filename = f"{filename}_copy.txt"
                
                with open(filename, 'rb') as source_file:
                    with open(output_filename, 'wb') as dest_file:
                        dest_file.write(source_file.read())
                
                print(f"✓ '{filename}': Successfully copied as binary")
                successful_copies.append((filename, output_filename))
                
            except Exception as e:
                print(f"✗ '{filename}': Error - {e}")
                failed_copies.append(filename)
        except Exception as e:
            print(f"✗ '{filename}': Error - {e}")
            failed_copies.append(filename)

    print("\n" + "=" * 60)
    print("COPY SUMMARY")
    print("=" * 60)
    print(f"Total files: {len(filenames)}")
    print(f"Successfully copied: {len(successful_copies)}")
    print(f"Failed: {len(failed_copies)}")
    
    if successful_copies:
        print("\nSuccessfully copied files:")
        for original, copy in successful_copies[:5]:
            print(f"  {original} -> {copy}")
        if len(successful_copies) > 5:
            print(f"  ... and {len(successful_copies)-5} more")

def copy_specific_files():
    print("=" * 60)
    print("FILE COPIER - Copy Specific Text Files")
    print("=" * 60)
    
    specific_files = [
        "spooky_story.txt",
        "giraffe_facts.txt", 
        "capybara_facts.txt"
    ]
    
    print("Available specific files to copy:")
    for i, filename in enumerate(specific_files, 1):
        exists = "✓" if os.path.exists(filename) else "✗"
        print(f"{i}. {exists} {filename}")
    
    print("\nWhich files would you like to copy?")
    print("Enter file numbers (e.g., '1,2,3') or 'all' for all files: ")
    choice = input("Your choice: ").strip().lower()
    
    files_to_copy = []
    
    if choice == 'all':
        files_to_copy = specific_files
    else:
        try:
            indices = [int(num.strip()) for num in choice.split(',') if num.strip()]
            for idx in indices:
                if 1 <= idx <= len(specific_files):
                    files_to_copy.append(specific_files[idx-1])
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")
            return
    
    if not files_to_copy:
        print("No files selected.")
        return
    
    for filename in files_to_copy:
        if not os.path.exists(filename):
            print(f"\n✗ '{filename}': File not found")
            continue
        
        try:
            output_filename = f"{filename}_copy.txt"
            
            with open(filename, 'r', encoding='utf-8') as source_file:
                content = source_file.read()
            
            with open(output_filename, 'w', encoding='utf-8') as dest_file:
                dest_file.write(content)
            
            lines = content.split('\n')
            words = content.split()
            
            print(f"\n✓ '{filename}': Successfully copied")
            print(f"   Output: {output_filename}")
            print(f"   Stats: {len(lines)} lines, {len(words)} words, {len(content)} characters")
            
        except Exception as e:
            print(f"\n✗ '{filename}': Error - {e}")

def main_menu():
    while True:
        print("\n" + "=" * 60)
        print("FILE COPIER - Main Menu")
        print("=" * 60)
        print("1. Simple file copy (text files only)")
        print("2. Enhanced copy with verification")
        print("3. Copy multiple files at once")
        print("4. Copy specific text files (spooky_story.txt, etc.)")
        print("5. Exit")
        print("-" * 40)
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            copy_file_simple()
        elif choice == "2":
            copy_file_with_verification()
        elif choice == "3":
            copy_multiple_files()
        elif choice == "4":
            copy_specific_files()
        elif choice == "5":
            print("\nThank you for using File Copier. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")
        
        input("\nPress Enter to continue...")

def demonstrate_file_modes():
    print("=" * 60)
    print("FILE MODES DEMONSTRATION")
    print("=" * 60)
    
    print("\nCommon file modes in Python:")
    print("-" * 40)
    print("Mode 'r'  : Read-only (default)")
    print("          File must exist, otherwise raises FileNotFoundError")
    print()
    print("Mode 'w'  : Write-only")
    print("          Creates file if it doesn't exist")
    print("          Truncates (erases) file if it exists")
    print()
    print("Mode 'a'  : Append")
    print("          Creates file if it doesn't exist")
    print("          Writes at the end of file if it exists")
    print()
    print("Mode 'r+' : Read and write")
    print("          File must exist")
    print("          Allows reading and writing")
    print()
    print("Mode 'rb' : Read binary")
    print("Mode 'wb' : Write binary")
    print("Mode 'ab' : Append binary")    
    print("\nFor this task, we use:")
    print("  - 'r' or 'rb' to read the source file")
    print("  - 'w' or 'wb' to write the destination file")

def basic_copy():
    filename = input("Enter filename to copy: ")    
    try:
        with open(filename, 'r') as source:
            content = source.read()
        
            output_name = filename + '_copy.txt'
        
        with open(output_name, 'w') as dest:
            dest.write(content)
        
        print(f"File copied successfully: {output_name}")
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Welcome to File Copier!")
    print("This program creates an exact copy of a file.")

    main_menu()
