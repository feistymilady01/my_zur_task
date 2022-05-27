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

def count_words(text):
    # [assignment] Add your code here 
    my_dict = {}
    text = read_file_content("story.txt")
    for words in text:
        if words in my_dict:
            my_dict[words] += 1
        else:
            my_dict[words] = 0
            my_dict[words] +=1
        return my_dict

print(count_words(text))