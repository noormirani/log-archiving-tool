#!/usr/bin/env python3

import os
import tarfile
import time
import argparse
from datetime import datetime

# Function to compress logs into a tar.gz file
def archive_logs(log_dir, archive_dir):
    # Check if the log directory exists
    if not os.path.exists(log_dir):
        print(f"Error: Log directory '{log_dir}' does not exist.")
        return
    
    # Ensure the archive directory exists, create it if not
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    # Create a timestamp for naming the archive
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    archive_name = f'logs_archive_{timestamp}.tar.gz'
    archive_path = os.path.join(archive_dir, archive_name)

    # Compress the log directory into a tar.gz file
    with tarfile.open(archive_path, "w:gz") as tar:
        tar.add(log_dir, arcname=os.path.basename(log_dir))

    # Log the archiving event
    log_entry = f"{datetime.now()} - Archived logs to {archive_name}\n"
    log_file_path = os.path.join(archive_dir, 'archive_log.txt')
    with open(log_file_path, 'a') as log_file:
        log_file.write(log_entry)

    print(f"Logs archived successfully at {archive_path}")

# Command-line interface for the tool
def main():
    parser = argparse.ArgumentParser(description="Log Archiving Tool")
    parser.add_argument("log_directory", help="Path to the directory containing logs")
    parser.add_argument("-d", "--dest", default="/var/log/archived_logs",
                        help="Directory to store archived logs (default: /var/log/archived_logs)")
    args = parser.parse_args()

    # Call the archive function with user input
    archive_logs(args.log_directory, args.dest)

if __name__ == "__main__":
    main()
