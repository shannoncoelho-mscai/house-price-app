# House Price Prediction App

A machine learning application that predicts house prices based on property details such as area, number of bedrooms, and number of bathrooms. The trained model is served through a FastAPI REST API and can be run locally or inside a Docker container.

## Features

- Predicts house prices from property inputs.
- Uses a saved machine learning model (`model.pkl`).
- Provides a REST API built with FastAPI.
- Logs prediction inputs and outputs.
- Supports Docker-based execution.

## Tech Stack

- Python
- FastAPI
- NumPy
- Scikit-learn
- Joblib / Pickle
- Uvicorn
- Docker

## Project Structure

```text
house-price-app/
│
├── app/
│   └── main.py          # FastAPI application and prediction endpoint
├── model/
├── model.pkl            # Trained machine learning model
├── housing_data.csv     # Housing dataset
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker configuration
└── app.log              # Application log file
```

## How It Works

1. The application loads the trained model from `model.pkl`.
2. A user submits the property's area, number of bedrooms, and number of bathrooms.
3. The API converts these inputs into the feature format expected by the model.
4. The model predicts the house price.
5. The API returns the predicted price as a JSON response.

## Getting Started

### Prerequisites

- Python 3.9 or later
- pip
- Git

### 1. Clone the repository

```bash
git clone https://github.com/shannoncoelho-mscai/house-price-app.git
cd house-price-app
```

### 2. Create and activate a virtual environment

**Windows PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the API

From the repository root, run:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 5000 --reload
```

The API will be available at:

- Root endpoint: http://localhost:5000/
- Interactive API documentation: http://localhost:5000/docs

## API Usage

### Check API status

**GET** `/`

Example response:

```json
{
  "message": "House Price Prediction API"
}
```

### Predict a house price

**POST** `/predict`

The endpoint accepts the following query parameters:

| Parameter | Type | Description |
|---|---|---|
| `area` | float | Area of the property |
| `bedrooms` | integer | Number of bedrooms |
| `bathrooms` | integer | Number of bathrooms |

Example request:

```text
POST http://localhost:5000/predict?area=1200&bedrooms=3&bathrooms=2
```

Example response:

```json
{
  "predicted_price": 4500000.0
}
```

The response value above is illustrative; the actual prediction depends on the trained model and input values.

## Running with Docker

### 1. Build the image

```bash
docker build -t house-price-app .
```

### 2. Run the container

```bash
docker run -p 5000:5000 house-price-app
```

Open http://localhost:5000/docs to try the API.

## Author

**Shannon Coelho**

- GitHub: [@shannoncoelho-mscai](https://github.com/shannoncoelho-mscai)
- Repository: [house-price-app](https://github.com/shannoncoelho-mscai/house-price-app)
