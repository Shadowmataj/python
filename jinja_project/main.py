from flask import Flask, render_template
from post import Post

app = Flask(__name__)

post = Post()

@app.route('/')
def home():
    print(post.response_blogs)
    return render_template("index.html", blogs= post.response_blogs)

@app.route("/blog/<int:num>")
def blog(num):
    print(post.response_blogs[num])
    return render_template("post.html", num=num, blogs=post.response_blogs)

if __name__ == "__main__":
    app.run(debug=True)
