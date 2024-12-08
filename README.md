# Stock Market Sentiment and Prediction Project

This project scrapes data from Twitter accounts discussing the stock market, cleans and preprocesses the data, performs sentiment analysis, extracts features, and builds a machine learning model to predict stock movements based on sentiment and key indicators.

## Dependencies and Setup
1. Ensure you have Python 3.8 or higher installed.  
2. Install required libraries using the following command:  
   ```bash
   pip install tweepy pandas nltk scikit-learn

## Download the NLTK Vader lexicon by running:

Copy code
import nltk
nltk.download('vader_lexicon')

How to Run:
**Data Scraping:** Open the main.py script, replace the bearer_token variable with your Twitter API bearer token, and run the script to save tweets into twitter1.csv.

**Data Cleaning**: Run the data_clean.py script to clean the scraped tweets and save them into cleaned_tweets.csv.

**Sentiment Analysis**: Execute sentiment_analysis.py to perform sentiment analysis and save results into sentiment_tweets.csv.

**Feature Extraction**: Run feature_extraction.py to extract stock mentions from tweets and analyze their frequency.

**Model Training:** Run ml_model.py to train the Random Forest classifier and evaluate its accuracy on the test set.

**Example Workflow**:
Start by running main.py to scrape tweets.
Then, clean the tweets with data_clean.py.
Perform sentiment analysis using sentiment_analysis.py.
Extract features with feature_extraction.py.
Finally, train and evaluate the prediction model using ml_model.py.

**Output**
The final machine learning model will output accuracy metrics and a classification report showing the precision, recall, and F1 score for predicting stock movements
