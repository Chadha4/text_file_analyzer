import string
from collections import Counter

def analyze(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            text = file.read()
            lines=text.splitlines()
            line_count=len(lines)
            char_count=len(text)

            words=text.lower().translate(str.maketrans('','',string.punctuation)).split()
            word_count=len(words)
            word_freq=Counter(words)

            return {
                'line_count': line_count,
                'char_count' : char_count,
                'word_count': word_count,
                'word_freq' : word_freq
            }
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found!")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__=="__main__":

    dummy_file_text = """ This is a sample file for testing purposes.
    This file will be analyzed.
    We'll see how many words, chars and lines this file has.
    """
    dummy_file_name="sample.txt"
    try:
        with open(dummy_file_name,'w', encoding='utf-8') as f:
            f.write(dummy_file_text.strip())
        print(f"Created a dummy file: '{dummy_file_name}'")
    except Exception as e:
        print(f"Error: {e}")
        exit()
        
    file_to_analyze = dummy_file_name
    res = analyze(file_to_analyze)

    if res:
        print("\n File Analysis Results")
        print(f"File: {file_to_analyze}")
        print(f"Total Lines: {res['line_count']}")
        print(f"Total Characters: {res['char_count']}")
        print(f"Total Words: {res['word_count']}")

        print("\n Top 10 most frequent words")
        for word, count in res['word_freq'].most_common(10):
            print(f"'{word}' : {count}")

