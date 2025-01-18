Folder Monitoring and Image Upload Script

This Python script automates the following tasks:

Monitor a folder: Watches a specified folder where a camera regularly saves captured images.
Upload images: Automatically uploads each image to a provided URL after a 30-second delay using the curl command.
Organize files: Moves successfully uploaded images to a separate uploaded folder to prevent redundant uploads.

Features

Automated Monitoring: Detects new files in the folder.
Timed Uploads: Ensures a delay before uploading each image.
File Management: Automatically organizes and moves files after successful uploads.
Error Logging: Prints logs for upload success or failure and any file movement errors.

Configuration

Update the following variables in the script as needed:

MONITOR_FOLDER: Path to the folder being monitored.
UPLOADED_FOLDER: Path to the folder where successfully uploaded images are moved.
UPLOAD_URL: URL to which the images are uploaded.
UPLOAD_ATTRIBUTE: Key attribute for the curl POST request.
UPLOAD_DELAY: Time delay (in seconds) before uploading a detected image.

Prerequisites

Python: Install Python (version 3.6 or higher).
Curl: Ensure the curl command is installed and available in your system's PATH.

Usage

Clone this repository:

git clone <repository_url>
cd <repository_name>

Ensure the required folders (MONITOR_FOLDER and UPLOADED_FOLDER) exist or are automatically created by the script.

Run the script:
python <script_name>.py
Place images in the MONITOR_FOLDER to trigger uploads.

Example

Folder to Monitor: ./camera_images

Uploaded Folder: ./uploaded

Upload URL: https://projects.benax.rw/f/o/r/e/a/c/h/p/r/o/j/e/c/t/s/4e8d42b606f70fa9d39741a93ed0356c/iot_testing_202501/upload.php

Command to Run: python folder_monitor_upload.py
