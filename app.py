from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
from threading import Thread
from coords_finder import coords_finder



app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/updating/', methods=["POST"])
def updating():
    if request.method == "POST":
        file = request.files['file_name']
        global filename
        filename = secure_filename(file.filename)
        thread = Thread(target=coords_finder, args=(filename, success))
        thread.start()
        return render_template('updating.html')


@app.route('/success/')
def success(done, message):
    return render_template('success.html', data_frame=message, show_btn=done)


@app.route("/file_download/")
def file_download():
    # adding "+coords" to filename
    new_name = ".".join(filename.split(".")[:-1]) + "+Coords.csv"
    file_to_download = send_file("Nice.csv", attachment_filename=new_name, as_attachment=True)
    # clearing cache
    file_to_download.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"

    return file_to_download


if __name__ == '__main__':
    app.run(debug=True)
