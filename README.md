ba_reviews_sentiment
Sentiment analysis of ba reviews

This project looks at online reviews of British Airways.
The reviews are first scraped with BeautifulSoup from Skytrax (to keep it simple, only the first 100 pages were scraped).
After turning the csv file into a pandas dataframe, a wordcloud was created with, oddly enough, WordCloud.
Finally, sentiment analysis was carried oud with TextBlob. The scores were displayed numerically,
as well as with a boxplot and a histogram.
For the record, most reviews were neutral, with score close to 0.
The scraped reviews' csv file is included.
