def reverse_lines(input_file, output_file):
    try:
        with open(input_file, 'r') as f_in:
            lines = f_in.readlines()
        reversed_lines = [line.strip()[::-1] for line in lines]  # 简单实现行反转
        with open(output_file, 'w') as f_out:
            f_out.writelines(reversed_lines)
        print(f"Text reversal successful. Output file:{output_file}")
    except FileNotFoundError:
        print(f"Error: The file '{inputFILE}' does not exist")
    except PermissionError:
        print(f"Error: No permission to operate file")

reverse_lines("story.txt", "story.txt_reverse.txt")