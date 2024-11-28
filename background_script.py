import os
import time
import tarfile


def ensure_tmp_folder():
    """
    Ensure a 'tmp' folder exists in the current directory.
    If the folder does not exist, create it.
    """
    if not os.path.exists("tmp"):
        os.makedirs("tmp")
        print("Created 'tmp' folder.")


def archive_files():
    """
    Archive all files in the 'tmp' folder into 'files.tar.gz'.
    Clear the 'tmp' folder after archiving.
    """
    with tarfile.open("files.tar.gz", "w:gz") as archive:
        for file in os.listdir("tmp"):
            archive.add(os.path.join("tmp", file), arcname=file)

    # Clear the tmp folder
    for file in os.listdir("tmp"):
        os.remove(os.path.join("tmp", file))
    print("Files collected and archived as 'files.tar.gz'.")


def monitor_tmp_folder():
    """
    Monitor the 'tmp' folder and check the number of files.
    Once the file count reaches 10, archive the files and exit.
    """
    ensure_tmp_folder()

    try:
        while True:
            files = os.listdir("tmp")
            if len(files) >= 10:
                archive_files()
                break
            else:
                print(f"Current file count in 'tmp': {len(files)}. Waiting...")
            time.sleep(5)  # Check every 5 seconds
    except KeyboardInterrupt:
        print("Script stopped by user.")


if __name__ == "__main__":
    monitor_tmp_folder()
