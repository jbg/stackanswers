#!/usr/bin/env python

from flask import Flask, request, render_template
from stackoverflow import StackOverflowImporter


def query(q):
  if q is None:
    return None
  q = q.replace(" ", "_")  # TODO better preprocessing
  return StackOverflowImporter._fetch_code(StackOverflowImporter._fetch_url(q))


app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def home():
  q = request.args.get("q")
  return render_template("home.html", result=query(q), q=q)

if __name__ == "__main__":
  # Heroku passes PORT as an env var; otherwise use 5000
  import os
  app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")))
