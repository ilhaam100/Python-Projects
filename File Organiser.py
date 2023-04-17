'''File organiser program that organises the files based on their file types'''
import os
import shutil

# Define the source and destination folders
source_folder = "/path/to/source/folder"
destination_folder = "/path/to/destination/folder"

# Create the destination folder if it does not exist
if not os.path.exists(destination_folder):
    os.mkdir(destination_folder)

# Define a dictionary of file types and their corresponding folders
file_types = {
    ".txt": "Text Files",
    ".docx": "Word Files",
    ".xlsx": "Excel Files",
    ".pdf": "PDF Files",
    ".png": "Image Files",
    ".jpg": "Image Files",
    ".mp3": "Music Files",
    ".mp4": "Video Files"
}

# Loop through all the files in the source folder
for filename in os.listdir(source_folder):
    # Get the file extension
    file_extension = os.path.splitext(filename)[1]
    # If the file extension is in the dictionary
    if file_extension in file_types:
        # Get the corresponding folder name
        folder_name = file_types[file_extension]
        # Create the folder if it doesn't exist
        folder_path = os.path.join(destination_folder, folder_name)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        # Move the file to the folder
        file_path = os.path.join(source_folder, filename)
        new_file_path = os.path.join(folder_path, filename)
        shutil.move(file_path, new_file_path)
