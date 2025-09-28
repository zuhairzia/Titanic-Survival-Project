import streamlit as st
import joblib
import numpy as np

# Load saved model
model = joblib.load("Titanic_Survival_Joblib/titanic_model.joblib")

# =======================
# 🎨 Custom CSS
# =======================
st.markdown(
    """
    <style>
    /* Background White */
    .stApp {
        background: #ffffff;  /* Pure White Background */
        color: #000000;       /* Black Text */
    }

    /* Title */
    h1 {
        color: #2C3E50;
        text-align: center;
        font-family: 'Trebuchet MS', sans-serif;
        font-size: 42px !important;
        margin-bottom: 20px;
    }

    /* Subheader */
    h3 {
        color: #2980B9;
        text-align: center;
    }

    /* Prediction Box */
    .prediction-box {
        padding: 20px;
        border-radius: 12px;
        background-color: #F8F9F9;
        text-align: center;
        font-size: 24px;
        margin-top: 20px;
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(135deg, #2C3E50, #4CA1AF); /* Dark Blue to Teal */
        color: black;
    }
    [data-testid="stSidebar"] * {
        color: black !important;  /* Force black text */
    }

    
    /* Sidebar Header specific (⚙️ Passenger Details) */
    [data-testid="stSidebar"] h2 {
        color: white !important;
        font-weight: bold;
    }


    /* Predict Button Styling */
    div.stButton > button {
        background: linear-gradient(135deg, #FF512F, #DD2476); 
        color: black;
        border-radius: 10px;
        border: none;
        font-size: 18px;
        font-weight: bold;
        padding: 10px 20px;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background: linear-gradient(135deg, #DD2476, #FF512F);
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =======================
# 🚢 App Title
# =======================
st.title("🚢 Titanic Survival Prediction")
st.markdown("<h3>Will You Survive the Titanic? 🌊</h3>", unsafe_allow_html=True)

# =======================
# 🛠 Sidebar Inputs
# =======================
st.sidebar.header("⚙️ Passenger Details")

pclass = st.sidebar.selectbox("Passenger Class", [1, 2, 3], format_func=lambda x: f"{x} Class")
sex = st.sidebar.selectbox("Sex", ["male", "female"])
age = st.sidebar.slider("Age", 0, 80, 25)
sibsp = st.sidebar.number_input("Siblings/Spouses Aboard", min_value=0, max_value=10, value=0)
parch = st.sidebar.number_input("Parents/Children Aboard", min_value=0, max_value=10, value=0)
fare = st.sidebar.number_input("Fare Paid ($)", min_value=0.0, max_value=600.0, value=32.0)
embarked = st.sidebar.selectbox("Port of Embarkation", ["C", "Q", "S"])

# Encode categorical features
sex = 1 if sex == "female" else 0
embarked = {"C": 0, "Q": 1, "S": 2}[embarked]

# Prepare input
features = np.array([[pclass, sex, age, sibsp, parch, fare, embarked]])

# =======================
# 🎯 Prediction
# =======================
if st.button("🔮 Predict Survival"):
    prediction = model.predict(features)
    proba = model.predict_proba(features)[0][1]  # survival probability

    result = "🎉 Survived" if prediction[0] == 1 else "💀 Did Not Survive"
    color = "lime" if prediction[0] == 1 else "red"

    st.markdown(
        f"""
        <div class="prediction-box" style="border: 2px solid {color}; color: {color};">
            <b>Prediction:</b> {result}<br>
            <span style="font-size:20px;">Survival Probability: <b>{proba*100:.2f}%</b></span>
        </div>
        """,
        unsafe_allow_html=True
    )
