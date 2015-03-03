#This bot is created for educational purposes. It is made for the IACD course at CMU, spring 2015.
#It makes use of several Temboo libraries and could not have existed without it.
#Thomas Langerak, www.thomaslangerak.nl

import time
from temboo.Library.Twitter.Timelines import LatestMention
from temboo.Library.Twitter.Tweets import StatusesUpdate
from temboo.Library.Bitly.Links import ShortenURL
from temboo.core.session import TembooSession

# Create a session with your Temboo account details
session = TembooSession("tlangerak", "myFirstApp", "c5ae74ae20be474583c9e2c22252ed38")

# Initiate the Choreos
latestMentionChoreo = LatestMention(session)
statusesUpdateChoreo = StatusesUpdate(session)

# Get an InputSet object for the Choreos
latestMentionInputs = latestMentionChoreo.new_input_set()
statusesUpdateInputs = statusesUpdateChoreo.new_input_set()

# Set the Choreos inputs
latestMentionInputs.set_AccessToken("")
latestMentionInputs.set_AccessTokenSecret("")
latestMentionInputs.set_ConsumerSecret("")
latestMentionInputs.set_ConsumerKey("")

statusesUpdateInputs.set_AccessToken("")
statusesUpdateInputs.set_AccessTokenSecret("")
statusesUpdateInputs.set_ConsumerSecret("")
statusesUpdateInputs.set_ConsumerKey("")

while True:
    # get tweet
    latestMentionResults = latestMentionChoreo.execute_with_results(latestMentionInputs)
    user=latestMentionResults.get_ScreenName()
    tweet=latestMentionResults.get_Text()
    
    #analyze words
    words=tweet.split();
    question="http://en.lmgtfy.com/?q="
    
    for index in range(len(words)):
        analyze=words[index].lower()
        if analyze != "@bot_qna":
            question=question+words[index]+"+"
    
    #shorten url
    shortenURLChoreo = ShortenURL(session)
    shortenURLInputs = shortenURLChoreo.new_input_set()
    shortenURLInputs.set_AccessToken("")
    shortenURLInputs.set_LongURL(question)
    shortenURLResults = shortenURLChoreo.execute_with_results(shortenURLInputs)
    shortURL=shortenURLResults.get_Response()
    
    print(question)
    #tweet back
    answer="@"+user+" "+"You're welcome:"+" "+shortURL
    statusesUpdateInputs.set_StatusUpdate(answer)
    statusesUpdateResults = statusesUpdateChoreo.execute_with_results(statusesUpdateInputs)
    
    print("done")
    time.sleep(150)