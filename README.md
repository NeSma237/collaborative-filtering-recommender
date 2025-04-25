# collaborative-filtering-recommender

# 🎬 Movie Recommendation System (Collaborative Filtering)

This project implements a **Collaborative Filtering-based Recommendation System** using the [MovieLens 100K dataset](https://www.kaggle.com/datasets/prajitdatta/movielens-100k-dataset). The system suggests movies to users based on their past ratings and the preferences of similar users or items.

---

## 📌 Project Objectives

- Load and preprocess the MovieLens dataset
- Implement:
  - User-Based Collaborative Filtering
  - Item-Based Collaborative Filtering
- Evaluate with:
  - RMSE
  - Precision & Recall at K
- Generate Top-N movie recommendations
- (Optional) Visualize user similarities and model performance

---

## 📁 Dataset

- **Name**: MovieLens 100K
- **Source**: [Kaggle](https://www.kaggle.com/datasets/prajitdatta/movielens-100k-dataset)
- **Content**: 100,000 ratings from 943 users on 1,682 movies

---

## 🛠️ Tech Stack

- **Language**: Python 3.x
- **Libraries**:
  - `pandas`, `numpy`
  - `scikit-learn`
  - `surprise` (for collaborative filtering)
  - `matplotlib`, `seaborn` (for optional visualizations)
- **Environment**: Jupyter Notebook or Python script

---

## 🚀 How to Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/movie-recommender-cf.git
   cd movie-recommender-cf

   Install Dependencies


pip install -r requirements.txt
Download the Dataset

Place u.data in the root directory or update the path in the script accordingly.

Run the Notebook or Script

jupyter notebook recommender_system.ipynb
# OR
python recommender_system.py
📊 Evaluation Metrics
RMSE (Root Mean Square Error): Measures prediction accuracy

Precision@K / Recall@K: Measures recommendation relevance

🧠 Collaborative Filtering Methods
User-Based: Recommends items by finding users with similar tastes

Item-Based: Recommends similar items to those the user has rated highly

📌 Sample Output

Top-5 recommendations for User 196:
Movie ID: 50, Predicted Rating: 4.63
Movie ID: 172, Predicted Rating: 4.57
Movie ID: 181, Predicted Rating: 4.51
...
📈 Optional: Visualizations
Heatmaps of user-user or item-item similarities

Performance metric plots (e.g., RMSE over different K values)

📃 License
This project is licensed under the MIT License.

🙌 Acknowledgements
GroupLens Research for the dataset

surprise library authors for simplifying recommender system development
