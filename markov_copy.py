import sys

corpus = open("green-eggs.txt")
#corpus.read()
def make_chains(corpus):
    text = corpus.read()
    """Takes input text as string; returns dictionary of markov chains."""
    random_dict = {}
    text = text.replace('/n',' ')
    print text
    words = text.split()

    i = 0
    while i < (len(words) - 1):
        keys = []
        keys.append(words[i])
        keys.append(words[i+1])
        random_dict[tuple(keys)] = None
        i += 1
        print keys
    print random_dict    






    return {}


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    return "Here's some random text."


# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

make_chains(corpus)

#input_text = "Some text"

# Get a Markov chain
chain_dict = make_chains(input_text)

# Produce random text
random_text = make_text(chain_dict)

print random_text
