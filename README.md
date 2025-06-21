# 🎬 Movie Recommendation System

> 🔍 An intelligent movie recommendation web app built with Django, Pandas, Scikit-learn, and Bootstrap – offering personalized film suggestions based on what you like.

<p align="center">
  <img src="https://media.giphy.com/media/26BRrSvJUa0crqw4E/giphy.gif" width="400" alt="Movie Recommender">
</p>

---

## 🚀 Features

✨ **User-Friendly Web Interface**  
🎯 **Item-Based Collaborative Filtering** using cosine similarity  
🧠 **Real-time Recommendations** based on movie selection  
📊 Scalable system ready for hybrid or user-based extensions  
🌐 Arabic RTL Interface (designed for real-world users)  
🎨 Clean, responsive UI with Bootstrap 5

---

## 🛠️ Technologies Used

| Tool / Tech        | Role                                 |
|--------------------|--------------------------------------|
| 🐍 Python          | Backend & Logic                      |
| 🧠 Scikit-learn    | Similarity Computation               |
| 🐼 Pandas          | Data Cleaning & Preprocessing        |
| 🌐 Django          | Web Framework                        |
| 🎨 Bootstrap 5     | UI Styling                           |
| 📁 MovieLens 100K  | Dataset Source                       |

---

## 📷 Screenshots

### 🎬 Home Page
<img src="https://i.imgur.com/Jfsf9bH.png" width="700">

### 🔍 Recommendations
<img src="https://i.imgur.com/8JyrBJN.png" width="700">

---

## ⚙️ How to Run Locally

```bash
git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Import movies from similarity matrix
python manage.py import_movies

# Run the development server
python manage.py runserver
