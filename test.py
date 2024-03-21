from flask import Flask

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Website</title>
</head>
<body style="background-color: lightblue;">
    <h1>Welcome to My Website</h1>
    <p>This is some content on my website.</p>
</body>
</html>
"""

@app.route("/")
def index():
    return html

if __name__ == "__main__":
    app.run()
