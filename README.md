Disk Usage Analyzer
📄 Project Overview
Disk Usage Analyzer is a simple Python tool to scan a directory and list the largest files and folders by size.
It helps you quickly understand what is taking up the most space on your disk.

🚀 Features
Calculates the total size of files and directories.

Lists the top N largest files and folders.

Handles missing files gracefully.

Provides a clean, readable disk usage report.

🛠️ How It Works
User Input:
The program prompts the user to enter a directory path.
(If left blank, it analyzes the current working directory.)

Size Calculation:
It traverses through the directory, calculates the size of each file and folder.

Sorting:
Items are sorted by size in descending order.

Display:
The top 10 largest items are displayed in a neat report.

📂 Project Structure
get_size(path):
Returns the size of a file or the total size of a directory.

analyze_disk_usage(directory, top_n=10):
Analyzes the disk usage of a given directory and returns the top N largest items.

print_report(items):
Prints a formatted report showing the paths and sizes.

main():
Handles user input and coordinates the analysis and reporting.

🧩 Requirements
Python 3.x

No external libraries required (only built-in os module is used).

💻 How to Run
bash
Copy
Edit
python disk_analyzer.py
Follow the prompt to enter the directory you want to analyze.

📈 Example Output
vbnet
Copy
Edit
Enter the directory to analyze (leave blank for current directory): 

Disk Usage Report:
Path                                               Size (bytes)   
=================================================================
/path/to/folder1                                   104857600     
/path/to/folder2                                   52428800      
/path/to/file1.txt                                 10485760      
...
