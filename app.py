from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask import send_file

import numpy as np
import pickle

# CREATE APP

app = Flask(__name__)

# LOAD MODEL

model = pickle.load(
    open("crop_model.pkl", "rb")
)

# LOAD LABEL ENCODER

label_encoder = pickle.load(
    open("label_encoder.pkl", "rb")
)

# PROFIT DATA (TEMPORARY)

profit_data = {

    "rice": 20,
    "maize": 18,
    "jute": 25,
    "cotton": 30,
    "coconut": 40,
    "papaya": 35,
    "orange": 50,
    "apple": 120,
    "muskmelon": 45,
    "watermelon": 28,
    "grapes": 80,
    "mango": 60,
    "banana": 32,
    "pomegranate": 90,
    "lentil": 55,
    "blackgram": 48,
    "mungbean": 52,
    "mothbeans": 35,
    "pigeonpeas": 40,
    "kidneybeans": 65,
    "chickpea": 45,
    "coffee": 150
}

# YIELD DATA (KG/HECTARE)

yield_data = {

    "rice": 4000,
    "maize": 3500,
    "jute": 2500,
    "cotton": 2000,
    "coconut": 15000,
    "papaya": 18000,
    "orange": 12000,
    "apple": 8000,
    "muskmelon": 10000,
    "watermelon": 15000,
    "grapes": 9000,
    "mango": 11000,
    "banana": 30000,
    "pomegranate": 7000,
    "lentil": 1500,
    "blackgram": 1200,
    "mungbean": 1400,
    "mothbeans": 1000,
    "pigeonpeas": 1800,
    "kidneybeans": 2200,
    "chickpea": 2000,
    "coffee": 2500
}

# MAX VALUES FOR NORMALIZATION

max_profit = max(
    profit_data.values()
)

max_yield = max(
    yield_data.values()
)

# HOME PAGE

@app.route("/")

def home():

    return render_template(
        "welcome.html"
    )


# MAIN PAGE

@app.route("/main")

def main():

    return render_template(
        "main.html"
    )

# CROP PAGE

@app.route("/crop")

def crop():

    return render_template(
        "crop.html"
    )

# WEATHER PAGE

@app.route("/weather")

def weather():

    return render_template(
        "weather.html"
    )

# CHAT PAGE

@app.route("/chat")

def chat():

    return render_template(
        "chat.html"
    )

# FERTILIZER PAGE

@app.route("/fertilizer")

def fertilizer():

    return render_template(
        "fertilizer.html"
    )

# DISEASE PAGE

@app.route("/disease")

def disease():

    return render_template(
        "disease.html"
    )

# ABOUT PAGE
@app.route("/about")

def about():

    return render_template(
        "about.html"
    )

# DATASET PAGE
@app.route("/data")

def data():

    return render_template(
        "data.html"
    )

# DATASET DOWNLOAD
@app.route("/download-dataset")

def download_dataset():

    return send_file(
        "static/datasets/Crop_recommendation.csv",
        as_attachment=True
    )
# PREDICTION ROUTE

@app.route("/predict", methods=["POST"])

def predict():

    try:

        # RECEIVE DATA

        data = request.json

        print("\nReceived Data:")
        print(data)

        # EXTRACT FEATURES

        N = float(data["N"])

        P = float(data["P"])

        K = float(data["K"])

        temperature = float(
            data["temperature"]
        )

        humidity = float(
            data["humidity"]
        )

        ph = float(
            data["ph"]
        )

        rainfall = float(
            data["rainfall"]
        )

        # USER PREFERENCES

        alpha = float(
            data["alpha"]
        )

        beta = float(
            data["beta"]
        )

        gamma = float(
            data["gamma"]
        )

        # NORMALIZE WEIGHTS

        total_weight = (
            alpha + beta + gamma
        )

        if total_weight == 0:
            alpha = 1/3
            beta = 1/3
            gamma = 1/3
        else:
            alpha /= total_weight
            beta /= total_weight
            gamma /= total_weight

        # CREATE FEATURE ARRAY

        features = np.array([[
            N,
            P,
            K,
            temperature,
            humidity,
            ph,
            rainfall
        ]])

        # GET PROBABILITIES

        probabilities = model.predict_proba(
            features
        )[0]

        # GET CROP NAMES

        crop_names = (
            label_encoder.classes_
        )

        # CALCULATE SCORES

        crop_scores = []

        for i in range(
            len(crop_names)
        ):

            crop = crop_names[i]

            probability = (
                probabilities[i]
            )

            normalized_profit = (
                profit_data[crop]
                / max_profit
            )

            normalized_yield = (
                yield_data[crop]
                / max_yield
            )

            final_score = (

                alpha * probability +

                beta * normalized_profit +

                gamma * normalized_yield
            )

            crop_scores.append({

                "crop": crop,

                "probability":
                round(
                    float(probability)*100,
                    4
                ),

                "score":
                round(
                    float(final_score),
                    4
                )
            })

        # SORT CROPS

        crop_scores.sort(

            key=lambda x: x["score"],

            reverse=True
        )

        # SEND RESPONSE

        return jsonify({

            "recommendations":
            crop_scores

        })

    except Exception as e:

        print("\nERROR:")
        print(str(e))

        return jsonify({

            "error": str(e)

        }), 500

# RUN SERVER

if __name__ == "__main__":

    app.run(debug=True)