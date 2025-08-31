🎬 Movie Recommendation System

This project is a Movie Recommendation System that suggests movies to users based on similarity measures. It is built using Python, Machine Learning, and Streamlit for the frontend interface.

🚀 Features

✅ Content-Based Recommendation using cosine similarity

✅ Interactive Streamlit Web App for frontend

✅ Clean and simple user interface

✅ Easy to extend with new datasets

📂 Project Structure
MOVIE_RECOMMENDATION/
│── app.py                # Main Streamlit app  
│── model.py              # ML model for recommendation  
│── movies.pkl            # Preprocessed dataset  
│── similarity.pkl        # Similarity matrix for recommendations  
│── requirements.txt      # Required dependencies  
│── README.md             # Project documentation  

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/yashikasharma2004/MOVIE_RECOMMENDATION.git
cd MOVIE_RECOMMENDATION

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the app
streamlit run app.py

🛠️ Tech Stack

Python

Pandas, NumPy, Scikit-learn (ML & preprocessing)

Streamlit (frontend UI)

🎯 How It Works

The dataset is preprocessed and stored in movies.pkl.

A cosine similarity matrix (similarity.pkl) is used to compute movie similarities.

The user selects a movie from the dropdown.

The system recommends top 5 similar movies.


🌟 Future Improvements

Add hybrid recommendation (content + collaborative filtering)

Deploy on Streamlit Cloud / Heroku

Improve UI with images/posters of movies
