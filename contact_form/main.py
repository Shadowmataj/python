from flask import Flask, render_template, request
import requests
from smtplib import SMTP
import os

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)

def send_email(form_info):
    email=os.environ.get("GMAIL")
    password=os.environ.get("GOOGLE_KEY")
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr= email,
            to_addrs=email,
            msg=f"Subject: New form answer!!\n\nName: {form_info["name"]}\n"
                 f"Email: {form_info["email"]}\n"
                 f"Phone number: {form_info["phone"]}\n"
                 f"Message: {form_info["message"]}"
        )


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.get("/contact")
def contact():
    message = "Contact Me"
    return render_template("contact.html", message=message)

@app.post("/contact")
def form_entry():
    message="Successfully sent message"
    send_email(form_info=request.form)
    return render_template("contact.html", message=message)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)



if __name__ == "__main__":
    app.run(debug=True, port=5001)
