import os
import pickle
import pandas as pd

# ==========================================================
# Paths
# ==========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "Model", "ann.pkl")

# ==========================================================
# Load Model
# ==========================================================

print("=" * 60)
print("Loading Maternal Health ANN Model...")
print("=" * 60)

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)

print("Model Loaded Successfully!")
print("=" * 60)


# ==========================================================
# Feature Engineering
# (Must be SAME as Training Notebook)
# ==========================================================

def preprocess_input(df):

    df = df.copy()

    eps = 1e-3

    # Pulse Pressure
    df["PulsePressure"] = (
        df["SystolicBP"] -
        df["DiastolicBP"]
    )

    # Blood Pressure Ratio
    df["BPRatio"] = (
        df["SystolicBP"] /
        (df["DiastolicBP"] + eps)
    )

    # Blood Sugar × Heart Rate
    df["BS_HR_Interaction"] = (
        df["BS"] *
        df["HeartRate"]
    )

    # Age × Systolic BP
    df["Age_SystolicBP"] = (
        df["Age"] *
        df["SystolicBP"]
    )

    return df


# ==========================================================
# Prediction Function
# ==========================================================

def predict_risk(input_dict):

    df = pd.DataFrame([input_dict])

    df = preprocess_input(df)

    prediction = model.predict(df)[0]

    return str(prediction)


# ==========================================================
# Local Testing
# ==========================================================

if __name__ == "__main__":

    sample = {

        "Age": 28,
        "SystolicBP": 130,
        "DiastolicBP": 85,
        "BS": 7.2,
        "BodyTemp": 98.5,
        "HeartRate": 92

    }

    result = predict_risk(sample)

    print()
    print("=" * 60)
    print("Predicted Risk Level :", result)
    print("=" * 60)