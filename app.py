from flask import Flask, render_template, request
import joblib
import pandas as pd
import shap
import matplotlib.pyplot as plt
import os
from utils.feature_extractor import extract_features
import uuid

app = Flask(__name__)

# Load model and feature names
try:
    model = joblib.load("phishing_model.pkl")
    feature_names = joblib.load("feature_names.pkl")
    print("✅ Model and feature names loaded.")
except Exception as e:
    model = None
    feature_names = None
    print(f"❌ Error loading model or feature names: {e}")

# Initialize SHAP explainer with dummy background
explainer = None
try:
    if model is not None and feature_names is not None:
        dummy_bg = pd.DataFrame([[0] * len(feature_names)], columns=feature_names)
        explainer = shap.TreeExplainer(model, data=dummy_bg)
        print("✅ SHAP TreeExplainer initialized.")
except Exception as e:
    print(f"⚠️ Could not initialize SHAP explainer: {e}")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    probability = None
    shap_image = None
    url_input = ""

    if request.method == "POST":
        url_input = request.form.get("url")

        try:
            # Extract features
            features_df = extract_features(url_input)

            # Align features
            if feature_names:
                features_df = features_df[feature_names]

            # Predict
            pred = model.predict(features_df)[0]
            prob = model.predict_proba(features_df)[0]
            probability = max(prob)

            prediction = "🟢 Legitimate" if pred == 0 else "🔴 Phishing"

            # SHAP Explanation
            if explainer:
                shap_values = explainer.shap_values(features_df)

                plt.figure(figsize=(10, 6))
                shap.plots._waterfall.waterfall_legacy(
                    explainer.expected_value[pred],
                    shap_values[pred][0],
                    features_df.iloc[0],
                    max_display=10,
                    show=False
                )

                plt.title(f"SHAP Explanation for: {url_input}", fontsize=10)
                plt.tight_layout()

                filename = f"shap_{uuid.uuid4().hex}.png"
                shap_image_path = os.path.join("static", filename)
                plt.savefig(shap_image_path, bbox_inches="tight")
                plt.close()

                shap_image = filename

        except Exception as e:
            print(f"❌ Error during prediction or SHAP: {e}")
            prediction = "❌ An error occurred while processing the URL."

    return render_template("index.html",
                           prediction=prediction,
                           probability=probability,
                           shap_image=shap_image,
                           url=url_input)


if __name__ == "__main__":
    app.run(debug=True)
