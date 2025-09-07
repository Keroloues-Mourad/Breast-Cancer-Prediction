import streamlit as st
import pandas as pd
import joblib

model = joblib.load("breast_cancer_model.pkl")

st.set_page_config(page_title="Breast Cancer Prediction", page_icon="🩺", layout="wide")
st.title("🩺 Breast Cancer Prediction")
st.write("Upload a CSV file with patient data or choose a **sample dataset** to predict if they are **Benign** or **Malignant**.")


st.subheader("📄 Download Patient Data Template (Doctors Only)")
template_df = pd.read_csv("K:/Breast_Cancer_Project/Template.csv")  
template_csv = template_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇️ Download Template CSV",
    data=template_csv,
    file_name="patient_template.csv",
    mime="text/csv"
)


sample_files = {
    "Case 1": "samples/case_1.csv",
    "Case 2": "samples/case_2.csv",
    "Case 3": "samples/case_3.csv"
}


option = st.radio("Select Data Source:", ["Upload CSV", "Use Sample Data"])

uploaded_file = None
patient_data = None

if option == "Upload CSV":
    uploaded_file = st.file_uploader("📂 Choose a CSV file", type="csv")
    if uploaded_file is not None:
        patient_data = pd.read_csv(uploaded_file)

elif option == "Use Sample Data":
    sample_choice = st.selectbox("Choose a sample dataset", list(sample_files.keys()))
    if sample_choice:
        patient_data = pd.read_csv(sample_files[sample_choice])
        st.success(f"Loaded {sample_choice}")


if patient_data is not None:
    st.subheader("📋 Patient Data")
    st.dataframe(patient_data)

    
    predictions = model.predict(patient_data)
    probabilities = model.predict_proba(patient_data)

    results_df = patient_data.copy()
    results_df["Prediction"] = ["Benign" if pred == 0 else "Malignant" for pred in predictions]
    results_df["Probability (%)"] = [round(max(prob) * 100, 2) for prob in probabilities]

    st.subheader("🔍 Prediction Results")

    for _, row in results_df.iterrows():
        col1, col2 = st.columns([2, 1])
        with col1:
            if row["Prediction"] == "Benign":
                st.markdown(
                    f"<div style='background-color:#155724;padding:15px;border-radius:10px'>"
                    f"<h3 style='color:#FFFFFF;'>✅ Benign</h3>"
                    f"<p>With Percentage: <b>{row['Probability (%)']}%</b></p>"
                    "</div>", unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f"<div style='background-color:#FF2C2C;padding:15px;border-radius:10px'>"
                    f"<h3 style='color:#FFFFFF;'>⚠️ Malignant</h3>"
                    f"<p>With Percentage: <b>{row['Probability (%)']}%</b></p>"
                    "</div>", unsafe_allow_html=True
                )

    csv = results_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="💾 Download Predictions as CSV",
        data=csv,
        file_name="predictions.csv",
        mime="text/csv"
    )
else:
    st.info("Please upload a file or choose a sample dataset to proceed.")
