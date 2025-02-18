import string

def main():
    # Define the file path
    file_path = "books/frankenstein.txt"

    with open(file_path) as f:
        file_contents = f.read()  # Read the book text

        # Count total words
        word_count = len(file_contents.split())

        # Get sorted character frequencies
        char_list = get_sorted_char_counts(file_contents)

        # Print formatted report
        print_report(file_path, word_count, char_list)


def get_sorted_char_counts(text):
    """Counts occurrences of each letter (a-z) and returns a sorted list of dictionaries."""
    count_dict = {}  # Dictionary to store character counts

    # Loop through each character
    for char in text.lower():  # Convert to lowercase
        if char in string.ascii_lowercase:  # Only count alphabetic letters
            count_dict[char] = count_dict.get(char, 0) + 1

    # Convert dictionary to a list of dictionaries
    char_list = [{"char": char, "num": count} for char, count in count_dict.items()]

    # Sort the list by 'num' in descending order
    char_list.sort(reverse=True, key=sort_on)

    return char_list


def sort_on(dict_item):
    """Sorting function for .sort(), sorts by 'num' key."""
    return dict_item["num"]


def print_report(file_path, word_count, char_list):
    """Prints the formatted report to the console."""
    print(f"--- Begin report of {file_path} ---\n")
    print(f"{word_count} words found in the document\n")

    for item in char_list:
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("\n--- End report ---")


# Call main() to execute the script
main()
