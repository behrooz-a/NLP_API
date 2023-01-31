#!/usr/bin/env python

from flask import Flask, render_template, request
import numpy as np
from transformers import pipeline
classifier = pipeline("sentiment-analysis")


app = Flask(__name__)

@app.route("/")
def web():
    return render_template("web.html")

@app.route(
    "/Prediction", methods=["POST"])  # this line will be activated when Submit button has been
def Prediction():

    height_strings = request.form.get("height")
    res=classifier(height_strings)


    return render_template(
        "web.html", result="Based on the sentiment analysis your sentence is {} with the socre of {: .1f} out of 1.".format(res[0].get('label'), res[0].get('score'))
    )


if __name__ == "__main__":
    app.run(debug=True)
