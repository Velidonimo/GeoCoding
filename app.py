from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
from coords_finder import coords_finder


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/success/', methods=["POST"])
def success():
    if request.method == "POST":
        file = request.files['file_name']
        done, message = coords_finder(file)
        return render_template('success.html', data_frame=message, show_btn=done)


@app.route("/file_download/")
def file_download():
    file_to_download = send_file("Nice.csv", attachment_filename="Your Coordinates.csv", as_attachment=True)
    # clearing cache
    file_to_download.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"

    return file_to_download


if __name__ == '__main__':
    app.run(debug=True)
