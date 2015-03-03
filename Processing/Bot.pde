import com.temboo.core.*;
import com.temboo.Library.Twitter.Timelines.*;
import com.temboo.Library.Twitter.Tweets.*;
import com.temboo.Library.Bitly.Links.*;

String user;
String tweet;

String longURL="http://en.lmgtfy.com/?q=";
String shortURL;
String answer;


// Create a session using your Temboo account application details
TembooSession session = new TembooSession("tlangerak", "myFirstApp", "");

void setup() {
  runLatestMentionChoreo();
  runShortenURLChoreo();
  runStatusesUpdateChoreo();
}

void runLatestMentionChoreo() {

  LatestMention latestMentionChoreo = new LatestMention(session);
  latestMentionChoreo.setAccessToken("");
  latestMentionChoreo.setAccessTokenSecret("");
  latestMentionChoreo.setConsumerSecret("");
  latestMentionChoreo.setConsumerKey("");
  LatestMentionResultSet latestMentionResults = latestMentionChoreo.run();

  user = latestMentionResults.getScreenName();
  tweet = latestMentionResults.getText();

  String[] analyze = split(tweet, " ");
  for (int i=0; i<analyze.length; i++) {
    if (i==0) {
      longURL=longURL+analyze[i];
    } else {
          String str=analyze[i]; //makes sure that al captions are small for comparison. 
          str=str.toLowerCase();
      if (str.equals("@bot_qna")==false) { //dont include own name in search.
        longURL=longURL+"+"+analyze[i]; //add each word to the url as lmgtfy does. Luckily their url is easy.
      }
    }
  }
  println(longURL);
}

void runShortenURLChoreo() {
  ShortenURL shortenURLChoreo = new ShortenURL(session);
  shortenURLChoreo.setAccessToken("");
  shortenURLChoreo.setLongURL(longURL);
  ShortenURLResultSet shortenURLResults = shortenURLChoreo.run();

  shortURL = shortenURLResults.getResponse(); //shorten the URL for tweet
  answer="@"+user+" "+"You're welcome:"+" "+shortURL;
  println(answer);
}

void runStatusesUpdateChoreo() {
  StatusesUpdate statusesUpdateChoreo = new StatusesUpdate(session);  
  statusesUpdateChoreo.setAccessToken("");
  statusesUpdateChoreo.setAccessTokenSecret("");
  statusesUpdateChoreo.setConsumerSecret("");
  statusesUpdateChoreo.setConsumerKey("");

  statusesUpdateChoreo.setStatusUpdate(answer);
  StatusesUpdateResultSet statusesUpdateResults = statusesUpdateChoreo.run();
  println(statusesUpdateResults.getResponse());
}

