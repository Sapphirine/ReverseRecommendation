# ReverseRecommendation
### Big Data Analytics Final Project - Team 25 - ReverseRecommendation
========================

###remember to run the following command before development:
pip install -t lib -r requirements.txt

###If you want to try this program, you can go to this website:
http://reverse-recommendation.appspot.com/

###General Purpose
*  Find out the insight of customer's negative reviews.
*  Provide the recommendations from the negative reviews.

###Introduction
This project focused on recommending restaurants for Yelp users based on their review article. A naïve approach to build a recommendation system could just be based on user queries and star ratings. However, personal interests and preferences are difficult to identify and sometimes not even aware by consumers themselves. In this project, we build our recommendation model based on low-rating reviews. The major challenge is to identify preferences of consumers, and map it to features of products.
A crucial component in this project is to recognize the relations between information hidden in negative reviews and user preferences. In the final stage, our system generates searchable words and phrases into Yelp search API to fetch recommendation results. This step mimics human actions when our mind translates preferences into searchable keywords.

###How To Use Our Service?
   1.   Post your negative review at the location our website indicates:
   ![Imgur](http://i.imgur.com/OxwyVvS.png)

   2.   Click "Recommend for me!":
   ![Imgur](http://i.imgur.com/yxeVb6n.png?1)

   3.   Now, you can get the recommendations from our service:
   ![Imgur](http://i.imgur.com/StPYBAM.png)

   4.   As you can see, there are reversed keywords our service extracts from your review:
   ![Imgur](http://i.imgur.com/uhLwnaw.png)

   5.   Also, you can read the reviews from our servie to understand why we recommend it for you:
   ![Imgur](http://i.imgur.com/keahIHW.png)

   6.   Evenmore, you can click on the picture or the name, we will redirect you to the yelp website:
   ![Imgur](http://i.imgur.com/VHvqPhw.png)
        Here is the original Yelp Website:
   ![Imgur](http://i.imgur.com/2iNhjI8.png)


###System Work Flow
   1.   Generate the reversed keywords from the negative review
   2.   Put the reversed keywords to the Yelp API to query the result
   3.   Google App Engine get the Yelp API response
   4.   Render the recommendations & keywords to our frontend.

###Web app
In the folder named WebApp, there are two subfolders including Recommend2U and sign_in_with_twitter. Recommend2U folder contains the front-end code, servlet and database API; sign_in_with_twitter folder contains OAuth2.0 codes to allow Twitter users be redirected to Twitter and get authentication afterwards. Due to the technical error in Twitter app, the Twitter app credential may not work sometimes, please replace it with your credentials

###Google App Engine


###entry main function of recommendation on twitter side
GetFollowersIDs.java in BigDataProject/javaResources/src/cmu.arktweetnlp

This function is used for fetching tweets from our followers in nearly real time, detect desires, query products, respond with recommendations and analyze the users reviews. In order to run it, you would have to firstly include your own AWS credential and twitter credential.

###Map Reduce pattern design
The folder named Classification contains all the Map Reduce pattern designs. WordCount.java is used for constructing the dictionary. ClassWordCount.java is used for training the data set.  Sentiment.java is used for the implementing the sentiment algorithm. In order to run them, we suggest you first build the path to make your Eclipse be able to run Hadoop and then open the run configuration to set the input path and the out put path. More details will be included on the readme file on our github.
