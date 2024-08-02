import streamlit as st
import os
import zipfile
import shutil
import tempfile

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
                out_file.write('---------\n')
                # Adds the file name before the content
                out_file.write(f"File: {file}\n\n")

                # Check if the file is not an image, video, or audio file
                if not file_path.endswith(('.jpg', '.jpeg', '.png', '.svg', '.gif', '.mp4', '.mov', '.mp3', '.wav')):
                    try:
                        with open(file_path, 'r') as in_file:
                            content = in_file.read()
                            out_file.write(content)
                            out_file.write('\n\n')
                    except UnicodeDecodeError:
                        out_file.write("[Binary or non-text content omitted]\n\n")
                    except Exception as e:
                        out_file.write(f"[Error reading file: {e}]\n\n")

# Streamlit app
st.title("Zip File to Text Converter")

uploaded_file = st.file_uploader("Choose a zip file", type="zip")

if uploaded_file is not None:
    with tempfile.TemporaryDirectory() as temp_dir:
        zip_path = os.path.join(temp_dir, uploaded_file.name)
        
        with open(zip_path, 'wb') as f:
            f.write(uploaded_file.getbuffer())
        
        extract_zip(zip_path, temp_dir)
        output_file = os.path.join(temp_dir, "output.txt")
        flatten_files(temp_dir, output_file)

        with open(output_file, 'r') as f:
            st.download_button(
                label="Download Processed File",
                data=f.read(),
                file_name='output.txt',
                mime='text/plain'
            )
