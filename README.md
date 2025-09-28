Titanic Survival Project
![1601702195306](https://github.com/user-attachments/assets/428b9e6f-bed5-48c8-9e0a-bad9a1d092ac)

🚢 Titanic Survival Prediction
📌 Project Overview
This project aims to predict whether a passenger survived the Titanic disaster or not, based on features like age, gender, ticket class, and fare.

The workflow includes:


Data Cleaning & Preprocessing
Feature Engineering
Model Training
Model Evaluation
Saving the Model
📌 Step 1: Import Required Libraries
We will import all the necessary Python libraries for:

Data manipulation (Pandas, NumPy)
Visualization (Matplotlib, Seaborn)
Machine learning (Scikit-learn)
Model saving (Joblib)
📂 Step 2: Load Dataset
Now, we will load the Titanic dataset (train.csv) and look at the first few rows to understand the structure.

📊 Step 3: Explore the Dataset
Let's check:

Dataset information
Missing values
Statistical summary
🧹 Step 4: Data Cleaning
We need to handle:

Missing values in Age, Cabin, and Embarked
Drop irrelevant columns (Name, Ticket, Cabin) since they don’t add much value
🔄 Step 5: Encode Categorical Variables
We will convert categorical features into numeric format:

Sex → 0 = female, 1 = male
Embarked → Encoded into 0, 1, 2
🎯 Step 6: Define Features (X) and Target (y)
We will separate the dataset into:

X (features) → independent variables
y (target) → Survived column
✂️ Step 7: Train-Test Split
We will split the dataset into:

Training set (80%) → used for training the model
Testing set (20%) → used for evaluating the model
⚖️ Step 8: Feature Scaling
We will standardize our features so that all values lie on the same scale. This helps the model train more effectively.

🤖 Step 9: Train Model (Logistic Regression)
We will use Logistic Regression as our first ML model to predict survival.

📊 Step 10: Evaluate Model
We will check:

Accuracy Score
Confusion Matrix
Classification Report
🚀 Step 11: Try Multiple ML Models & Compare
To make our Titanic survival prediction model more professional, we will try multiple Machine Learning algorithms and compare their performance:

Decision Tree
Random Forest
Support Vector Machine (SVM)
K-Nearest Neighbors (KNN)
We will evaluate each model using Accuracy Score and then compare results to select the best model.

📊 Step 12: Model Performance Visualization
To make the comparison more clear and professional, we will visualize the accuracy scores of all models using a bar chart.

🛠 Step 11: Save Best Model with Joblib
Now that we have trained and compared multiple ML models, we will save the best performing model (Random Forest) using joblib.
This allows us to reuse the trained model later without retraining, which is especially useful when deploying the model in a Streamlit app.

We will save the model inside a dedicated folder: Titanic_Survival_Joblib.

🚀 Step 12: Build Streamlit App for Deployment
We will now create a Streamlit app (app.py) that:

Loads our saved Random Forest model (titanic_model.joblib).
Takes passenger details as user input.
Predicts whether the passenger survived or not.
