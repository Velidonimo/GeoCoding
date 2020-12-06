from flask import Flask, render_template, request, send_file
import pandas
from werkzeug.utils import secure_filename


app = Flask("__main__")

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/success/', methods=["POST"])
def success():
    if request.method == "POST":
        global file
        file = request.files['file_name']
        df = pandas.read_csv(file)
        print("Address" in df)
        return render_template('success.html',
                data_frame=df.to_html(max_rows=10, max_cols=8, classes="table"))


@app.route("/file_download/")
def file_download():
    # adding "+coords" to filename
    filename = secure_filename(file.filename)
    new_name = ".".join(filename.split(".")[:-1]) + "+Coords.csv"

    file_to_download = send_file(filename, attachment_filename=new_name, as_attachment=True)
    # clearing cache
    file_to_download.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"

    return file_to_download


if __name__ == '__main__':
    app.run(debug=True)
