from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Define features (X) and target variable (y)
X = df.drop(columns=["Crop"])  # Features
y = df["Crop"]  # Target variable

# Split data into train (80%) and test (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a K-Nearest Neighbors classifier
crop_classifier = KNeighborsClassifier(n_neighbors=5)
crop_classifier.fit(X_train, y_train)

# Evaluate model
y_pred = crop_classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")
