def copy_file(input_file, output_file):
    try:
        with open(input_file, 'r') as f_in:
            content = f_in.read()
        with open(output_file, 'w') as f_out:
            f_out.write(content)
        print(f"File copied successfully. Output file: {output_file}")
    except FileNotFoundError:
        print(f"Error: The file '{inputFILE}' does not exist")
    except PermissionError:
        print(f"Error: No permission to operate file")

copy_file("story.txt", "story.txt_copy.txt")