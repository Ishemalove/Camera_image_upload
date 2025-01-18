import os
import time
import subprocess
import shutil

# Configuration
MONITOR_FOLDER = "./camera_images"  # Folder to monitor
UPLOADED_FOLDER = "./uploaded"  # Folder to move uploaded files
UPLOAD_URL = "https://projects.benax.rw/f/o/r/e/a/c/h/p/r/o/j/e/c/t/s/4e8d42b606f70fa9d39741a93ed0356c/iot_testing_202501/upload.php"
UPLOAD_ATTRIBUTE = "imageFile"
UPLOAD_DELAY = 30  # Time delay before attempting an upload, in seconds

# Ensure folders exist
os.makedirs(MONITOR_FOLDER, exist_ok=True)
os.makedirs(UPLOADED_FOLDER, exist_ok=True)


def upload_image(file_path):
    """Uploads an image using the curl command."""
    try:
        result = subprocess.run(
            [
                "curl",
                "-X", "POST",
                "-F", f"{UPLOAD_ATTRIBUTE}=@{file_path}",
                UPLOAD_URL
            ],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print(f"Successfully uploaded: {file_path}")
            return True
        else:
            print(f"Failed to upload {file_path}. Error: {result.stderr}")
            return False

    except Exception as e:
        print(f"An error occurred while uploading {file_path}: {e}")
        return False


def move_to_uploaded_folder(file_path):
    """Moves a file to the uploaded folder."""
    try:
        filename = os.path.basename(file_path)
        destination = os.path.join(UPLOADED_FOLDER, filename)
        shutil.move(file_path, destination)
        print(f"Moved {file_path} to {UPLOADED_FOLDER}")
    except Exception as e:
        print(f"Failed to move {file_path} to {UPLOADED_FOLDER}: {e}")


def monitor_and_upload():
    """Monitors the folder and uploads new images."""
    print(f"Monitoring folder: {MONITOR_FOLDER}")
    while True:
        try:
            files = [f for f in os.listdir(MONITOR_FOLDER) if os.path.isfile(os.path.join(MONITOR_FOLDER, f))]

            for file in files:
                file_path = os.path.join(MONITOR_FOLDER, file)
                print(f"Detected file: {file_path}")

                time.sleep(UPLOAD_DELAY)  # Delay before attempting the upload

                if upload_image(file_path):
                    move_to_uploaded_folder(file_path)

        except Exception as e:
            print(f"Error during monitoring: {e}")

        time.sleep(5)  # Check for new files every 5 seconds


if __name__ == "__main__":
    monitor_and_upload()
