# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    with open (filename,'r') as f:
        file = f.readlines()
        print(file)

read_file_content("story.txt")

def count_words():
    # [assignment] Add your code here 
    text = read_file_contrnt(./style txt)
    return(word:text.count_word(word) for word in text.split)
