from flask import Flask, render_template
from data_manager import DataManager

data_manager = DataManager()

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html", header_title="home", posts= data_manager.posts)

@app.route("/about")
def about():
    return render_template("about.html", header_title="about")

@app.route("/contact")
def contact():
    return render_template("contact.html", header_title="contact")

@app.route("/post/<int:num>")
def post(num):
    return render_template("post.html", header_title="post", post= data_manager.posts[num-1])

if __name__ == "__main__":
    app.run(debug=True)