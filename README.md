# Python-week4.assignment
WEEK4 assignment, File Handling

# 📝 Text File Processor

This Python script reads a text file, processes its content, and handles user input for additional file operations.

## 📌 Features

- Reads content from `input.txt`
- Displays original and uppercase versions
- Calculates and displays word count
- Saves processed content to `modified.txt`
- Prompts the user for another filename and handles errors like:
  - File not found
  - Permission denied
  - Other unexpected issues

## 📂 Required Files
- `main.py` for editing and running the code.
- `input.txt`: Place this file in the same directory with the `main.py` to link them.

## 💾 Output

The script generates a modified file called `modified.txt` containing:
- Uppercase version of the original text
- Word count
- A friendly closing message.


## 🚀 How to Run

1. Make sure Python 3 is installed.
2. Save the script `main.py`.
3. Place `input.txt` in the same folder.
4. Run the script:

```bash```
python text_processor.py

5. After processing, you'll be prompted to enter the name of another file to open. The script will handle errors if the file doesn't exist or can't be read.

✅ Error Handling
The script gracefully handles:

Missing or unreadable files

Permission issues

General exceptions with clear messages

👋 Final Output
The terminal will show:

Original content from input.txt

Uppercase version of the content

Word count

A prompt to test the filename input feature.
