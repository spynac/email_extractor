import re
import time
import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def extract_emails_from_file(file_name):
    """
    Extracts all email addresses from the specified file.

    Args:
        file_name (str): The name of the file to read.

    Returns:
        list: A list of extracted email addresses.
    """
    try:
        if not os.path.isfile(file_name):
            raise FileNotFoundError(f"The file '{file_name}' does not exist.")

        with open(file_name, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()

        # Simulating a processing animation
        print(Fore.YELLOW + "Processing file...")
        for i in range(1, 101):
            time.sleep(0.01)  # Simulated delay
            bar = (Fore.GREEN + "=" * (i // 2) + Style.RESET_ALL).ljust(50)
            print(f"\r[{bar}] {i}%", end="")
        print()

        # Regular expression to match email addresses
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = re.findall(email_pattern, content)

        # Remove duplicates and sort the emails
        unique_emails = sorted(set(emails))

        return unique_emails
    except FileNotFoundError as e:
        print(Fore.RED + f"Error: {e}")
        return []
    except PermissionError:
        print(Fore.RED + "Error: Permission denied to read the file.")
        return []
    except Exception as e:
        print(Fore.RED + f"An unexpected error occurred: {e}")
        return []

def save_emails_to_file(emails, file_name):
    """
    Saves the extracted emails to a .txt file with a timestamp.

    Args:
        emails (list): A list of email addresses.
        file_name (str): The original file name to generate the output name.
    """
    try:
        # Generate output file name with timestamp
        base_name = os.path.splitext(file_name)[0]
        output_file = f"{base_name}_emails_{int(time.time())}.txt"

        with open(output_file, 'w', encoding='utf-8') as file:
            for email in emails:
                file.write(email + '\n')

        print(Fore.CYAN + f"\nEmails successfully saved to '{output_file}'")
    except Exception as e:
        print(Fore.RED + f"Error saving emails to file: {e}")

if __name__ == "__main__":
    print(Fore.CYAN + "Welcome to the Email Extractor!" + Style.RESET_ALL)
    user_input = input(Fore.BLUE + "Enter the file name to extract emails from: " + Style.RESET_ALL).strip()

    # Simulating initialization animation
    print(Fore.YELLOW + "Initializing...")
    for i in range(1, 101, 20):
        time.sleep(0.1)
        bar = (Fore.MAGENTA + "=" * (i // 5) + Style.RESET_ALL).ljust(20)
        print(f"\r[{bar}] {i}%", end="")
    print(Fore.GREEN + "\nReady to process!\n")

    extracted_emails = extract_emails_from_file(user_input)

    if extracted_emails:
        print(Fore.GREEN + "\nExtracted Emails:")
        for email in extracted_emails:
            print(Fore.LIGHTBLUE_EX + email)

        # Automatically save results to a .txt file
        save_emails_to_file(extracted_emails, user_input)
    else:
        print(Fore.RED + "No emails found or an error occurred.")
