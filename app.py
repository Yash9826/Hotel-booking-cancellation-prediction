
# # main code 

# from flask import Flask, request, jsonify
# import joblib
# import pandas as pd
# import google.generativeai as genai

# # Load model
# model = joblib.load("hotel_model.pkl")

# # Configure Gemini
# GEMINI_API_KEY = "AIzaSyDl7JdG5QAd1E69esiczdowzW4aPIbiN6k"
# genai.configure(api_key=GEMINI_API_KEY)
# gemini_model = genai.GenerativeModel("gemini-1.5-flash")

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Hotel Booking Cancellation Prediction API"

# @app.route("/chat", methods=["POST"])
# def chat():
#     try:
#         data = request.get_json()
#         features = data.get("features", {})

#           # Convert input to DataFrame
#         input_data = pd.DataFrame([features])


#          # --- Handle missing columns ---
#         prep = model.named_steps['preprocessor']  # ColumnTransformer from your pipeline
#         numeric_cols = prep.transformers_[0][2]   # numeric columns
#         categorical_cols = prep.transformers_[1][2]  # categorical columns
#         training_columns = numeric_cols + categorical_cols

#         # Fill missing columns with defaults
#         for col in training_columns:
#             if col not in input_data.columns:
#                 if col in numeric_cols:
#                     input_data[col] = 0        # default numeric
#                 else:
#                     input_data[col] = "Unknown"  # default categorical



#         # Predict
#         prediction = model.predict(input_data)[0]
#         proba = model.predict_proba(input_data)[0][1]

#         # Generate explanation
#         prompt = f"""
#         Booking details: {features}.
#         Model prediction: {"Cancelled" if prediction == 1 else "Not Cancelled"}
#         Probability of cancellation: {proba:.2f}.
#         Please explain in simple terms why this prediction makes sense.
#         """
#         response = gemini_model.generate_content(prompt)

#         return jsonify({
#             "prediction": int(prediction),
#             "probability": float(proba),
#             "explanation": response.text
#         })

#     except Exception as e:
#         return jsonify({"error": str(e)})

# if __name__ == "__main__":
#     app.run(port=5000, debug=True)








#code with simple
from flask import Flask, request, jsonify
import joblib
import google.generativeai as genai
import pandas as pd

# Load trained model
model = joblib.load("hotel_model.pkl")

# Setup Gemini (optional explanation)
GEMINI_API_KEY = "AIzaSyDl7JdG5QAd1E69esiczdowzW4aPIbiN6k"
genai.configure(api_key=GEMINI_API_KEY)
gemini_model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)

@app.route("/")
def home():
    return "Hotel Booking Prediction API is running!"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        features = data.get("features", {})

        input_values = pd.DataFrame([features])

        # --- Handle missing columns ---
        prep = model.named_steps['preprocessor']  # ColumnTransformer from your pipeline
        numeric_cols = prep.transformers_[0][2]   # numeric columns
        categorical_cols = prep.transformers_[1][2]  # categorical columns
        training_columns = numeric_cols + categorical_cols

        # Fill missing columns with defaults
        for col in training_columns:
            if col not in input_values.columns:
                if col in numeric_cols:
                    input_values[col] = 0        # default numeric
                else:
                    input_values[col] = "Unknown"  # default categorical



        # Predict
        prediction = model.predict(input_values)[0]
        proba = model.predict_proba(input_values)[0][1]

        # Explanation (Gemini)
        prompt = f"""
        Booking details: {features}.
        Prediction: {"Cancelled" if prediction==1 else "Not Cancelled"}.
        Probability: {proba:.2f}.
        Explain in simple words why this might happen.
        """
        response = gemini_model.generate_content(prompt)

        return jsonify({
            "prediction": int(prediction),
            "probability": float(proba),
            "explanation": response.text
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
