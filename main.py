

with open("input.txt", "r") as file:
    content = file.read()

    print(content)


# Open the file in read mode to read its content
with open("input.txt", "r") as file:

    content = file.read()

# Convert the text to uppercase
uppercase_content = content.upper()

# Calculate the word count
word_count = len(content.split())

# Print the uppercase content
print("Uppercase Text:")
print(uppercase_content)

with open("modified.txt", "w") as file:
    file.write("processed text:\n")
    file.write(uppercase_content + "\n")
    file.write(f"\nword count: {word_count}\n")
    file.write("THANK YOU....THE END!!")


#Ask the user for a filename and handle errors if it doesn’t exist or can’t be read

import os

def get_filename():
    filename = input("please enter the filename:")
    try:
        if not os.path.exists (filename):
            raise FileNotFoundError (f"The file'{filename}' does not exist")
        with open(filename, 'r') as file:
            print(f"successfully opened'{filename}'.")
    except FileNotFoundError as e:
        print(e)
    except PermissionError:
        print(f"permission denied: Unable to read the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occured: {e}")

if __name__ == "__main__":
    get_filename()
