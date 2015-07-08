import random

working_filename = "green-eggs.txt"
def make_chains(working_filename):
    corpus = open(working_filename)
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


    #print random_dict

    corpus.close()

    return random_dict    



def make_text(chain_dict):
    """Takes dictionary of markov chains; returns random text."""
    
    # loop - while rand_key in chain_dict:
    rand_key = random.choice(chain_dict.keys())
    text_random = rand_key[0] + " " + rand_key[1]
    while rand_key in chain_dict:
        #string_key = rand_key[0] + " " + rand_key[1]
        next_word_list = chain_dict[rand_key]
        new_word = random.choice(next_word_list) 

        text_random = text_random + " " + new_word 

        rand_key = (rand_key[1],new_word)

    print text_random


    # print rand_key, next_word_list

    # print " "

    # print string_key, new_word 

    
    

    return "Here's some random text."


# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

make_chains(working_filename)

#input_text = "Some text"

# Get a Markov chain
chain_dict = make_chains(working_filename)

# Produce random text
random_text = make_text(chain_dict)

print random_text
