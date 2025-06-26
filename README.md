Text File Analyzer
This Python script provides a simple tool to analyze text files. It calculates various statistics about the text, including word count, character count, line count, and the frequency of words.

Features
Line Count: Counts the total number of lines in the file.

Character Count: Counts the total number of characters, including spaces, newlines, and punctuation.

Word Count: Counts the total number of words. Words are converted to lowercase and punctuation is removed for accurate counting.

Word Frequency: Identifies and displays the top 10 most frequent words in the text.

How to Use
Save the Script:
Save the provided Python code as a .py file (e.g., text_analyzer.py).

Prepare Your Text File:
Ensure you have a text file (.txt) that you want to analyze. The script includes a demonstration mode that creates a sample.txt file for testing.

Run the Script:
Open your terminal or command prompt, navigate to the directory where you saved text_analyzer.py, and run the script:

python text_analyzer.py

Analyze Your Own File:
To analyze a different text file, open text_analyzer.py in a text editor and locate the following line within the if __name__ == "__main__": block:

file_to_analyze = dummy_file_name # You can change this to any other text file

Change dummy_file_name to the path of your desired file. For example:

file_to_analyze = "path/to/your/my_document.txt"

Then, save the changes and run the script again.

Example Output
When run, the script will output statistics similar to this:

Created a dummy file: 'sample.txt' for testing.

File Analysis Results
File: sample.txt
Total Lines: 4
Total Characters: 140
Total Words: 24

Top 10 most frequent words
'this': 2
'is': 2
'a': 2
'text': 2
'sample': 2
'file': 2
'it': 1
'has': 1
'multiple': 1
'lines': 1

Requirements
Python 3.x
