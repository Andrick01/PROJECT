
import joblib

# Load the saved model pipeline
model = joblib.load("models/emotion_classifier.joblib")

print("Emotion Analyzer")
print("Type 'exit' to stop.")

while True:
    text = input("\nEnter feedback: ").strip()

    if text.lower() == "exit":
        break

    if not text:
        print("Please enter some text.")
        continue

    # Predict emotion
    emotion = model.predict([text])[0]

    # Show prediction confidence estimates
    probabilities = model.predict_proba([text])[0]
    classes = model.classes_
    confidence = probabilities[list(classes).index(emotion)] * 100

    print("Predicted emotion:", emotion)
    print(f"Model confidence estimate: {confidence:.2f}%")
