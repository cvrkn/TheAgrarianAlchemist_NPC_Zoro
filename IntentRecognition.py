import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the preprocessed dataset
df = pd.read_csv("Processed_Crop_Data.csv")

# Example intents for chatbot
intent_data = {
    "intent": ["crop_recommendation", "weather_impact", "soil_suitability", "market_price", "fertilizer_advice"],
    "example_queries": [
        "Which crop is best for black soil?",
        "How will rain affect my wheat crop?",
        "Is laterite soil good for rice?",
        "What is the current price of sugarcane?",
        "How much fertilizer should I use for potatoes?"
    ]
}

intent_df = pd.DataFrame(intent_data)

# NLP model for intent classification
nlp = spacy.load("en_core_web_sm")
vectorizer = TfidfVectorizer()

# Prepare data for training
X = vectorizer.fit_transform(intent_df["example_queries"])
y = intent_df["intent"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X_train, y_train)

# Test model accuracy
y_pred = classifier.predict(X_test)
print("Intent Recognition Accuracy:", accuracy_score(y_test, y_pred))

def predict_intent(user_input):
    """Predict the intent of a user query."""
    transformed_input = vectorizer.transform([user_input])
    return classifier.predict(transformed_input)[0]

# Example usage
user_query = "Which crop grows best in Kharif season?"
print("Predicted Intent:", predict_intent(user_query))
