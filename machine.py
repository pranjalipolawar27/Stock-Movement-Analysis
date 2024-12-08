import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load data from CSV
data = pd.read_csv('cleaned_tweets.csv')  # Replace 'features.csv' with your actual CSV file name

# Assuming the CSV has columns like 'sentiment_polarity', 'mentions_count', and 'stock_movement_label'
X = data[['sentiment_polarity', 'mentions_count']]  # Feature columns
y = data['stock_movement_label']  # Target column

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Build and train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Test the model
y_pred = model.predict(X_test)
print(f"Model Accuracy: {accuracy_score(y_test, y_pred)}")
