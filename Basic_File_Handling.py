print("===================================")
print("       BASIC FILE HANDLING        ")
print("===================================")

# File name
file_name = "sample.txt"

try:

    # Open file in read mode
    file = open(file_name, "r")

    # Read file content
    content = file.read()

    file.close()

    print("\n📄 Original File Content:\n")
    print(content)

    # User input for word replacement
    old_word = input("\nEnter the word to find: ")
    new_word = input("Enter the replacement word: ")

    # Replace word
    updated_content = content.replace(old_word, new_word)

    # Open file in write mode
    file = open(file_name, "w")

    # Write updated content
    file.write(updated_content)

    file.close()

    print("\n✅ Word replaced successfully!")

    # Display updated content
    print("\n📄 Updated File Content:\n")
    print(updated_content)

except FileNotFoundError:
    print("❌ Error: File not found.")

except PermissionError:
    print("❌ Error: Permission denied.")

except Exception as e:
    print("❌ An unexpected error occurred:")
    print(e)

finally:
    print("\nProgram execution completed.")