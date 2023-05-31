import os
import zipfile
import shutil

# Extract a zipped folder to a temporary directory
def extract_zip(zip_path, extract_dir):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)

# Flatten all files in a directory to a single file
def flatten_files(input_dir, output_file):
    with open(output_file, 'w') as out_file:
        for root, dirs, files in os.walk(input_dir):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as in_file:
                    out_file.write('---------\n')
                    out_file.write("File: " + file + " \n\n") # Adds the file name before the content
                    content = in_file.read()
                    out_file.write(content)
                    out_file.write('\n\n')  # Adds a newline after each file

# Convert a zipped folder to a text file
def zip_to_text(zip_path, output_file):
    temp_dir = 'temp_extract'
    extract_zip(zip_path, temp_dir)
    flatten_files(temp_dir, output_file)
    shutil.rmtree(temp_dir)  # Removes the temporary directory

# Specify the path to the input zipped folder
zip_path = '/Users/yourname/folder/zipped-folder.zip'

# Specify the path to the output text file
output_file = '/Users/yourname/Desktop/output.txt'

# Convert zipped folder to text file
zip_to_text(zip_path, output_file)