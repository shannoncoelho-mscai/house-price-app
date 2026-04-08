from fastapi import FastAPI
import pickle
import numpy as np
import os
import logging
import uvicorn

# Logging
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

app = FastAPI()

# Load model
model_path = os.path.join(os.path.dirname(__file__), "..", "model.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

@app.get("/")
def home():
    return {"message": "House Price Prediction API"}

@app.post("/predict")
def predict(area: float, bedrooms: int, bathrooms: int):

    logging.info(f"Input: {area}, {bedrooms}, {bathrooms}")

    features = np.array([[area, bedrooms, bathrooms]])
    prediction = model.predict(features)[0]

    logging.info(f"Prediction: {prediction}")

    return {"predicted_price": float(prediction)}


# 👇 THIS PART FIXES YOUR ISSUE (keeps container running)
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=5000)

