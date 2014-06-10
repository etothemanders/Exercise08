#!/usr/bin/env python
import random 

from sys import argv


def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    bag_of_words = corpus.read().split()
    chains = {}

    for i in range(len(bag_of_words) - 2): # i the index
        if (bag_of_words[i], bag_of_words[i + 1]) not in chains:
            chains[(bag_of_words[i], bag_of_words[i + 1])] = [bag_of_words[i + 2]] # helps us avoid making the same keys?
        else:
            chains[(bag_of_words[i], bag_of_words[i + 1])] += [bag_of_words[i + 2]] #helps us avoid overwriting previous values
    #print chains
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
    script, filename = argv

    # Change this to read input_text from a file
    input_text = open(filename, "r")#.read()

    chain_dict = make_chains(input_text)

    x = 0
    string = ""

    while x < 10: 
        random_key = get_random_start(chain_dict)
        random_value = get_next_word(random_key, chain_dict)
        string += (" " + random_value)
        x += 1

    print string

if __name__ == "__main__":
    main()