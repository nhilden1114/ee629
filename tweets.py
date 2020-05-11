#  Author:  Nicole Hilden
#  Initialization written by Cheryl Dugas

# tweets.py searches Twitter for tweets matching a search term,
#      up to a maximun number

######  user must supply authentication keys where indicated

# to run from terminal window: 
#        python3  tweets.py   --search_term1  mysearch1  --search_term2  mysearch2 --search_max  mymaxresults 
# where:  mysearch1 is the first term the user wants to search for;  default = music
# where:  mysearch2 is the second term the user wants to search for; default = movie
#   and:  mymaxresults is the maximum number of resulta;  default = 30

# other options used in the search:  lang = "en"  (English language tweets)
#  and  result_type = "popular"  (asks for most popular rather than most recent tweets)

# The program uses the TextBlob sentiment property to analyze the tweet for:
#  polarity (range -1 to 1)  and  
#  subjectivity (range 0 to 1 where 0 is objective and 1 is subjective)

# The program creates a .csv output file with a line for each tweet
#    including tweet data items and the sentiment information

from textblob import TextBlob	# needed to analyze text for sentiment
import argparse    				# for parsing the arguments in the command line
import csv						# for creating output .csv file
import tweepy					# Python twitter API package
import unidecode				# for processing text fields in the search results

### PUT AUTHENTICATOIN KEYS HERE ###
CONSUMER_KEY = "YOUR KEY HERE"
CONSUMER_KEY_SECRET = "YOUR KEY HERE"
ACCESS_TOKEN = "YOUR KEY HERE"
ACCESS_TOKEN_SECRET = "YOUR KEY HERE"

# AUTHENTICATION (OAuth)
authenticate = tweepy.auth.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
authenticate.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(authenticate)

# Get the input arguments - search_term1, search_term2, and search_max
parser = argparse.ArgumentParser(description='Twitter Search')
parser.add_argument("--search_term1", action='store', dest='search_term1', default="music")
parser.add_argument("--search_term2", action='store', dest='search_term2', default="movie")
parser.add_argument("--search_max", action='store', dest='search_max', default=30)
args = parser.parse_args()

search_term1 = args.search_term1
search_term2 = args.search_term2
search_max = int(args.search_max)

print("You searched for", search_term1, "and", search_term2);
print("The maximum number of search results: ", search_max);

# create a .csv file to hold the results from user's first search term, and write the header line
csvFile = open('twitter_results1.csv','w')
csvWriter = csv.writer(csvFile)
csvWriter.writerow(["username","userid","created", "text", "retweets", "followers",
    "friends","polarity","subjectivity"])

# do the twitter search on first term
for tweet in tweepy.Cursor(api.search, q = search_term1, lang = "en", 
		result_type = "popular").items(search_max):
		
    created = tweet.created_at				# date created
    text = tweet.text						# text of the tweet
    text = unidecode.unidecode(text) 
    retweets = tweet.retweet_count			# number of retweets
    username  = tweet.user.name            	# user name
    userid  = tweet.user.id              	# userid
    followers = tweet.user.followers_count 	# number of user followers
    friends = tweet.user.friends_count      # number of user friends
    
	# use TextBlob to determine polarity and subjectivity of tweet
    text_blob = TextBlob(text)
    polarity = text_blob.polarity
    subjectivity = text_blob.subjectivity
    
	# write tweet info to .csv tile
    csvWriter.writerow([username, userid, created, text, retweets, followers, 
    	friends, polarity, subjectivity])

csvFile.close()

# create a .csv file to hold the results from user's second search term, and write the header line
csvFile = open('twitter_results2.csv','w')
csvWriter = csv.writer(csvFile)
csvWriter.writerow(["username","userid","created", "text", "retweets", "followers",
    "friends","polarity","subjectivity"])

# do the twitter search on second term
for tweet in tweepy.Cursor(api.search, q = search_term2, lang = "en", 
		result_type = "popular").items(search_max):
		
    created = tweet.created_at				# date created
    text = tweet.text						# text of the tweet
    text = unidecode.unidecode(text) 
    retweets = tweet.retweet_count			# number of retweets
    username  = tweet.user.name            	# user name
    userid  = tweet.user.id              	# userid
    followers = tweet.user.followers_count 	# number of user followers
    friends = tweet.user.friends_count      # number of user friends
    
	# use TextBlob to determine polarity and subjectivity of tweet
    text_blob = TextBlob(text)
    polarity = text_blob.polarity
    subjectivity = text_blob.subjectivity
    
	# write tweet info to .csv tile
    csvWriter.writerow([username, userid, created, text, retweets, followers, 
    	friends, polarity, subjectivity])

csvFile.close()

#analyze the data stored in the two csv files to find polarization scores for the two search terms
def analyze_results():
    #open and read the files twitter_results1.csv and twitter_results2.csv
    file1 = open("twitter_results1.csv");
    csv_file1 = csv.reader(file1);
    file2 = open("twitter_results2.csv");
    csv_file2 = csv.reader(file2);

    #initialize polarization arrays, one for each csv file
    polarizing1 = [];
    polarizing2 = []
    
    #skips over the column titles for ease of analysis of data
    next(csv_file1);
    next(csv_file2);

    #iterate through the csv file and store all polarization scores
    for row in csv_file1:
        polarizing1.append(row[7]);
    for row in csv_file2:
        polarizing2.append(row[7]);
        
    #output the max and min polarizations for each array    
    print("The tweets about", search_term1, "with the most positive polarization had a score of ", max(polarizing1));
    print("The tweets about", search_term2, "with the most positive polarization had a score of ", max(polarizing2));
    
    print("The tweets about", search_term1, "with the most negative polarization had a score of ", min(polarizing1));
    print("The tweets about", search_term2, "with the most negative polarization had a score of ", min(polarizing2));
    
    #close the file
    file1.close();
    file2.close();

    
analyze_results();