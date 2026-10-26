
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

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


# Test sentences
sentences = [
    "I AM RUNNING happily",
    "She was crying yesterday",
    "They are playing outside",
    "I   am   HAPPY"
]

print("NLP PREPROCESSING RESULTS")
print("-" * 60)

for sentence in sentences:
    processed = preprocess_text(sentence)

    print("Original text:    ", repr(sentence))
    print("Processed text:   ", repr(processed))
    print("-" * 60)
