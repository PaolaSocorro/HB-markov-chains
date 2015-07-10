import os
import twitter
import twitter_markov
import sys


if len(sys.argv) <= 2:
    sys.exit()

# Get the name of the log file to open from the command line
working_filenames = sys.argv[1], sys.argv[2]



# Open the log file
# Creating the object file, instance of file.
f = open(working_filenames[0])
f2 = open(working_filenames[1])



api = twitter.Api(
    consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
    consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
    access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
    access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

#Create instance of class SimpleMarkovGenerator
markov = twitter_markov.TweetableMarkovGenerator()
text = markov.read_files(f,f2)

dictionary = markov.make_chains(text)
random_text = markov.make_text(dictionary)

#create instance of class TweetableMarkovGenerator
our_tweet = markov.limit_140char(random_text)

print "\n"
print "#############################################"
print "\n"
print our_tweet




print api.VerifyCredentials()

#send tweet

status = api.PostUpdate(our_tweet)
print status.text

# print " "
# message = raw_input("Enter to tweet again [q to quit]")
#     if message != "q":        