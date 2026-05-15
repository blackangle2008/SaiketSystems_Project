from collections import Counter

print("===================================")
print("         WORD COUNT TOOL          ")
print("===================================")

# File name
file_name = "sample.txt"

try:

    # Open file in read mode
    file = open(file_name, "r")

    # Read file content
    content = file.read()

    # Close file
    file.close()

    # ==========================================
    # Count Lines, Words, Characters
    # ==========================================

    lines = content.splitlines()
    words = content.split()
    characters = len(content)

    line_count = len(lines)
    word_count = len(words)

    # ==========================================
    # Word Frequency Analysis
    # ==========================================

    # Convert words to lowercase
    cleaned_words = []

    for word in words:

        # Remove punctuation
        word = word.lower().strip(".,!?;:'\"()[]{}")

        cleaned_words.append(word)

    # Count frequency
    word_frequency = Counter(cleaned_words)

    # ==========================================
    # Display Results
    # ==========================================

    print("\n📄 FILE ANALYSIS REPORT")
    print("-----------------------------------")

    print(f"Total Lines      : {line_count}")
    print(f"Total Words      : {word_count}")
    print(f"Total Characters : {characters}")

    print("\n📊 MOST COMMON WORDS")
    print("-----------------------------------")

    # Display top 5 common words
    for word, count in word_frequency.most_common(5):

        print(f"{word} --> {count} times")

except FileNotFoundError:
    print("❌ Error: File not found.")

except PermissionError:
    print("❌ Error: Permission denied.")

except Exception as e:
    print("❌ An unexpected error occurred:")
    print(e)

finally:
    print("\nProgram execution completed.")