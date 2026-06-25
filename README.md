# 🌱 KrishiMitra - AI Powered Crop Recommendation System

## Overview

KrishiMitra is an end-to-end Machine Learning project that recommends the most suitable crops based on soil nutrients and environmental conditions. The project combines a trained Random Forest model with a Flask web application to provide an interactive platform for intelligent crop recommendation.

Unlike traditional recommendation systems that only predict a single crop, KrishiMitra ranks all possible crops based on their predicted suitability and allows users to personalize recommendations using custom priority weights.

---

## Features

* 🌾 Crop recommendation using Machine Learning
* 📊 Probability-based ranking of all crop classes
* ⚖️ Customizable recommendation priorities through Alpha, Beta and Gamma weights
* 📈 Crop suitability scoring system
* 🌍 Interactive web interface built using Flask
* 📥 Dataset download page
* 📖 About project and dataset documentation
* ☁️ Deployed on Render

---

## Machine Learning Pipeline

```
Crop Recommendation Dataset
            │
            ▼
Data Preprocessing
            │
            ▼
Feature Engineering
            │
            ▼
Random Forest Classifier
            │
            ▼
Probability Prediction
            │
            ▼
Crop Suitability Score
            │
            ▼
Ranked Crop Recommendations
            │
            ▼
Flask Web Application
```

---

## Input Features

The model predicts crop suitability using the following parameters:

* Nitrogen (N)
* Phosphorous (P)
* Potassium (K)
* Temperature
* Humidity
* pH Value
* Rainfall

---

## Crop Recommendation Logic

The Random Forest model predicts the probability of every crop class.

Instead of recommending only the highest probability crop, KrishiMitra computes a custom Crop Suitability Score by combining:

* Model prediction probability
* Expected crop profitability
* Expected yield per hectare

Users can adjust the importance of these three factors using Alpha, Beta and Gamma weights to obtain recommendations that align with their farming priorities.

---

## Technology Stack

### Machine Learning

* Python
* Scikit-learn
* NumPy
* Pandas
* Random Forest Classifier

### Backend

* Flask

### Frontend

* HTML
* CSS
* JavaScript

### Deployment

* Render

### Version Control

* Git
* GitHub

---

## Project Structure

```
KrishiMitra/

│── app.py
│── crop_model.pkl
│── label_encoder.pkl
│── requirements.txt

├── static/
│   ├── style.css
│   ├── script.js
│   ├── images/
│   └── datasets/

├── templates/
│   ├── welcome.html
│   ├── main.html
│   ├── crop.html
│   ├── about.html
│   ├── data.html
│   ├── weather.html
│   ├── fertilizer.html
│   ├── disease.html
│   └── chat.html
```

---

## Local Installation

Clone the repository

```bash
git clone https://github.com/Harshit-15-10/KrishiMitra.git
```

Navigate into the project

```bash
cd KrishiMitra
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## Live Demo

🌐 **Website**

https://krishimitra-89h8.onrender.com

---

## Dataset

The project uses the Crop Recommendation Dataset containing approximately:

* 2200 samples
* 22 crop classes
* 7 environmental and soil features

---

## Future Improvements

* Weather API integration
* AI Agricultural Chatbot
* Fertilizer Recommendation System
* Disease Detection using Deep Learning
* Farmer Login System
* Real-time Weather Forecasting
* Soil Sensor Integration

---

## Learning Outcomes

This project helped strengthen my understanding of:

* Machine Learning model development
* Data preprocessing
* Feature engineering
* Model serialization using Pickle
* Flask backend development
* REST API integration
* Full ML model deployment
* Git and GitHub workflow
* Cloud deployment using Render

---

## Author

**Harshit Srivastava**

Machine Learning Enthusiast | AI Engineer Aspirant | Software Developer

GitHub: https://github.com/Harshit-15-10
live demo: https://krishimitra-89h8.onrender.com
