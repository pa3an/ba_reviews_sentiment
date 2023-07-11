
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd
from textblob import TextBlob
from google.colab import files
import matplotlib.pyplot as plt
import seaborn as sns

ba_reviews = files.upload()

file_name = 'british_airways_reviews.csv'

# Read the uploaded CSV file into a DataFrame
ba_reviews_df = pd.read_csv(file_name)

# Concatenate all reviews into a single string
text = ' '.join(ba_reviews_df['Review'].values)

# Create the WordCloud object
wordcloud = WordCloud(width=400, height=800, background_color='white').generate(text)

# Plot the WordCloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.savefig('wordcloud.jpg')
plt.show()

# Perform sentiment analysis on each review
ba_reviews_df['Sentiment'] = ba_reviews_df['Review'].apply(lambda x: TextBlob(x).sentiment.polarity)

# Display the updated DataFrame with the sentiment scores
print(ba_reviews_df.head())

# Plot a histogram of the sentiment scores
plt.figure(figsize=(10, 5))
plt.hist(ba_reviews_df['Sentiment'], bins=20, edgecolor='black')
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')
plt.title('Sentiment Analysis')
plt.savefig('hist.jpg')
plt.show()

# Create a box plot of the sentiment scores
plt.figure(figsize=(8, 6))
sns.boxplot(data=ba_reviews_df, y='Sentiment')
plt.ylabel('Sentiment Score')
plt.title('Sentiment Analysis')
plt.savefig('boxplot.jpg')  # Save the box plot as JPEG
plt.show()

# Compute statistics on the sentiment scores
sentiment_stats = ba_reviews_df['Sentiment'].describe()
print(sentiment_stats)

