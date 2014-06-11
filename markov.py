#!/usr/bin/env python
import random 

from sys import argv

def combine_files(script, filename, filename1):
    # Change this to read input_text from a file
    input_list = []

    first_text = open(filename, "r")
    first_text = first_text.read().split()
    second_text = open(filename1, "r")
    second_text = second_text.read().split()

    input_list = first_text + second_text

    return input_list

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    bag_of_words = corpus
    chains = {}

    """tuple key"""
    key = raw_input("How long do you want the tuple key to be? >>> ") #3

    key = int(key)

    # for i in range(key):
    #     tuple_key = bag_of_word[i:key]

    for i in range(len(bag_of_words) - key): # i the index
        #tuple_key = (bag_of_words[i], bag_of_words[i + 1])
        
        tuple_key = tuple(bag_of_words[i:i + key])
        print tuple_key
        value = [bag_of_words[i + key]]
        print value
        if chains.get(tuple_key, 0):
            chains[tuple_key] += value
        else:
            chains[tuple_key] = value
    return chains

def get_random_start(chains):
    """Pick one random tuple (key) from the Markov Chains dictionary."""
    start = random.choice(chains.keys())

    return start

def get_next_word(random_key, chains):
    """Given the last two words, get the next word from the Markov dictionary.
    Nick says we can stop after getting 10 words."""
    end = random.choice(chains[random_key])

    return end #end is a string, one word

def make_text(get_random_words_1, get_random_words_2):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    random_text = get_random_words_1 + " " + get_random_words_2
    return random_text

def main():
    script, filename, filename1 = argv

    input_list = combine_files(script, filename, filename1)

    # # Change this to read input_text from a file
    # input_text = open(filename, "r")

    chain_dict = make_chains(input_list)



    string = ""

    for x in range(10): 
        random_key = get_random_start(chain_dict)
        random_value = get_next_word(random_key, chain_dict)
        string += (" " + random_value)

    print string

if __name__ == "__main__":
    main()

