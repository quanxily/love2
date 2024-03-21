from flask import Flask, render_template,request
from datetime import datetime
app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>我和翔順寶寶的紀念網站</title>
</head>
<body style="background-color: lightblue;">
    <h1>我和翔順寶寶的紀念網站</h1>
</body>
</html>
"""


@app.route("/")
def index():
    x = html
    x +="<a href=/love>一周年紀念日</a><br>"
    x +="<a href=/our>彼此的基本資料</a><br>"
    x +="<a href=/story>相識到相戀故事</a><br>"
    x +="<a href=/photo>照片牆</a><br>"
    return x
@app.route("/love")
def love():
    return render_template("love.html")

@app.route("/our")
def our():
    return render_template("our.html")

@app.route("/story")
def story():
    return render_template("story.html")

@app.route("/photo")
def photo():
    return render_template("photo.html")

if __name__ == "__main__":
  app.run()