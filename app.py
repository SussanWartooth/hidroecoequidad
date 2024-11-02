from flask import Flask, render_template
from graph_generator import generate_bar_graph

app = Flask(__name__)

@app.route("/")
def home():
    generate_bar_graph()
    return render_template("home.html")

