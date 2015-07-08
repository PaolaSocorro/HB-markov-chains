import random

opened_file = open("green-eggs.txt")
def make_chains(corpus):
    text = corpus.read()
    """Takes input text as string; returns dictionary of markov chains."""
    random_dict = {}
    text = text.replace('/n',' ')
    words = text.split()

    i = 0

    while i < (len(words) - 2):
        keys = []
        keys.append(words[i])
        keys.append(words[i+1])
        third_word = words[i+2]
        tuple_key = tuple(keys)


        if tuple_key not in random_dict:
            random_dict[tuple_key] = [third_word]

        else:
            random_dict[tuple_key].append(third_word)

        i += 1    


    return random_dict    



def make_text(dict_chains):
    """Takes dictionary of markov chains; returns random text."""

    random.choice(dict_chains.keys())
    
    

    return "Here's some random text."


# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

make_chains(opened_file)

#input_text = "Some text"

# Get a Markov chain
chain_dict = make_chains(opened_file)

# Produce random text
random_text = make_text(chain_dict)

print random_text
