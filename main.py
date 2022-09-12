from flask import Flask, render_template
import requests
import random


app = Flask(__name__)


@app.route("/")
def index():
    response = requests.get("https://api.npoint.io/2154c8c275d701a9daa7").json()
    return render_template("index.html", posts=response)


@app.route("/contact")
def contact_page():
    return render_template("contact.html")


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/post/<int:post_id>")
def post_page(post_id):
    response = requests.get("https://api.npoint.io/2154c8c275d701a9daa7").json()
    post = None
    for blog_post in response:
        if blog_post["id"] == post_id:
            post = blog_post
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)

