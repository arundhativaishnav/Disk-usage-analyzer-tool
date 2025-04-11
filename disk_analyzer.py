import os

def get_size(path):
    """Get the total size of a directory or file."""
    if os.path.isfile(path):
        try:
            return os.path.getsize(path)
        except FileNotFoundError:
            print(f"File not found: {path}")
            return 0
    elif os.path.isdir(path):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                fp = os.path.join(dirpath, filename)
                try:
                    total_size += os.path.getsize(fp)
                except FileNotFoundError:
                    print(f"File not found: {fp}")
                    continue  # Skip this file and continue
        return total_size
    return 0

def analyze_disk_usage(directory, top_n=10):
    """Analyze disk usage and return the largest files and directories."""
    items = []

    # Walk through the directory and gather sizes
    for entry in os.scandir(directory):
        if entry.is_file():
            items.append((entry.path, get_size(entry.path)))
        elif entry.is_dir():
            items.append((entry.path, get_size(entry.path)))

    # Sort items by size in descending order
    items.sort(key=lambda x: x[1], reverse=True)

    return items[:top_n]

def print_report(items):
    """Print the disk usage report."""
    print("\nDisk Usage Report:")
    print(f"{'Path':<50} {'Size (bytes)':<15}")
    print("=" * 65)
    for path, size in items:
        print(f"{path:<50} {size:<15}")

def main():
    """Main function to run the disk usage analyzer."""
    directory = input("Enter the directory to analyze (leave blank for current directory): ")
    if not directory:
        directory = os.getcwd()

    if not os.path.exists(directory):
        print("The specified directory does not exist.")
        return

    top_n = 10  # Number of largest files/directories to display
    largest_items = analyze_disk_usage(directory, top_n)
    print_report(largest_items)

if __name__ == "__main__":
    main()