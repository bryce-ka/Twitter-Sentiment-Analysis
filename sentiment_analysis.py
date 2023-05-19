"""
This program performs a sentiment analysis on tweets about a user entered keyword.

Authors: Bryce Anthony, Isaac Bynum

"""

#import neccesary functions 
from csc121.twitter import get_tweets, pretty_print


def word_valence():
  """
  creates the word_valence dictionary from AFIN-111.txt

  parameters:
    none
  returns:
    a dictionay with an iteger value representing the sentiment of each key  
  """
  valence_dict = {}

  with open("AFINN-111.txt", "r") as in_file:
    for line in in_file:
      split_line = line.split()
      valence_dict[split_line[0]] = split_line[1]
  
  
  return valence_dict
  
  
  


def compute_sent(each_tweet):
  """
  uses the dictionary created from AFIN-111.txt and computes the sentiment of each tweet 

  Parameters:
    each_tweet - a string containing each tweet from the adjust_tweets function.
  Returns:
    returns the sentiment of each tweet based on the AFINN-111.txt
  """
  v_dict = word_valence()
  tweet_sum = 0 
  each_tweet = each_tweet.split()
  num_words = len(each_tweet)

  
  for each_word in each_tweet:
    try:
      tweet_sum = tweet_sum + int(v_dict[each_word])
    except KeyError:
      tweet_sum = tweet_sum + 0
   

  tweet_sent = tweet_sum
  
  return(tweet_sent)
  


    

def adjust_tweet(tweets):
  """
  creates a list of lowercased versions of each tweet.
  and computes the sentiment of each tweet 
  
  parameters:
    Tweets- tweets that contain the keyword inputted by the user 
  returns:
    tweet_sent_list- a list of the sentiments of each tweet with the keyword in it.
  """
  tweet_sent_lst = []

  for i in range(len(tweets["statuses"])):
    each_tweet =  str.lower((tweets["statuses"][i]["text"]))
    #print()
    #print(tweets["statuses"][i]["text"])
    #tweet_lst.append(each_tweet)
    indiv_sent = compute_sent(each_tweet)
    #print(indiv_sent)
    tweet_sent_lst.append(indiv_sent)

  return(tweet_sent_lst)


def keyword_sent(lst):
  """
  computes the sentiment of all tweets by averaging th esentiment of each tweet.
  parameters:
    lst - a list of the sentiment values of each tweet.
  returns:
    the average sentiment of all tweets 
  """
  if len(lst) > 1:
    #print(sum(lst))
    #print(len(lst))
    sent = sum(lst)/len(lst) 
  else:
    sent = 0
    
  return(sent)

    
  

def analyze_tweets(keyword):
  """
  computes the average sentiments of tweets around a given keyword 
  
  parameters:
    keyword- a user specified word or phrase used to seach for tweets 
  returns:
    he average sentiment of all tweets 
  """
  try:
    tweets = get_tweets(keyword)
  
    lst = adjust_tweet(tweets)
    sent = keyword_sent(lst)

  except IOError:
    print("something went wrong please try again")
    return 0
   
  #try:
    # format to get tweet:
    # pretty_print(tweets["statuses"][3]["text"])
    # [3] can be any number less than 20 since there are only 20 cached tweets 
    # ["text"] references the actual text of the tweet
    
  
  return sent

def main():
  #(keyword):
  keyword = input("enter a keyword: ")
  
  #print(analyze_tweets(keyword))

if __name__ == "__main__":
  main()
