from flask import Flask, render_template, request, send_file
import pandas


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
        return render_template('success.html',
                data_frame=df.to_html(max_rows=10, max_cols=8, classes="table"))


@app.route("/file_download/")
def file_download():
    # adding "+coords" to filename
    new_name = ".".join(file.filename.split(".")[:-1]) + "+coords.csv"

    file_to_download = send_file(file.filename, attachment_filename=new_name, as_attachment=True)
    # clearing cache
    file_to_download.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"

    # TODO add new btn to return to main page

    return file_to_download


if __name__ == '__main__':
    app.run(debug=True)
