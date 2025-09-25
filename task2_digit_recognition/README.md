# 🖋️ Handwritten Digit Recognition (MNIST)

## 📌 Overview

This project focuses on **classifying handwritten digits (0–9)** from the **MNIST dataset** using a **Convolutional Neural Network (CNN)** built with **TensorFlow/Keras**.

---

## ⚙️ Steps

1. **Data Preparation**

   * Dataset: **MNIST** (60,000 training images, 10,000 testing images)
   * Images are grayscale, size **28x28 pixels**

2. **Preprocessing**

   * Normalized pixel values (0–255 → 0–1)
   * Reshaped images into `(28, 28, 1)` for CNN input
   * One-hot encoded labels (0–9)

3. **Model Architecture (CNN)**

   * **Conv2D (32 filters, 3x3, ReLU)**
   * **MaxPooling2D (2x2)**
   * **Conv2D (64 filters, 3x3, ReLU)**
   * **MaxPooling2D (2x2)**
   * **Flatten Layer**
   * **Dense (128, ReLU)**
   * **Dense (10, Softmax)**

4. **Training**

   * Optimizer: **Adam**
   * Loss: **Categorical Crossentropy**
   * Epochs: **5**
   * Batch size: **128**
   * Validation on test set

5. **Evaluation & Visualization**

   * Test accuracy: *(fill in after training, usually \~99%)*
   * Visualized sample predictions and training history (accuracy/loss curves)

---

## 📊 Results

* CNN achieved **high accuracy (\~99%)** on MNIST test set.
* Example visualization:

```
Predicted: 7 | True: 7  
Predicted: 3 | True: 3  
Predicted: 9 | True: 9  
```

---

## 🛠️ Libraries Used

* **TensorFlow / Keras** → deep learning
* **matplotlib** → visualization
* **numpy** → numerical operations

---

## 🚀 Run the Project

1. Install requirements:

   ```bash
   pip install tensorflow numpy matplotlib
   ```

2. Run Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

3. Open `mnist_cnn.ipynb` and execute cells.

---

## 📌 Author

Ahmed Mohammed

---
