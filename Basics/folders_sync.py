import os
import sys
import shutil
import time
import hashlib
import argparse


def sync_folders(source_folder, replica_folder, interval, log_file):
    if not os.path.exists(replica_folder):
        os.makedirs(replica_folder)
        log(f"Created directory {replica_folder}", log_file)
    
    log(f"Started monitoring {source_folder} and updating {replica_folder} at an interval of {interval} seconds", log_file)

    while True:
        for root, dirs, files in os.walk(source_folder):
            relative_path = os.path.relpath(root, source_folder)
            replica_path = os.path.join(replica_folder, relative_path)

            # Create directories in the replica folder if they don't exist
            for directory in dirs:
                source_dir = os.path.join(root, directory)
                replica_dir = os.path.join(replica_path, directory)
                if not os.path.exists(replica_dir):
                    os.makedirs(replica_dir)
                    log(f"Created directory: {replica_dir}", log_file)

            # Copy files from source to replica folder
            for file in files:
                source_file = os.path.join(root, file)
                replica_file = os.path.join(replica_path, file)

                # Only copy if the file doesn't exist or is different in the replica folder
                if not os.path.exists(replica_file) or os.stat(source_file).st_mtime > os.stat(replica_file).st_mtime:
                    shutil.copy2(source_file, replica_file)
                    log(f"Copied file: {replica_file}", log_file)

            # Remove files and directories from the replica folder if they don't exist in the source folder
            for replica_root, replica_dirs, replica_files in os.walk(replica_path):
                for replica_dir in replica_dirs:
                    source_dir = os.path.join(root, replica_dir)
                    if not os.path.exists(source_dir):
                        replica_dir = os.path.join(replica_root, replica_dir)
                        shutil.rmtree(replica_dir)
                        log(f"Removed directory: {replica_dir}", log_file)

                for replica_file in replica_files:
                    source_file = os.path.join(root, replica_file)
                    if not os.path.exists(source_file):
                        replica_file = os.path.join(replica_root, replica_file)
                        os.remove(replica_file)
                        log(f"Removed file: {replica_file}", log_file)

        time.sleep(interval)

def log(message, log_file):
    print(message)
    with open(log_file, "a") as file:
        file.write(message + "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Folder Synchronization Program")
    parser.add_argument("source_folder", type=str, help="Path to the source folder")
    parser.add_argument("replica_folder", type=str, help="Path to the replica folder")
    parser.add_argument("interval", type=int, help="Synchronization interval in seconds")
    parser.add_argument("log_file", type=str, help="Path to the log file")

    args = parser.parse_args()

    source_folder = args.source_folder
    replica_folder = args.replica_folder
    interval = args.interval
    log_file = args.log_file

    sync_folders(source_folder, replica_folder, interval, log_file)
    
