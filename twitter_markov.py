import sys
import random



class SimpleMarkovGenerator(object):

    def read_files(self, working_filename1,working_filename2):
        """Given a list of files, make chains from them."""

        # your code here
        #working_filenames = "green-eggs.txt"

        text = working_filename1.read()
        text2 = working_filename2.read()

        text = text + text2

        working_filename1.close()
        working_filename2.close()

        return text


    def make_chains(self, text):
        """Takes input text as string; stores chains."""

        # your code here
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
        return random_dict  

    def make_text(self,chain_dict):
        """Takes dictionary of markov chains; returns random text."""

        # your code here
        while True:
            rand_key = random.choice(chain_dict.keys())
            if rand_key[0].isupper():
                break

        text_random = rand_key[0] + " " + rand_key[1]
        while rand_key in chain_dict:
            next_word_list = chain_dict[rand_key]
            new_word = random.choice(next_word_list)            

            text_random = text_random + " " + new_word 
            
            rand_key = (rand_key[1], new_word)
            
        return text_random    


# class TweetableMarkovGenerator(SimpleMarkovGenerator):
#     def limit_140char(self, full_text):
#         """ Takes generated random text and limits it to
#         the last full sentence before 140 characters."""
        

        


if __name__ == "__main__":

    if len(sys.argv) <= 2:
        sys.exit()

    # Get the name of the log file to open from the command line
    working_filenames = sys.argv[1], sys.argv[2]
 


    # Open the log file
    # Creating the object file, instance of file.
    f = open(working_filenames[0])
    f2 = open(working_filenames[1])




    generator = SimpleMarkovGenerator()

    text = generator.read_files(f,f2)

    chain_dict = generator.make_chains(text)
    random_text = generator.make_text(chain_dict)

    print random_text

    # we should get list of filenames from sys.argv
    # we should make an instance of the class
    # we should call the read_files method with the list of filenames
    # we should call the make_text method 5x
