
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the preprocessed training dataset
train_df = pd.read_csv("data/processed/train.csv")

# Separate text and emotion labels
X_train = train_df["text"].fillna("")
y_train = train_df["emotion"]

# Create the TF-IDF vectorizer
tfidf = TfidfVectorizer(
    max_features=5000,
    ngram_range=(1, 2)
)

# Convert text into numerical features
X_train_tfidf = tfidf.fit_transform(X_train)

# Display the results
print("TF-IDF FEATURE EXTRACTION RESULTS")
print("-" * 40)
print("Number of text records:", X_train_tfidf.shape[0])
print("Number of TF-IDF features:", X_train_tfidf.shape[1])
print("Feature matrix shape:", X_train_tfidf.shape)

# Display some extracted feature names
print("\nSample TF-IDF features:")
print(tfidf.get_feature_names_out()[:20])

# Display numerical values for the first sentence
print("\nTF-IDF values for the first sentence:")
print(X_train_tfidf[0].toarray())
