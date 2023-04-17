import fileinput

import nltk
import string
import os

def counter(text,name):

    # Open the file in read mode

    # Create an empty dictionary
    d = dict()
    tok_c = 0

    # Loop through each line of the file
    for line in text:
        # Remove the leading spaces and newline character
        line = line.strip()

        # Convert the characters in line to
        # lowercase to avoid case mismatch
        line = line.lower()

        # Remove the punctuation marks from the line
        line = line.translate(line.maketrans("", "", string.punctuation + "¡¿"))

        # Split the line into words
        words = line.split(" ")
        #remove all the empty elements from the list (aka the deleted punctuation)
        words = [x for x in words if x != '']


        # Iterate over each word in line
        for word in words:
            tok_c = tok_c + 1
            # Check if the word is already in dictionary
            if word in d:
                # Increment count of word by 1
                d[word] = d[word] + 1
            else:
                # Add the word to dictionary with count 1
                d[word] = 1

    # Print the contents of dictionary
    with open("tsv_data/"+name, "w", encoding="utf-8")as c_dict:
        for key in list(d.keys()):
            c_dict.write(f"{key}\t{d[key]}")
            c_dict.write("\n")
    print(tok_c)
    print(d)
    return d

def overlapping(train_dic, dev_dic):
    overlapp = 0
    l_dev = len(dev_dic)
    l_train = len(train_dic)
    for key in dev_dic.keys():
        if key in train_dic.keys():
            overlapp = overlapp + 1
    print(len_dev, l_train, overlapp)


def write_tok_data(name):
    with open("tok_data/"+name, "w", encoding="utf-8") as file:
        for line in fileinput.input():
            if line.strip():
                file.write(" ".join(nltk.word_tokenize(line)))
                file.write("\n")


def main():

    path = "tok_data"
    # Check whether the specified path exists or not
    isExist = os.path.exists(path)
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(path)
        print("The new directory is created!")
    #write the data to a tokenized version:
    #write_tok_data("jw300.es-quy.quy")
    #write_tok_data("jw300.es-quy.es")
    #open the data and read it:
    text_train = open("tok_data/jw300.es-quy.quy", "r")
    text_dev = open("tok_data/jw300.es-quy.es", "r")
    #count the occurences of each token present in the file.
    name_train = "jw300.es-quy.quy"
    name_dev = "jw300.es-quy.es"
    overlapping(counter(text_train, name_train),counter(text_dev, name_dev))



if __name__ == "__main__":
    main()

