# phishing-url-detector
# 🛡️ CyberShield – Phishing URL Detection with SHAP Explainability

A machine learning-powered Flask web app that detects phishing URLs and visually explains **why** it flagged a website using **SHAP (SHapley Additive exPlanations)**. Ideal for cybersecurity awareness, education, and threat analysis.

---

## 🚀 Features

- 🔍 Predicts whether a given URL is **Phishing** or **Legitimate**
- 🧠 Powered by a trained ML model (e.g. Random Forest)
- 📊 SHAP Explainability: Visualizes which features influenced the prediction
- 🎨 Cybersecurity-themed UI (styled with `style.css`)
- 🧪 Includes custom feature extractor for URL analysis

---

## 📁 Project Structure
phishing-detector/ 
├── app.py
├── dataset_phishing.csv 
├── train_model.py 
├── utils/ │ 
           └── feature_extractor.py
├── model/ │ 
           ├── phishing_model.pkl 
           │ └── feature_names.pkl 
├── static/ 
 │ └── style.css 
 ├── templates/ 
            │ └── index.html 

