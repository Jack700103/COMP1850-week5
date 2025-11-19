import csv

boundaries = {
    '1': 70,    
    '2:1': 60,  
    '2:2': 50,  
    '3': 40,    
    'F': 0      
}

def process_file(input_filename, output_filename):
    with open(input_filename, 'r') as f_in, open(output_filename, 'w', newline='') as f_out:
        reader = csv.reader(f_in)
        writer = csv.writer(f_out)

        writer.writerow(['student_id', 'average_grade', 'classification'])

        next(reader)
        
        for row in reader:
            student_id = row[0]
            grades = [float(x) for x in row[1:] if x.strip() != '']

            avg_grade = round(sum(grades) / len(grades), 2) if grades else 0

            classification = next(
                class_name for class_name, boundary in sorted(boundaries.items(), key=lambda x: x[1], reverse=True)
                if avg_grade >= boundary
            )
            
            writer.writerow([student_id, f"{avg_grade:.2f}", classification])

for file_name in ['student_data_10', 'student_data_25', 'student_data_50_A', 'student_data_50_B']:
    process_file(f"{file_name}.csv", f"{file_name}_out.csv")
    print(f"document {file_name}_out.csv Generated")