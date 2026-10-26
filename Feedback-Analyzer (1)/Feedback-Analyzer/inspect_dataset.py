
import pandas as pd

# Load the training dataset
df = pd.read_csv("data/raw/train.csv")

# Display the first five records
print("\nFirst five records:")
print(df.head())

# Display column names
print("\nColumn names:")
print(df.columns.tolist())

# Display dataset size
print("\nDataset shape:")
print(df.shape)

# Display emotion labels
print("\nEmotion label distribution:")
print(df["label"].value_counts().sort_index())

# Display the label names
emotion_labels = [
    "sadness",
    "joy",
    "love",
    "anger",
    "fear",
    "surprise"
]

print("\nLabel mapping:")
for i, emotion in enumerate(emotion_labels):
    print(f"{i} = {emotion}")
