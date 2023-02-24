#!/usr/bin/env python3
import os
import time
import subprocess

# Directory Path
directory = '/home/ubuntu/myproject/'

# 30 Min age of files to be deleted 
max_age = 30 * 60  

# Get the current time
current_time = time.time()

# All files in the directory
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    # Check All file of the  the maximum age
    if os.path.isfile(file_path) and (current_time - os.path.getmtime(file_path)) > max_age:
        # Delete the file using curl command
        subprocess.call(['curl', '-X', 'DELETE', 'https://localhost:8080/files/' + filename])
        os.remove(file_path)
        
