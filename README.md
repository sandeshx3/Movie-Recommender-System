🎬 Movie Recommender System
A sophisticated Content-Based Movie Recommender built using Machine Learning, Streamlit, and the TMDB API. This application suggests films by calculating mathematical similarities between movie metadata such as genres, cast, and keywords.

🌍 Live Link: https://movie-recommender-system-svly.onrender.com/

📌 Project Overview
This system is designed to help users discover new movies based on their existing favorites. By leveraging Natural Language Processing (NLP), we transform movie descriptions and metadata into high-dimensional vectors to find the closest matches in our database of 5,000+ films.

✨ Key Features
Intelligent Recommendations: Suggests the top 5 most similar movies based on content tags.

Dynamic Poster Rendering: Connects to the TMDB API to fetch and display high-resolution movie posters in real-time.

Seamless UI: A clean, data-driven dashboard built for high-performance desktop viewing.

Optimized Performance: Uses pre-computed similarity matrices for instant results.

💻 User Experience Note
Desktop/Laptop Optimization: This application is currently optimized for laptop and desktop screens. The layout uses a multi-column grid system to showcase movie posters effectively, which may not scale properly on smaller mobile devices. Mobile responsiveness is a planned future update.

🧠 How the Engine Works
The "magic" behind the recommendations follows a standard Machine Learning pipeline:

Data Cleaning: We merged the TMDB 5000 movies and credits datasets, extracting relevant features: genres, keywords, cast, and director.

Tagging: These features were merged into a single "tags" column and converted to lowercase for consistency.

Vectorization: Using CountVectorizer (Bag of Words), we converted the text tags into 5,000-dimensional vectors.

Similarity Measurement: We calculated the Cosine Similarity between every movie vector. This measures the cosine of the angle between two vectors, determining how "close" they are in a multi-dimensional space.

🛠️ Tech Stack & Dependencies
Frontend: Streamlit

Language: Python 3.13

Machine Learning: Scikit-Learn (CountVectorizer, Cosine Similarity)

Data Science: Pandas, NumPy

API: TMDB (The Movie Database)

Version Control: Git LFS (for managing the 185MB similarity.pkl file)

⚙️ Local Setup and Installation
Clone the Repository:

Bash

git clone https://github.com/sandeshx3/Movie-Recommender-System.git
cd Movie-Recommender-System
Install Git LFS (Crucial for large files):

Bash

git lfs install
git lfs pull
Install Required Libraries:

Bash

pip install -r requirements.txt
Run the Application:

Bash

streamlit run app.py
☁️ Deployment Details (Render)
The application is deployed on Render using the following configuration:

Build Command: pip install -r requirements.txt

Start Command: streamlit run app.py

Note: The system uses Git LFS pointers to ensure the large similarity matrix is successfully pulled into the Render environment during the build process.

