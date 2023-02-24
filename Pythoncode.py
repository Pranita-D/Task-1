import os
import time

# Define the directory to search for files
directory = "/home/ubuntu/myproject"

# Define the maximum age of files to be deleted (in seconds)
max_age = 30 * 60  # 30 minutes * 60 seconds/minute

# Get the current time
current_time = time.time()

# Loop through all files in the directory
for filename in os.listdir(directory):
    # Get the full path to the file
    file_path = os.path.join(directory, filename)
    # Check if the file is older than the maximum age
    if os.path.isfile(file_path) and (current_time - os.path.getmtime(file_path)) > max_age:
        # Delete the file
        os.remove(file_path)
