
import pandas as pd
from pathlib import Path
import nltk
from nltk.stem import WordNetLemmatizer

# Define the input and output folders
input_dir = Path("data/raw")
output_dir = Path("data/processed")
output_dir.mkdir(parents=True, exist_ok=True)

# Map the original labels to your three target emotions
label_mapping = {
    0: "Sad",
    1: "Happy",
    3: "Angry"
}
lemmatizer = WordNetLemmatizer()

# Basic text preprocessing
def preprocess_text(text):
    if not isinstance(text, str):
        return ""

    text = text.lower()
    text = text.strip()
    text = " ".join(text.split())

    words = text.split()
    words = [
        lemmatizer.lemmatize(word, pos="v")
        for word in words
    ]

    return " ".join(words)


print("\nPreprocessing completed!")
