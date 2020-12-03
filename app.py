from flask import Flask, render_template, request
import pandas


app = Flask("__main__")

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/success/', methods=["POST"])
def success():
    if request.method == "POST":
        file = request.files['file_name']
        df = pandas.read_csv(file)

        return render_template('success.html', dataframe=df.to_html())


if __name__ == '__main__':
    app.run(debug=True)
