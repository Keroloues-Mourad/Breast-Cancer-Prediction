# 🩺 Breast_Cancer_Prediction  
Modern web app that predicts whether a breast tumor is **Benign** or **Malignant**  

💡 Breast Cancer Predictor  

This is an interactive and modern web application designed to help doctors and researchers predict breast cancer outcomes.  
It leverages a trained **machine learning model** built on breast cancer patient data.  

The app allows users to upload patient data (CSV) or use **ready-made sample cases** and provides real-time predictions with clear visual indicators and probability percentages.  

---

## 🚀 Features  

- 📊 Predicts whether a tumor is **Benign ✅** or **Malignant ⚠️**  
- 📂 Upload patient data via **CSV** or use built-in sample cases  
- 🎨 Clean and intuitive web interface (Streamlit)  
- 📈 Displays prediction results with **percentage confidence**  
- 💾 Option to **download predictions** as a CSV file  
- 🧠 Backend model: **Random Forest Classifier** (best performing)  

---

## 🗂️ Project Structure  

```bash
.
├── app.py                     # Streamlit UI App
├── Main_Code.ipynb            # Jupyter notebook: data analysis + model training
├── breast_cancer_model.pkl    # Trained ML model
├── Template.csv               # Input data template
├── samples/                   # Example patient data files
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

## 📬 Try It Online  

👉  [Launch the app on Streamlit](https://stay-or-churn-analyzer-by-keroloues-mourad.streamlit.app/)

---

## 📊 Dataset Info  

This model is trained on a breast cancer dataset containing key features from patient records.  
The dataset includes tumor characteristics (e.g., size, texture, compactness) and ground-truth labels (**Benign** or **Malignant**).  

---

## 🧠 Model Summary  

We tested two machine learning models:  

- 🔹 **Logistic Regression** – simple baseline model  
- 🔹 **Random Forest Classifier** – chosen as the final model  

✅ Final Choice: **Random Forest** because it achieved:  
- **Recall:** 94%  
- **Accuracy:** 97%  

---

**Created by Keroloues Mourad**
