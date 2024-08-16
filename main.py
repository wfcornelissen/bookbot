def main():
    file_path = "books/frankenstein.txt"
    text_in_file = read_file(file_path)
    #REMOVE WHEN NEEDED. Don't want to print full text to console each run. print(text_in_file)
    word_count = num_words(text_in_file)
    print(f'function num_words returned an integer of: {word_count}')
    print("Calling function: num_chars")


#takes path to a file as arguement and returns the text contained in the file
def read_file(path):
    with open(path) as f:
          file_contents = f.read()
    return file_contents

#takes text as a string and returns number of words in text
def num_words(strings):
     words = strings.split()
     return len(words)

#takes text as a string and returns number of times each character appears.
# --- Lowercase only

def num_chars(strings):
     print("starting function:num_chars")


main ()