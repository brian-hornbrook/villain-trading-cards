from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask("app")

app.config["SQLALCHEMY_DATABASE_URL"] = "sqlite:///villain.db"

db = SQLAlchemy(app)

@app.route("/")
def villains_cards():
  return render_template("villain.html")

app.run(host='0.0.0.0', port=8080)
