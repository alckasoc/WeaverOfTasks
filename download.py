"""Downloads the wildfires dataset from Kaggle.

Source: https://www.kaggle.com/datasets/rtatman/188-million-us-wildfires/data
"""

import subprocess
import zipfile
import os

def download_wildfires_dataset() -> None:
    """Download the wildfire dataset."""

    original_directory = os.getcwd()

    os.chdir('data/')

    # Command to download the dataset from Kaggle.
    command = "kaggle datasets download -d rtatman/188-million-us-wildfires"

    # Run the command.
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    os.chdir(original_directory)

    # Check the output and error.
    if result.returncode == 0:
        print("Download successful")
        print(result.stdout)
    else:
        print("Error occurred")
        print(result.stderr)

def unzip_data() -> None:

    # Specify the path to your zip file.
    zip_file_path = 'data/188-million-us-wildfires.zip'

    # Specify the directory to extract to.
    extract_to_path = 'data/'

    # Create a ZipFile object.
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # Extract all the contents into the directory.
        zip_ref.extractall(extract_to_path)

    print("Files extracted successfully!")



if __name__ == "__main__":
    download_wildfires_dataset()
    unzip_data()