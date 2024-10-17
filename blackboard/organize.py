import os
import shutil
import zipfile

# Directory path containing assignment files
# PATH MUST BE CHANGED ACCORDING TO THE LOCATION OF THE ASSIGNMENT FILES
# FOR WINDOW "\\"
# FOR LINUX "/"
# FOR MAC "/"

assignments_path = "INSERT PATH HERE"

# Iterate over all files in the directory
for filename in os.listdir(assignments_path):
    # Split the filename based on '_'
    parts = filename.split('_')
    
    if len(parts) > 1:  # Filename must contain '_'
        student_number = parts[1]  # Extract student number (adjust according to filename rules)
        
        student_folder_path = os.path.join(assignments_path, student_number)
        
        if not os.path.exists(student_folder_path):
            os.makedirs(student_folder_path)
        
        # Move the file to the student number folder
        shutil.move(os.path.join(assignments_path, filename), student_folder_path)

print('Initial file organization complete!')

# Unzip files within each student folder
total_zip_files = 0
for student_folder in os.listdir(assignments_path):
    student_folder_path = os.path.join(assignments_path, student_folder)
    
    if os.path.isdir(student_folder_path):  # Check if it is a directory
        for file in os.listdir(student_folder_path):
            if file.endswith('.zip'):
                total_zip_files += 1

processed_zip_files = 0
for student_folder in os.listdir(assignments_path):
    student_folder_path = os.path.join(assignments_path, student_folder)
    
    if os.path.isdir(student_folder_path):  # Check if it is a directory
        for file in os.listdir(student_folder_path):
            if file.endswith('.zip'):
                zip_file_path = os.path.join(student_folder_path, file)
                
                # Unzip the file
                try:
                    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                        zip_ref.extractall(student_folder_path)
                except FileNotFoundError as e:
                    print(f"Error occurred while extracting file: {e}")
                    continue
                
                # Delete the zip file (optional)
                os.remove(zip_file_path)
                
                processed_zip_files += 1
                print(f'Unzipping progress: {processed_zip_files}/{total_zip_files} complete')

print('All files unzipped in each folder!')
