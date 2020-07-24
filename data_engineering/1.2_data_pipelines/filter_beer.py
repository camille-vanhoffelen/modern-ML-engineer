import glob
import os 

def file_name(path):
        return os.path.basename(path)

def read_file(path):
    with open(path, 'r') as f:
        return f.read()

def contains_beer(text):
    return 'beer' in text.lower()

def write_file(path, content):
    with open(path, 'w') as f:
        f.write(content)

def filter_beer(input_dir, output_dir):
    # INSERT YOUR CODE HERE

def main():
    filter_beer('input', 'output')

if __name__ == "__main__":
    # execute only if run as a script
    main()
