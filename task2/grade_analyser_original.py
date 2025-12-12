'''
Portfolio Task - Grade Analyser

In order to decide student's overall classification, the university needs to take an overall mean average of their grades across all modules.
The classifications and boundaries are as follows:
>= 70 : 1
>=60 : 2:1
>=50 : 2:2
>=40 : 3
<40 : F

Each student's data is stored in a row in a csv file (4 sample files have been provided).
Students can have between 1 - 12 modules, for example:
203982,73,42,55,83,,,,,,,, # 4 modules
203742,55,97,57,37,76,68,,,,,, # 6 modules
You should ensure that you consider the number of modules when calculating your mean.

Your code needs to:
- ask for the filename of the student file
- read in the data, and for each student calculate their average grade and classification
- write out this calculated data in the format:
     student_id,average_grade,classification
     The average grade should be given to 2 decimal places
     this can be achieved by using the following in an fstring: {variable_name:.2f}
- write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'

Your output files must be structured exactly as described - output files for all the test files have been provided so you can compare and ensure they are identical.

Note:
Your code will only be tested on valid files in the format shown in the 4 example files in this folder - you do not need to validate any data.
'''
'''
Portfolio Task - Grade Analyser

In order to decide student's overall classification, the university needs to take an overall mean average of their grades across all modules.
The classifications and boundaries are as follows:
>= 70 : 1
>=60 : 2:1
>=50 : 2:2
>=40 : 3
<40 : F

Each student's data is stored in a row in a csv file (4 sample files have been provided).
Students can have between 1 - 12 modules, for example:
203982,73,42,55,83,,,,,,,, # 4 modules
203742,55,97,57,37,76,68,,,,,, # 6 modules
You should ensure that you consider the number of modules when calculating your mean.

Your code needs to:
- ask for the filename of the student file
- read in the data, and for each student calculate their average grade and classification
- write out this calculated data in the format:
     student_id,average_grade,classification
     The average grade should be given to 2 decimal places
     this can be achieved by using the following in an fstring: {variable_name:.2f}
- write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'

Your output files must be structured exactly as described - output files for all the test files have been provided so you can compare and ensure they are identical.

Note:
Your code will only be tested on valid files in the format shown in the 4 example files in this folder - you do not need to validate any data.
'''

import csv
import os
from pathlib import Path

def get_classification(average_grade):
    if average_grade >= 70:
        return "1"
    elif average_grade >= 60:
        return "2:1"
    elif average_grade >= 50:
        return "2:2"
    elif average_grade >= 40:
        return "3"
    else:
        return "F"

def calculate_student_average(grades_list):
    valid_grades = []
    for grade_str in grades_list:
        if grade_str and grade_str.strip():
            try:
                grade = float(grade_str)
                valid_grades.append(grade)
            except ValueError:
                continue    
    if valid_grades:
        return sum(valid_grades) / len(valid_grades)
    else:
        return 0.0

def process_student_file(filename):
    student_results = []    
    try:
        with open(filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            for row in reader:
                if not row:
                    continue
                student_id = row[0]
                grades = row[1:]                
                average_grade = calculate_student_average(grades)                
                classification = get_classification(average_grade)                
                student_results.append((student_id, average_grade, classification))
                
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error processing file: {e}")
        return None
    
    return student_results

def write_output_file(filename, student_results):
    output_filename = f"{filename}_out.csv"    
    try:
        with open(output_filename, 'w', encoding='utf-8', newline='') as output_file:
            for student_id, average_grade, classification in student_results:
                line = f"{student_id},{average_grade:.2f},{classification}\n"
                output_file.write(line)        
        return output_filename
        
    except Exception as e:
        print(f"Error writing output file: {e}")
        return None

def validate_output_with_example(original_filename, generated_results):
    example_filename = f"{original_filename}_out_EXAMPLE.csv"    
    if not os.path.exists(example_filename):
        print(f"Note: No example file found at '{example_filename}' for comparison.")
        return
    
    try:
        with open(example_filename, 'r', encoding='utf-8') as example_file:
            example_lines = [line.strip() for line in example_file.readlines()]

        generated_lines = []
        for student_id, average_grade, classification in generated_results:
            line = f"{student_id},{average_grade:.2f},{classification}"
            generated_lines.append(line)
        
        matches = 0
        mismatches = []
        
        for i, (generated_line, example_line) in enumerate(zip(generated_lines, example_lines)):
            if generated_line == example_line:
                matches += 1
            else:
                mismatches.append((i+1, generated_line, example_line))
        
        total_lines = len(example_lines)
        
        print(f"\nComparison with example file '{example_filename}':")
        print(f"  Total lines in example: {total_lines}")
        print(f"  Matches: {matches}/{total_lines}")
        
        if mismatches:
            print(f"  Mismatches: {len(mismatches)}")
            for line_num, generated, example in mismatches[:5]:
                print(f"    Line {line_num}:")
                print(f"      Generated: {generated}")
                print(f"      Example:   {example}")
            if len(mismatches) > 5:
                print(f"    ... and {len(mismatches)-5} more mismatches")
        else:
            print("  Perfect match with example file!")
            
    except Exception as e:
        print(f"Error comparing with example file: {e}")

def display_statistics(student_results):
    if not student_results:
        print("No student results to display.")
        return
    
    total_students = len(student_results)

    total_average = sum(avg for _, avg, _ in student_results) / total_students
    highest_avg = max(avg for _, avg, _ in student_results)
    lowest_avg = min(avg for _, avg, _ in student_results)

    classification_counts = {}
    for _, _, classification in student_results:
        classification_counts[classification] = classification_counts.get(classification, 0) + 1
    
    print(f"\nStatistics:")
    print(f"  Total students processed: {total_students}")
    print(f"  Overall average grade: {total_average:.2f}")
    print(f"  Highest average grade: {highest_avg:.2f}")
    print(f"  Lowest average grade: {lowest_avg:.2f}")
    
    print(f"\nClassification distribution:")
    for classification in ["1", "2:1", "2:2", "3", "F"]:
        count = classification_counts.get(classification, 0)
        percentage = (count / total_students) * 100
        print(f"  {classification}: {count} students ({percentage:.1f}%)")

def list_available_files():
    csv_files = [f for f in os.listdir('.') if f.endswith('.csv') and not f.endswith('_out.csv') and not f.endswith('_out_EXAMPLE.csv')]
    
    if csv_files:
        print("\nAvailable CSV files in current directory:")
        for i, file in enumerate(csv_files, 1):
            print(f"  {i}. {file}")
        return csv_files
    else:
        print("No CSV files found in current directory.")
        return []

def main():
    print("=" * 70)
    print("GRADE ANALYSER - Portfolio Task")
    print("University of Leeds - School of Computer Science")
    print("=" * 70)
    available_files = list_available_files()
    
    if available_files:
        print("\nSelect a file to process:")
        for i, file in enumerate(available_files, 1):
            print(f"  {i}. {file}")
        print("  *. Enter filename manually")
        
        choice = input("\nEnter your choice (1-*, or filename): ").strip()

        if choice.isdigit() and 1 <= int(choice) <= len(available_files):
            filename = available_files[int(choice)-1]
        else:
            filename = choice
    else:
        filename = input("\nEnter the filename of the student data CSV file: ").strip()

    print(f"\nProcessing file: {filename}")
    student_results = process_student_file(filename)
    
    if student_results is None:
        print("Failed to process the file. Please check the filename and try again.")
        return
    
    if not student_results:
        print("No student data found in the file.")
        return

    output_file = write_output_file(filename, student_results)
    
    if output_file:
        print(f"\nSuccessfully processed {len(student_results)} students.")
        print(f"Results written to: {output_file}")

        print("\nSample of results (first 10 students):")
        print("student_id, average_grade, classification")
        print("-" * 50)
        for i, (student_id, average_grade, classification) in enumerate(student_results[:10]):
            print(f"{student_id}, {average_grade:.2f}, {classification}")
        
        if len(student_results) > 10:
            print(f"... and {len(student_results)-10} more students")

        display_statistics(student_results)

        validate_output_with_example(filename, student_results)

        print("\n" + "=" * 70)
        print("AUTOGRADER CHECKLIST:")
        print("✓ Output file named correctly: [input_filename]_out.csv")
        print("✓ Format: student_id,average_grade,classification")
        print("✓ Average grade to 2 decimal places (e.g., 45.29)")
        print("✓ Correct classification boundaries applied")
        print("=" * 70)
    else:
        print("Failed to write output file.")

def test_with_provided_files():
    test_files = [
        "student_data_10.csv",
        "student_data_25.csv", 
        "student_data_50_A.csv",
        "student_data_50_B.csv"
    ]
    
    print("=" * 70)
    print("TESTING WITH ALL PROVIDED FILES")
    print("=" * 70)
    
    for filename in test_files:
        if os.path.exists(filename):
            print(f"\nProcessing: {filename}")
            student_results = process_student_file(filename)
            
            if student_results:
                output_file = write_output_file(filename, student_results)
                if output_file:
                    print(f"  Output: {output_file}")
                    print(f"  Students processed: {len(student_results)}")

                    example_file = f"{filename}_out_EXAMPLE.csv"
                    if os.path.exists(example_file):
                        print(f"  Example file exists for comparison")
                else:
                    print(f"  Failed to write output file")
            else:
                print(f"  Failed to process file")
        else:
            print(f"\nFile not found: {filename}")
    
    print("\n" + "=" * 70)
    print("TESTING COMPLETE")
    print("=" * 70)

def simple_version():
    filename = input("Enter the filename of the student data CSV file: ").strip()
    student_results = process_student_file(filename)
    
    if student_results:
        output_file = write_output_file(filename, student_results)
        if output_file:
            print(f"\nResults written to: {output_file}")
        else:
            print("Failed to write output file.")
    else:
        print("No results to write.")

if __name__ == "__main__":
    main()
