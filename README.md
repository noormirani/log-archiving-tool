# log-archiving-tool


This tool archives and compresses log files from a specified directory and stores them in a compressed .tar.gz format with a timestamp. It also logs the date and time of each archive action. This project helps keep your system organized by compressing and archiving old logs on demand.

Features:
Accepts a log directory as a command-line argument.
Compresses the log files into .tar.gz format.
Archives logs into a specified or default directory.
Logs the date and time of each archive operation into a log file.

Requirements:
Unix-based system (Linux, macOS).

Python 3 installed.

Installation:
Clone the repository:

```bash
git clone https://github.com/your-username/log-archiving-tool.git
cd log-archiving-tool
```

Make the script executable:

```bash

chmod +x log_archive_tool.py
```

Usage:
Basic Usage: Run the script by providing the path to the log directory you want to archive:

```bash
./log_archive_tool.py /path/to/log/directory
```

Optional: Specify an Archive Directory
You can specify a custom destination directory where the compressed logs will be stored (by default, it will save to /var/log/archived_logs):

```bash
./log_archive_tool.py /path/to/log/directory -d /path/to/archive/directory
```
Example Command
Archive logs from /var/log and store them in /home/user/archives:

```bash
./log_archive_tool.py /var/log -d /home/user/archives
```

Logs of the Archive Operation
The tool creates a archive_log.txt in the archive directory, which logs the date and time of each archive operation:

```bash
cat /home/user/archives/archive_log.txt
```
Notes:
The script uses the tar format to compress the logs.
It automatically names the archive files using the current date and time (e.g., logs_archive_20241014_123456.tar.gz).
Make sure you have the necessary permissions to access the log directory and create archives.


Example Output:
The archive will be saved as:

```bash
/path/to/archive/directory/logs_archive_YYYYMMDD_HHMMSS.tar.gz
```
And an entry like this will be added to archive_log.txt:

```vbnet

2024-10-14 12:34:56 - Archived logs to logs_archive_20241014_123456.tar.gz
```
License:
This project is open-source and free to use. Feel free to modify it as needed!

Project Page:
https://github.com/noormirani/log-archiving-tool
https://roadmap.sh/projects/log-archive-tool

Customization and Contribution:
If you'd like to add features, feel free to fork the project and submit a pull request! Some potential improvements could include:

Scheduling the archive with cron jobs.
Adding error handling for permissions issues or missing directories.
