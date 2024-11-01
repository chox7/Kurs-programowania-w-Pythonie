import sys
import json

def read_ipynb(file_name):
    """Reads a .ipynb file and returns its content as a JSON object."""
    with open(file_name, 'r') as f:
        data = json.load(f)
    return data

def convert_cell(cell, line_length=130):
    """Converts a cell to Python code or Markdown comments."""
    if cell['cell_type'] == 'markdown':
        converted = []
        for line in cell['source']:
            # Split long lines into smaller
            while len(line) > line_length:
                # Find the last space
                split_index = line.rfind(' ', 0, line_length)
                if split_index == -1:  
                    split_index = line_length # No spaces
                converted.append('# ' + line[:split_index] + '\n')
                line = line[split_index:].lstrip()
    
            converted.append('# ' + line)

    elif cell['cell_type'] == 'code':
        converted = cell['source']
    
    return "".join(converted)

def ipynb_to_python(data):
    """Converts all cells to Python format."""
    cells = data['cells']
    python_data = list(map(convert_cell, cells))
    return python_data

def write_py(data, file_name):
    """Writes the converted Python data to .py file."""
    with open(file_name, 'w') as f:
        print(*data, file=f, sep="\n\n", end="\n")

def count_sequence(data, sequence):
    """Counts the number of string sequence occuring in list."""
    sequence_count = sum(1 for cell in filter(lambda x: sequence in x, data))
    return sequence_count

def convert_ipynb(file_name):
    """Main function to convert .ipynb to .py."""

    # Convert file names to .ipynb and .py type
    base_name = file_name.split('.ipynb')[0]
    ipynb_file = base_name + '.ipynb'
    python_file = base_name + '.py'

    json_data = read_ipynb(ipynb_file)
    python_file_data = ipynb_to_python(json_data)
    exercise_count = count_sequence(python_file_data, '# Ćwiczenie')
    print("Liczba ćwiczeń: ", exercise_count)
    write_py(python_file_data, python_file)

if __name__ == "__main__":
    # Check if there is a correct number of arguments
    if len(sys.argv) != 2:
        print("Nieprawidłowa liczba argumentów.")
        sys.exit(1)

    file_name = sys.argv[1]
    convert_ipynb(file_name)