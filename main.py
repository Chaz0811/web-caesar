print("top")
from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True
print("top1")
form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form>
        <form action="/encrypt" methods="POST">
        <label for "rot">Rotate by:</label>
        <input type = "text" name = "rot">
        <textarea type = "text" name = "text">{0}</textarea>
        <input type="submit" value="Submit">




    </body>
</html>

"""
print("top3")
@app.route("/")
def index():
    print("top2")
    return form.format("")
    

@app.route("/encrypt", methods =['POST'])
def encrypt(text, rot):
    coded_text = ""
    rot = int(request.form["rot"])
    text = request.form["text"]
    print("this is bullshit")


    return form.format(rotate_string(text,rot))




app.run
