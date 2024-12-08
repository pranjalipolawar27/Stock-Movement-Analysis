import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


data = pd.read_csv('cleaned_tweets.csv')  

X = data[['sentiment_polarity', 'mentions_count']]  
y = data['stock_movement_label']  


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


model = RandomForestClassifier()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
print(f"Model Accuracy: {accuracy_score(y_test, y_pred)}")


from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))