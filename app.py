from flask import Flask, render_template, request
import pandas as pd
from scraper import scrape_laptops

app = Flask(__name__)

def load_data():
    return pd.read_excel("products.xlsx").to_dict(orient="records")

@app.route("/", methods=["GET", "POST"])
def index():
    products = load_data()
    search = ""
    if request.method == "POST":
        search = request.form.get("search", "").lower()
        products = [p for p in products if search in p["Title"].lower()]
    return render_template("index.html", products=products, search=search)

if __name__ == "__main__":
    scrape_laptops()
    app.run(debug=True)
