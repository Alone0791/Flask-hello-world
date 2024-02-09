from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    file = open("hi", "r")
    return f"<pre><code>{file.read()}<code><pro>"

@app.route('/pro', methods=['GET', 'POST'])
def paste():
    if request.method == 'POST':
        file = open("hi", "w")
        file.write(request.data.decode("utf-8"))
        return "Done"

if __name__ == '__main__':
    app.run(debug=True)
