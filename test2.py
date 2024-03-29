from flask import Flask, render_template,request
from datetime import datetime
app = Flask(__name__)

html = """
<!DOCTYPE html>
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>我和翔順寶寶的紀念網站</title>
    <style type="text/css">
        header, footer {
            text-align: center;
            padding: 10pX;
            margin: 10pX;
        }
        header {
            background-image: url("/static/ve.jpg");

        }
        footer {
            background-color: #c5e0ed;

        }


        article {
            padding: 10pX;
            margin: 10pX;
        }
        h2 {
            border-color: white;
            border-style: solid ;
            border-radius: 12px;
            border-width: 5px;
            background-color: skyblue;
        }


        p {
            font-size: 20px;
        }

        h4 {
            border-color: white;
            border-style: solid ;
            border-radius: 12px;
            border-width: 5px;
            background-color: #e99dfa ;
            font-size: 25px;
        }

        h3 {
            border-color: white;
            border-style: solid ;
            border-radius: 12px;
            border-width: 5px;
            background-color: #f5d5d5;
            font-size: 25px;
        }
        h1 {
            text-decoration: underline solid white 30%;
            text-shadow: 2px 2px #e4f3fe;
        }

        .row {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            align-items: stretch;
        }

        .colum {
            padding: 10px;
        }

        .colum.side {
            flex: 1;
            background-image: url("/static/le.jpg");
            padding: 20px;
            margin-bottom: 10px;
            overflow: hidden;
        }

        .colum.middle {
            flex: 1;
            background-image: url("/static/le.jpg");
            padding: 20px;
            margin-bottom: 10px;
            overflow: hidden;
        }

        @media(max-width: 600px) {
            .row {
                flex-direction: column;
                -webkit-flex-direction: column;
            }

    </style>
</head>


<body>
<header>
    <h1>我和翔順寶寶的紀念網站</h1>
</header>

<main>
    <article>
        <section class="row">
            <div class ="colum side">
                <h4>彼此基本資料</h4>
                 <p><a href ="/our">基本資料</a></p>
                <img src = "static/67.jpg" width ="200">
                <img src = "static/68.jpg" width ="200">  
            </div>
                
            <div class ="colum middle">
                <h4>相識到相戀的故事</h4>
                <p><a href ="/story">相識到相戀故事</a></p> 
                <img src = "static/lv.jpg" width ="200"> 
            </div>

            <div class="colum side">
                <h4>照片牆</h4>
                <p><a href ="/photo">照片牆</a></p> 
            </div>
        </section>
    </article>
</main>

<footer>
            Copyright ©  楊荃喜. All Rights Reserved.
</footer>
</body>
</html>
"""


@app.route("/")
def index():
    x = html
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