🏨 Hotel Booking Cancellation Prediction
An end-to-end machine learning project that predicts hotel booking cancellations using Random Forest Classifier, served via Flask, Streamlit, and integrated with Google Gemini API for AI-powered insights.
Achieved 99% accuracy with proper preprocessing, feature engineering, and explainable AI support.

🚀 Features
Data Preprocessing: Missing value handling, encoding, scaling.
EDA: Exploratory Data Analysis with visualizations.
Model: Random Forest Classifier for high accuracy.
Deployment: Flask API + Streamlit UI for easy interaction.
AI Integration: Google Gemini API for explainable predictions.

⚙️ Tech Stack
Python
Flask
Streamlit
Scikit-learn (Random Forest Classifier)
Pandas, NumPy, Matplotlib, Seaborn
Google Gemini API

1. Clone the repository
git clone https://github.com/your-username/hotel-booking-cancellation.git
cd hotel-booking-cancellation

2. Install dependencies
pip install -r requirements.txt

3. Add your dataset
Replace data/your_dataset.csv with your own hotel booking dataset.

4. Configure Google Gemini API
Get your Gemini API Key from Google AI Studio
Add it inside your code:
GEMINI_API_KEY = "your_api_key_here"

5. Run Flask backend
python app.py

6. Run Streamlit app
streamlit run streamlit_app.py
