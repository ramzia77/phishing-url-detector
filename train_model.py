# train_model.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import os
import joblib
from utils.feature_extractor import extract_features

# Load raw dataset
df = pd.read_csv("combined_dataset.csv")


# Clean labels
df.columns = [col.strip().lower() for col in df.columns]
df = df.dropna()

if 'status' not in df.columns or 'url' not in df.columns:
    raise ValueError("CSV must contain 'url' and 'status' columns.")

# Convert status to binary label
df['status'] = df['status'].apply(lambda x: 1 if str(x).lower().strip() == 'phishing' else 0)

# Extract features
features = []
labels = []

print("✅ Extracting features from all URLs...")
for _, row in df.iterrows():
    url = row['url']
    label = row['status']
    feature_row = extract_features(url)
    if not feature_row.empty:
        features.append(feature_row)
        labels.append(label)

# Combine feature rows
X = pd.concat(features, ignore_index=True)
y = pd.Series(labels)

# Save feature names
feature_names = list(X.columns)
os.makedirs("model", exist_ok=True)
joblib.dump(feature_names, "model/feature_names.pkl")

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print("✅ Accuracy:", accuracy_score(y_test, y_pred))
print("✅ Classification Report:\n", classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "model/phishing_model.pkl")
print("✅ Model and feature names saved.")
