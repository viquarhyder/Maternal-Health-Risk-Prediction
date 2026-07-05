from flask import Flask, render_template, request
from Prediction.predictor import predict_risk

app = Flask(__name__)


# ==========================================================
# Home
# ==========================================================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================================================
# Prediction
# ==========================================================

@app.route("/predict", methods=["GET", "POST"])
def predict():

    if request.method == "GET":
        return render_template("predict.html")

    try:

        age = float(request.form["age"])
        systolic_bp = float(request.form["systolic_bp"])
        diastolic_bp = float(request.form["diastolic_bp"])
        bs = float(request.form["bs"])
        body_temp = float(request.form["body_temp"])
        heart_rate = float(request.form["heart_rate"])

        input_data = {

            "Age": age,
            "SystolicBP": systolic_bp,
            "DiastolicBP": diastolic_bp,
            "BS": bs,
            "BodyTemp": body_temp,
            "HeartRate": heart_rate

        }

        prediction = predict_risk(input_data)

        prediction_lower = prediction.lower()

        # --------------------------------------------------
        # Risk Messages
        # --------------------------------------------------

        if prediction_lower == "low risk":

            risk_level_class = "success"

            risk_message = (
                "Patient is classified as LOW RISK. "
                "Continue routine antenatal check-ups, maintain a healthy diet, "
                "stay hydrated, and follow your doctor's advice."
            )

        elif prediction_lower == "mid risk":

            risk_level_class = "warning"

            risk_message = (
                "Patient is classified as MEDIUM RISK. "
                "Closer monitoring and consultation with a healthcare professional "
                "is recommended."
            )

        elif prediction_lower == "high risk":

            risk_level_class = "danger"

            risk_message = (
                "Patient is classified as HIGH RISK. "
                "Immediate medical evaluation is strongly recommended. "
                "Please consult an obstetrician as soon as possible."
            )

        else:

            risk_level_class = "secondary"

            risk_message = (
                "Prediction generated successfully."
            )

        return render_template(

            "result.html",

            prediction=prediction,

            risk_message=risk_message,

            risk_level_class=risk_level_class,

            input_data=input_data

        )

    except Exception as e:

        return render_template(

            "predict.html",

            error=str(e)

        )


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":
    app.run(debug=True)