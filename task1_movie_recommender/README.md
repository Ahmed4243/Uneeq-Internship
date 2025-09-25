# 🎬 Movie Recommender System

This is **Task 1** of my Uneeq Internship.
It’s a **content-based movie recommender system** built with Python, scikit-learn, and Streamlit.
The app suggests movies similar to the one selected by the user.

---

## 📂 Project Structure

```
Task1-Movie-Recommender/
│── app.py                # Streamlit app
│── build_data.ipynb      # Preprocessing notebook
│── movies.pkl            # Processed movie data
│── similarity.pkl        # Cosine similarity matrix
│── README.md             # Project documentation
```

---

## 📊 Dataset

This project uses the **TMDB 5000 Movie Dataset**.
You need two CSV files:

* `tmdb_5000_movies.csv`
* `tmdb_5000_credits.csv`

👉 Download here: [TMDB Movie Dataset (Kaggle)](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

---

## ⚙️ Installation & Usage

1. Clone the repo:

   ```bash
   git clone https://github.com/Ahmed4243/Uneeq-Internship.git
   cd Uneeq-Internship/task1_movie_recommender
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   Example `requirements.txt`:

   ```
   streamlit
   scikit-learn
   pandas
   numpy
   ```

3. Run the preprocessing notebook (`build_data.ipynb`) to generate `movies.pkl` and `similarity.pkl`.
   (These files are already included in the repo, so this step is optional.)

4. Launch the app:

   ```bash
   streamlit run app.py
   ```

---

## 🚀 Features

* Select a movie from a dropdown list.
* Get top 5 similar movies based on cosine similarity of genres, keywords, cast, and crew.
* Simple and interactive Streamlit UI.

---

## 📌 Notes

* The dataset is **not included** in this repo due to size limits. Download it separately from Kaggle.
---
