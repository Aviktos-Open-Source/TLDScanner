# Global imports
import os

# Local imports
from .utils         import remove_duplicates

def read_file(file_path):
    """Reads the data from .data files and returns it as a list."""
    with open(file_path, 'r') as file:
        return [
            f".{line.strip().lstrip('.')}" for line in file.readlines() if line.strip()
        ]

def process_data(data_dir_path):
    """Processes all the .data file in the given directory and its subdirectories."""
    tlds_list = []
    for root, _, files in os.walk(data_dir_path):
        for file in files:
            if file.endswith('.data'):
                file_path = os.path.join(root, file)
                data = read_file(file_path)
                tlds_list.extend(data)
    sorted_data = sorted(remove_duplicates(tlds_list))
    return sorted_data
