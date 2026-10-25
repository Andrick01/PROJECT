
import numpy as np
import pyttsx3

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# ------------------------------------------
# 1. FAQ DATASET
# ------------------------------------------

faqs = [
    {
        "question": "What is this chatbot?",
        "answer": (
            "This is an FAQ chatbot that uses sentence embeddings "
            "to find answers and text to speech to speak them aloud."
        )
    },
    {
        "question": "How do I reset my password?",
        "answer": (
            "To reset your password, open Settings, select Security, "
            "and choose Reset Password."
        )
    },
    {
        "question": "How can I contact customer support?",
        "answer": (
            "You can contact customer support by emailing "
            "support@example.com."
        )
    },
    {
        "question": "What are your working hours?",
        "answer": (
            "Our working hours are 9 AM to 5 PM, Monday to Friday."
        )
    },
    {
        "question": "How do I create a new account?",
        "answer": (
            "Open the registration page, enter your details, "
            "and follow the instructions to create an account."
        )
    },
    {
        "question": "How can I change my username?",
        "answer": (
            "Open your account settings, select Profile, "
            "and update your username."
        )
    },
    {
        "question": "How do I check my order status?",
        "answer": (
            "Open the Orders section of your account and select "
            "your order to view its current status."
        )
    },
    {
        "question": "What is your refund policy?",
        "answer": (
            "Please contact customer support with your order details "
            "to learn about refund eligibility and the applicable policy."
        )
    },
    {
        "question": "How can I delete my account?",
        "answer": (
            "Open account settings and look for the account deletion "
            "option. Contact support if you need assistance."
        )
    },
    {
        "question": "How do I update my email address?",
        "answer": (
            "Open your profile settings, update your email address, "
            "and complete any verification steps requested."
        )
    }
]


# ------------------------------------------
# 2. LOAD THE SENTENCE EMBEDDING MODEL
# ------------------------------------------

print("Loading the sentence embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

faq_questions = [faq["question"] for faq in faqs]

# Convert all FAQ questions into embeddings once.
faq_embeddings = model.encode(
    faq_questions,
    convert_to_numpy=True,
    normalize_embeddings=True
)

print("FAQ chatbot is ready!")


# ------------------------------------------
# 3. INITIALIZE TEXT-TO-SPEECH
# ------------------------------------------

try:
    tts_engine = pyttsx3.init()
    tts_engine.setProperty("rate", 165)
    tts_engine.setProperty("volume", 1.0)
except Exception as error:
    tts_engine = None
    print("Warning: TTS initialization failed:", error)


def speak(text):
    """Speak the given text using the local TTS engine."""
    if tts_engine is None:
        print("Speech is unavailable. Please check your TTS setup.")
        return

    try:
        tts_engine.say(text)
        tts_engine.runAndWait()
    except Exception as error:
        print("Could not speak the answer:", error)


# ------------------------------------------
# 4. FIND THE BEST FAQ ANSWER
# ------------------------------------------

def get_answer(user_question):
    """Return the best FAQ match, or reject a weak match."""

    # Convert the user's question into an embedding.
    question_embedding = model.encode(
        [user_question],
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    # Compare it against every stored FAQ embedding.
    scores = cosine_similarity(
        question_embedding,
        faq_embeddings
    )[0]

    # Find the FAQ with the highest similarity.
    best_index = int(np.argmax(scores))
    best_score = float(scores[best_index])

    # Starting threshold: tune it using test questions.
    threshold = 0.40

    if best_score < threshold:
        return (
            "Sorry, I could not find a suitable answer. "
            "Please try asking in a different way or contact support."
        ), best_score, None

    best_faq = faqs[best_index]

    return best_faq["answer"], best_score, best_faq["question"]


# ------------------------------------------
# 5. CHATBOT LOOP
# ------------------------------------------

def main():
    print("\n================================")
    print("      FAQ CHATBOT WITH TTS")
    print("================================")
    print("Ask a question or type 'exit' to quit.")

    while True:
        user_question = input("\nYou: ").strip()

        if user_question.lower() in {"exit", "quit"}:
            print("Bot: Thank you for using the FAQ chatbot!")
            speak("Thank you for using the FAQ chatbot!")
            break

        if not user_question:
            print("Bot: Please enter a question.")
            continue

        answer, score, matched_question = get_answer(user_question)

        if matched_question is not None:
            print("Matched FAQ:", matched_question)

        print(f"Similarity score: {score:.3f}")
        print("Bot:", answer)

        # Speak the same answer that is displayed.
        speak(answer)


if __name__ == "__main__":
    main()
