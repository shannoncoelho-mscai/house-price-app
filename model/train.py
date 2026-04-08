import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle


file_path = os.path.join(os.path.dirname(__file__), "..", "housing_data.csv")
df = pd.read_csv(file_path)

print(df.columns)  # check columns

# Example (EDIT THIS BASED ON YOUR DATASET)
X = df[['area', 'bedrooms', 'bathrooms']]
y = df['price']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained successfully")