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
            animation: example1;
            animation-duration: 4s;
            animation-iteration-count: 1;
        }

        @keyframes example1 {
            from {
                transform: rotate(-15deg) translateY(-100%);
                opacity: 0;
            }
            to {
                transform: rotate(0deg) translateY(0%);
                opacity: 1;
            }
        }
        
        footer {
           background-image: url("/static/ve.jpg");
        }

        p {
            font-size: 20px;
        }

        h4 {
            border-color: white;
            border-style: solid ;
            border-radius: 12px;
            border-width: 5px;
            background-color: #e4f3fe;
            font-size: 25px;
        }

        h1 {
            text-decoration: underline solid white 30%;
            text-shadow: 2px 2px #e4f3fe;
        }

        .row {
            display: flex;
            flex-wrap: wrap;
            align-items: stretch;
        }

        .colum {
            padding: 12px;
        }

        .colum.side {
            flex: 1;
            background-image: url("/static/le.jpg");
            padding: 10px;
            margin-bottom: 10px;
            overflow: hidden;
        }

        .colum.middle {
            flex: 1;
            background-image: url("/static/le.jpg");
            padding: 10px;
            margin-bottom: 10px;
            overflow: hidden;
        }

        @media(max-width: 600px) {
            .row {
                flex-direction: column;
                -webkit-flex-direction: column;
            }


        @media(max-width: 580px) {
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
                <div class="image-container" id="example1">
                <img src = "static/67.jpg" width ="350" height = "450"> 
                </div>
                <button onclick="prevImage()">❮</button>
                <button onclick="nextImage()">❯</button>
                <button onclick="toggleCarousel()">暫停</button>
                <script>
                  // JavaScript 函式
                     var intervalId;
                        // 範例 1: 圖片切換
                           function changeImage(containerId, imageName) {
                            var container = document.getElementById(containerId);
                            var image = container.querySelector("img");
                            image.src = imageName;
                        }

                        var images = ["static/67.jpg", "static/68.jpg"];
                        var currentIndex = 0;

                        function prevImage() {
                            currentIndex = (currentIndex - 1 + images.length) % images.length;
                            changeImage('example1', images[currentIndex]);
                        }

                        function nextImage() {
                            currentIndex = (currentIndex + 1) % images.length;
                            changeImage('example1', images[currentIndex]);
                        }

                        function toggleCarousel() {
                            var button = document.querySelector("button:last-of-type");
                            if (intervalId) {
                                clearInterval(intervalId);
                                intervalId = null;
                                button.textContent = "開始";
                            } else {
                                intervalId = setInterval(function() {
                                    nextImage();
                                }, 1000);
                                button.textContent = "暫停";
                            }
                        }

                        toggleCarousel();
                    </script> 
            </div>
                
            <div class ="colum middle">
                <h4>故事 旅遊</h4>
                <p><a href ="/story">相識到相戀故事</a></p>
                <img src = "static/lv.jpg" width ="350"> 
                <iframe src="https://www.youtube.com/embed/t5O51RmCTsg" allowfullscreen width="300" height="350" ></iframe>
            </div>

            <div class="colum side">
                <h4>照片牆</h4>
                <p><a href ="/photo">照片牆2023</a></p>  
                <img src = "static/hug.jpg" width ="350"> 
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