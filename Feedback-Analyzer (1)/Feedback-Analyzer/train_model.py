
import pandas as pd
import joblib
from pathlib import Path
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load the preprocessed datasets
train_df = pd.read_csv("data/processed/train.csv")
val_df = pd.read_csv("data/processed/validation.csv")

# Prepare training data
X_train = train_df["text"].fillna("")
y_train = train_df["emotion"]

# Prepare validation data
X_val = val_df["text"].fillna("")
y_val = val_df["emotion"]

# Create the complete ML pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer(
        max_features=5000,
        ngram_range=(1, 2)
    )),
    ("classifier", LogisticRegression(
        max_iter=1000,
        class_weight="balanced"
    ))
])

# Train the model
print("Training the emotion classification model...")
model.fit(X_train, y_train)

# Evaluate on validation data
y_pred = model.predict(X_val)

print("\nVALIDATION RESULTS")
print("-" * 40)
print("Accuracy:", round(accuracy_score(y_val, y_pred), 4))
print("\nClassification Report:")
print(classification_report(y_val, y_pred, zero_division=0))

# Save the trained model
model_dir = Path("models")
model_dir.mkdir(parents=True, exist_ok=True)

joblib.dump(model, model_dir / "emotion_classifier.joblib")

print("Model saved to models/emotion_classifier.joblib")

