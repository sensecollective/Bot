import processing.core.*; 
import processing.data.*; 
import processing.event.*; 
import processing.opengl.*; 

import com.temboo.core.*; 
import com.temboo.Library.Twitter.Timelines.*; 
import com.temboo.Library.Twitter.Tweets.*; 
import com.temboo.Library.Bitly.Links.*; 

import java.util.HashMap; 
import java.util.ArrayList; 
import java.io.File; 
import java.io.BufferedReader; 
import java.io.PrintWriter; 
import java.io.InputStream; 
import java.io.OutputStream; 
import java.io.IOException; 

public class QnA extends PApplet {






String user;
String tweet;

String longURL="http://en.lmgtfy.com/?q=";
String shortURL;
String answer;


// Create a session using your Temboo account application details
TembooSession session = new TembooSession("tlangerak", "myFirstApp", "c5ae74ae20be474583c9e2c22252ed38");

public void setup() {
  runLatestMentionChoreo();
  runShortenURLChoreo();
  runStatusesUpdateChoreo();
}

public void runLatestMentionChoreo() {

  LatestMention latestMentionChoreo = new LatestMention(session);
  latestMentionChoreo.setAccessToken("3045027399-teKCLMdkITVcDtuO64m4BtYG8j0zYKjgoVI0LaK");
  latestMentionChoreo.setAccessTokenSecret("sM2z5NrI1p0kzYds3y6ZASErLWCYIwNnESp25Yw3bYCv0");
  latestMentionChoreo.setConsumerSecret("M88VlRrRviXizl7AykhVNG8G4Aq7dje8KNp4RCWROBzIeAyj30");
  latestMentionChoreo.setConsumerKey("T3eBLoKPVh7FhKd8X7xEYoFlp");
  LatestMentionResultSet latestMentionResults = latestMentionChoreo.run();

  user = latestMentionResults.getScreenName();
  tweet = latestMentionResults.getText();

  String[] analyze = split(tweet, " ");
  for (int i=0; i<analyze.length; i++) {
    if (i==0) {
      longURL=longURL+analyze[i];
    } else {

      if ( analyze[i].equals("@Bot_QnA") == false) { //dont include own name in search.
        longURL=longURL+"+"+analyze[i]; //add each word to the url as lmgtfy does. Luckily their url is easy.
      }
    }
  }
}

public void runShortenURLChoreo() {
  ShortenURL shortenURLChoreo = new ShortenURL(session);
  shortenURLChoreo.setAccessToken("e86b2809e0738771e437c6979e3bb3110954c30d");
  shortenURLChoreo.setLongURL(longURL);
  ShortenURLResultSet shortenURLResults = shortenURLChoreo.run();

  shortURL = shortenURLResults.getResponse(); //shorten the URL for tweet
  answer="@"+user+" "+"You're welcome:"+" "+shortURL;
  println(answer);
}

public void runStatusesUpdateChoreo() {
  StatusesUpdate statusesUpdateChoreo = new StatusesUpdate(session);  
  statusesUpdateChoreo.setAccessToken("3045027399-teKCLMdkITVcDtuO64m4BtYG8j0zYKjgoVI0LaK");
  statusesUpdateChoreo.setAccessTokenSecret("sM2z5NrI1p0kzYds3y6ZASErLWCYIwNnESp25Yw3bYCv0");
  statusesUpdateChoreo.setConsumerSecret("M88VlRrRviXizl7AykhVNG8G4Aq7dje8KNp4RCWROBzIeAyj30");
  statusesUpdateChoreo.setConsumerKey("T3eBLoKPVh7FhKd8X7xEYoFlp");

  statusesUpdateChoreo.setStatusUpdate(answer);
  StatusesUpdateResultSet statusesUpdateResults = statusesUpdateChoreo.run();
  println(statusesUpdateResults.getResponse());
}

  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "QnA" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
