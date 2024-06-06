import os
import argparse
from datetime import datetime
from colorama import Fore, Style, init


def parse_logs(folder_path):
    log_entries = []

    def is_date(find_date):
        try:
            datetime.strptime(find_date[:19], "%Y-%m-%d %H:%M:%S")
            return True
        except ValueError:
            return False

    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    current_entry = []
                    for line in f:
                        if is_date(line):
                            if current_entry:
                                log_entries.append((' '.join(current_entry), file_path))
                                current_entry = []
                        current_entry.append(line.strip())
                    if current_entry:
                        log_entries.append((' '.join(current_entry), file_path))
            except Exception as e:
                print(f"Could not read file {file_path} due to {e}")

    return log_entries


def search_in_entries(log_entries, search_text):
    results = []

    for entry, file_path in log_entries:
        if search_text in entry:
            words = entry.split()
            search_text_index = words.index(search_text)
            start_index = max(0, search_text_index - 5)
            end_index = min(len(words), search_text_index + 6)
            snippet = ' '.join(words[start_index:end_index])
            results.append((file_path, snippet))

    return results


def main():
    parser = argparse.ArgumentParser(description='Search for text in log files.')
    parser.add_argument('folder_path', type=str, help='The path to the folder containing log files')
    parser.add_argument('--text', type=str, required=True, help='The text to search for in the files')

    args = parser.parse_args()

    folder_path = args.folder_path
    search_text = args.text

    init(autoreset=True)

    log_entries = parse_logs(folder_path)
    results = search_in_entries(log_entries, search_text)

    for file_path, snippet in results:
        print(f"{Fore.RED}File: {Fore.LIGHTYELLOW_EX}{file_path}{Style.RESET_ALL}")
        print(f"{Fore.RED}Snippet: {Fore.BLUE}{snippet}...{Style.RESET_ALL}\n")


if __name__ == "__main__":
    main()
