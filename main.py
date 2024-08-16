char_dict = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}

def main():
    file_path = "books/frankenstein.txt"
    text_in_file = read_file(file_path)
    word_count = num_words(text_in_file)

    #reporting part
    print("*** In the beninging of report for books/frankenstein.txt ***")
    print(f"{word_count} words found in the document")
    for i in num_chars(text_in_file):
        print(f"The {i} character appeared {char_dict[i]} times.")
    print("*** I bid thee farewell ***")




#takes path to a file as arguement and returns the text contained in the file
def read_file(path):
    with open(path) as f:
          file_contents = f.read()
    return file_contents

#takes text as a string and returns number of words in text
def num_words(strings):
     words = strings.split()
     return len(words)

#takes text as a string and returns number of times each character appears in a dictionary.
# --- Lowercase only
def num_chars(strings):
     for char in strings.lower():
          try:
            char_dict[char] += 1
          except Exception as e:
            pass
     return char_dict


main ()