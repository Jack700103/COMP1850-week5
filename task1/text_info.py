def count_file_stats(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        lines = content.split('\n')
        words = content.split()
        chars = len(content)
        print(f"File statistics results:")
        print(f"Number of rows:{len(lines)}")
        print(f"Number of words:{len(words)}")
        print(f"Character count:{chars}")
    except FileNotFoundError:
        print(f"Error: The file '{file_cath}' does not exist")
    except PermissionError:
        print(f"错Error: No permission to read file")

count_file_stats("story.txt")