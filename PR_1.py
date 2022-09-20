from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("proyect.html")

@app.route("/hello", methods=["POST"])
def hello():
   name: object = request.form.get("name")
   #nacimiento: object = request.form.get("macimiento")
   return render_template("CV.html", nombre=name)
