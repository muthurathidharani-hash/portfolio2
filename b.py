from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv
from flask import send_from_directory
# Load environment variables
load_dotenv()

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.getenv('DEL_EMAIL')
app.config['MAIL_PASSWORD'] = os.getenv('PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)
LOGIN_PASSWORD = "muthu404"
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        password = request.form["password"]
        if password == LOGIN_PASSWORD:
            return redirect(url_for("homepage"))
        else:
            return "Invalid Password!"
    return render_template("index.html")

@app.route("/homepage")
def homepage():
    return render_template("homepage.html")

@app.route("/about")
def about():
    return render_template("aboutme.html")

@app.route("/skills")
def skills():
    return render_template("skills.html")

@app.route("/projects")
def projects():
    return render_template("project.html")

@app.route("/contact")
def contact():
    return render_template("contactme.html")

@app.route("/resume")
def resume():
    return send_from_directory(".", "resume.pdf")

@app.route("/submit", methods=["POST"])
def submit():
    if request.method == "POST":
        name = request.form["name"]
        subject = request.form["subject"]
        message = request.form["message"]

        msg = Message(
            subject,
            sender=os.getenv('DEL_EMAIL'),
            recipients=[os.getenv('REC_EMAIL')]
        )
        msg.body = f"Hello from {name},\n\n{message}"
        mail.send(msg)

        return redirect(url_for("contact"))

# ------------------- MAIN -------------------
if __name__ == "__main__":
    app.run(debug=True, port=5000)
