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

🔍 How It Works
User inputs a URL

extract_features() extracts characteristics (length, presence of @, hyphens, etc.)

The trained model predicts Phishing or Legitimate

SHAP explains which features contributed to the decision via a waterfall plot

🖼️ Example Output
⚠️ URL flagged as Phishing

✅ URL marked as Legitimate

🔍 SHAP Plot visualizes top features influencing decision
![image](https://github.com/user-attachments/assets/40ec003e-808e-49b8-b4a5-fa5617a47a29)
