# 📝 Sentiment Analysis on Twitter Data

## 📌 Overview

This project focuses on **classifying tweets** into three sentiment categories:

* **Positive (1)**
* **Neutral (0)**
* **Negative (-1)**

It demonstrates text preprocessing (tokenization, lemmatization, stopword removal), feature engineering, and machine learning for sentiment classification.

---

## ⚙️ Steps

1. **Data Preparation**

   * Dataset: Tweets labeled with sentiment (`-1, 0, 1`)
   * Loaded into a Pandas DataFrame

2. **Preprocessing**

   * Tokenization (splitting text into words)
   * Stopword removal (removing words like *the, and, is*)
   * Lemmatization (reducing words to their base form)
   * Re-joining tokens into a clean text column

3. **Feature Engineering**

   * Used `TF-IDF Vectorization` to convert text into numerical features

4. **Model Training**

   * Trained a **Logistic Regression Classifier** (baseline model)
   * Evaluated using accuracy and confusion matrix

---

## 📊 Results

* Successfully classified tweets into positive, neutral, and negative.
* Accuracy: *(fill in after training)*
* Example:

  ```
  Tweet: "talk all the nonsense and continue all the drama"
  Predicted Sentiment: Neutral (0)
  ```

---

## 🛠️ Libraries Used

* **pandas** → data handling
* **nltk** → tokenization, stopwords, lemmatization
* **scikit-learn** → TF-IDF, model training, evaluation

---

## 🚀 Run the Project

1. Install requirements:

   ```bash
   pip install pandas scikit-learn nltk
   ```

2. Run Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

3. Open `sentiment_analysis.ipynb` and execute cells.

---

## 📌 Author

Ahmed Mohammed

---
